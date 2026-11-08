param(
    [Parameter(Mandatory = $true)][string]$Path,
    [Parameter(Mandatory = $true)][string]$ApprovedParent,
    [Parameter(Mandatory = $true)][string]$RecoveryRoot,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
if (-not [OperatingSystem]::IsWindows()) { throw 'This helper requires PowerShell 7 on Windows.' }
foreach ($suppliedPath in @($Path, $ApprovedParent, $RecoveryRoot)) {
    if (-not [IO.Path]::IsPathFullyQualified($suppliedPath)) { throw 'Supply absolute paths.' }
}
$target = [IO.Path]::TrimEndingDirectorySeparator([IO.Path]::GetFullPath($Path))
$parent = [IO.Path]::TrimEndingDirectorySeparator([IO.Path]::GetFullPath($ApprovedParent))
$recovery = [IO.Path]::TrimEndingDirectorySeparator([IO.Path]::GetFullPath($RecoveryRoot))
$targetParent = [IO.Directory]::GetParent($target)
if ($null -eq $targetParent -or -not $targetParent.FullName.Equals($parent, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'The target must be one immediate child of the approved parent, not the parent itself.'
}
if (-not [IO.Path]::GetPathRoot($target).Equals([IO.Path]::GetPathRoot($recovery), [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Recovery storage must be on the same volume; copy-and-delete is not supported.'
}
if ($recovery.Equals($target, [StringComparison]::OrdinalIgnoreCase) -or $recovery.StartsWith($target + '\', [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Recovery storage must be outside the target.'
}

function Assert-RealDirectoryPath([string]$DirectoryPath) {
    $entryPath = $DirectoryPath
    while ($entryPath) {
        $entry = Get-Item -LiteralPath $entryPath -Force -ErrorAction SilentlyContinue
        if ($entry -and (-not $entry.PSIsContainer -or ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint))) {
            throw 'Target, recovery storage and their ancestors must be real directories, not files or links.'
        }
        $ancestor = [IO.Directory]::GetParent($entryPath)
        $entryPath = if ($ancestor) { $ancestor.FullName } else { $null }
    }
}

Assert-RealDirectoryPath $target
Assert-RealDirectoryPath $recovery
if (-not [IO.Directory]::Exists($parent)) { throw 'The approved parent does not exist.' }
if (-not [IO.Directory]::Exists($target)) {
    @{ path = $target; result = 'already-absent' } | ConvertTo-Json -Compress
    return
}
if (-not $Execute) {
    @{ path = $target; recoveryRoot = $recovery; result = 'preview' } | ConvertTo-Json -Compress
    return
}

[IO.Directory]::CreateDirectory($recovery) | Out-Null
$destination = Join-Path $recovery ([IO.Path]::GetFileName($target) + '-' + [Guid]::NewGuid().ToString('N'))
# A same-volume rename preserves the complete tree without a permanent-delete fallback.
[IO.Directory]::Move($target, $destination)
if ([IO.Directory]::Exists($target) -or -not [IO.Directory]::Exists($destination)) {
    throw 'Retirement did not complete; inspect the source and recovery destination.'
}
@{ path = $target; recoveryPath = $destination; result = 'retired' } | ConvertTo-Json -Compress
