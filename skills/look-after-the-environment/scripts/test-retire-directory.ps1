param([Parameter(Mandatory = $true)][string]$TestRoot)

$ErrorActionPreference = 'Stop'
$helper = Join-Path $PSScriptRoot 'retire-directory.ps1'
$root = Join-Path $TestRoot ('retire-test-' + [Guid]::NewGuid().ToString('N'))
$recovery = Join-Path $root 'recovery'
[IO.Directory]::CreateDirectory($root) | Out-Null

function Assert-True([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}
function Assert-Rejected([scriptblock]$Action, [string]$ExpectedMessage) {
    try { & $Action | Out-Null }
    catch {
        Assert-True ($_.Exception.Message.Contains($ExpectedMessage)) 'Unexpected rejection reason.'
        return
    }
    throw 'Unsafe target was accepted.'
}

$preview = Join-Path $root 'preview'
[IO.Directory]::CreateDirectory($preview) | Out-Null
[IO.File]::WriteAllText((Join-Path $preview 'keep.txt'), 'keep')
$result = & $helper -Path $preview -ApprovedParent $root -RecoveryRoot $recovery | ConvertFrom-Json
Assert-True ($result.result -eq 'preview') 'Preview result missing.'
Assert-True ([IO.File]::ReadAllText((Join-Path $preview 'keep.txt')) -eq 'keep') 'Preview altered files.'
Write-Output 'PASS: preview preserves the target'

$volumeRoot = [IO.Path]::GetPathRoot($root)
$absentRootChild = Join-Path $volumeRoot ('cleanup-preview-' + [Guid]::NewGuid().ToString('N'))
$result = & $helper -Path $absentRootChild -ApprovedParent $volumeRoot -RecoveryRoot $recovery | ConvertFrom-Json
Assert-True ($result.result -eq 'already-absent') 'Volume-root parent was not accepted.'
Assert-True (-not (Test-Path -LiteralPath $absentRootChild)) 'Preview created a root child.'
Write-Output 'PASS: volume-root parent preview preserves root-path semantics'

Assert-Rejected { & $helper -Path $preview -ApprovedParent $TestRoot -RecoveryRoot $recovery -Execute } 'immediate child'
Assert-True (Test-Path -LiteralPath $preview) 'Wrong-parent target disappeared.'
Write-Output 'PASS: outside-parent target is rejected'

Assert-Rejected { & $helper -Path $root -ApprovedParent $root -RecoveryRoot $recovery -Execute } 'immediate child'
Assert-True (Test-Path -LiteralPath $preview) 'Parent-root rejection lost data.'
Write-Output 'PASS: parent root is rejected'

Assert-Rejected { & $helper -Path $preview -ApprovedParent $root -RecoveryRoot (Join-Path $preview 'inside') -Execute } 'outside the target'
Assert-True (Test-Path -LiteralPath $preview) 'Nested recovery target lost data.'
Write-Output 'PASS: recovery inside the target is rejected'

$otherVolume = if ([IO.Path]::GetPathRoot($root) -eq 'C:\') { 'D:\' } else { 'C:\' }
Assert-Rejected { & $helper -Path $preview -ApprovedParent $root -RecoveryRoot (Join-Path $otherVolume 'cleanup-test-recovery') -Execute } 'same volume'
Assert-True (Test-Path -LiteralPath $preview) 'Cross-volume rejection lost data.'
Write-Output 'PASS: cross-volume recovery is rejected before mutation'

$protected = Join-Path $root 'protected'
[IO.Directory]::CreateDirectory($protected) | Out-Null
$sentinel = Join-Path $protected 'sentinel.txt'
[IO.File]::WriteAllText($sentinel, 'protected')
$link = Join-Path $root 'linked-target'
New-Item -ItemType Junction -Path $link -Target $protected | Out-Null
Assert-Rejected { & $helper -Path $link -ApprovedParent $root -RecoveryRoot $recovery -Execute } 'not files or links'
Assert-Rejected { & $helper -Path $preview -ApprovedParent $root -RecoveryRoot (Join-Path $link 'recovery') -Execute } 'not files or links'
$linkedChild = Join-Path $protected 'child'
[IO.Directory]::CreateDirectory($linkedChild) | Out-Null
Assert-Rejected { & $helper -Path (Join-Path $link 'child') -ApprovedParent $link -RecoveryRoot $recovery -Execute } 'not files or links'
Assert-True (Test-Path -LiteralPath $linkedChild) 'Target-ancestor rejection moved data.'
Assert-True ([IO.File]::ReadAllText($sentinel) -eq 'protected') 'Junction rejection lost data.'
Write-Output 'PASS: junction targets, target ancestors and recovery ancestors are rejected'

$longTarget = Join-Path $root 'long-target'
$segments = foreach ($index in 1..5) { ('deep-' + $index + '-') + ('x' * 70) }
$relative = [IO.Path]::Combine([string[]]$segments)
$deep = Join-Path $longTarget $relative
[IO.Directory]::CreateDirectory($deep) | Out-Null
$longFile = Join-Path $deep 'fixture.txt'
[IO.File]::WriteAllText($longFile, 'long-path-fixture')
Assert-True ($longFile.Length -gt 260) 'Fixture does not reproduce the legacy path limit.'
New-Item -ItemType Junction -Path (Join-Path $longTarget 'shared-cache-link') -Target $protected | Out-Null
$result = & $helper -Path $longTarget -ApprovedParent $root -RecoveryRoot $recovery -Execute | ConvertFrom-Json
Assert-True ($result.result -eq 'retired') 'Retirement result missing.'
Assert-True (-not (Test-Path -LiteralPath $longTarget)) 'Long-path target remains.'
$recoveredFile = Join-Path (Join-Path $result.recoveryPath $relative) 'fixture.txt'
Assert-True ([IO.File]::ReadAllText($recoveredFile) -eq 'long-path-fixture') 'Recovery copy is incomplete.'
Assert-True ([IO.File]::ReadAllText($sentinel) -eq 'protected') 'Retirement followed an internal junction.'
[IO.Directory]::Move($result.recoveryPath, $longTarget)
Assert-True ([IO.File]::ReadAllText($longFile) -eq 'long-path-fixture') 'Actual restoration failed.'
Assert-True ([IO.File]::ReadAllText($sentinel) -eq 'protected') 'Restoration damaged shared data.'
Write-Output 'PASS: long paths retire and restore; linked shared data survives'

& $helper -Path $longTarget -ApprovedParent $root -RecoveryRoot $recovery -Execute | Out-Null
$result = & $helper -Path $longTarget -ApprovedParent $root -RecoveryRoot $recovery -Execute | ConvertFrom-Json
Assert-True ($result.result -eq 'already-absent') 'Repeated cleanup is not idempotent.'
Write-Output 'PASS: already absent target is a successful no-op'

& $helper -Path $root -ApprovedParent $TestRoot -RecoveryRoot (Join-Path $TestRoot 'retired-tests') -Execute | Out-Null
Assert-True (-not (Test-Path -LiteralPath $root)) 'Test workspace retirement failed.'
Write-Output 'PASS: test workspace retirement completed'
