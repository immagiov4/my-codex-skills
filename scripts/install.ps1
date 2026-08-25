$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repositoryRoot "skills"
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$targetRoot = Join-Path $codexRoot "skills"
$sourcePrefix = $sourceRoot.TrimEnd("\") + "\"

New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null

Get-ChildItem -LiteralPath $sourceRoot -File -Recurse | ForEach-Object {
    $relativePath = $_.FullName.Substring($sourcePrefix.Length)
    $targetPath = Join-Path $targetRoot $relativePath
    $targetDirectory = Split-Path -Parent $targetPath
    New-Item -ItemType Directory -Path $targetDirectory -Force | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $targetPath -Force
}

Write-Host "Installed Codex skills in $targetRoot"
