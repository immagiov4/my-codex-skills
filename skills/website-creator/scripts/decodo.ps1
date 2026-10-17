<# Runs the official Decodo CLI with a Windows user-encrypted token.
   The token is exposed only to this process and its CLI child while it runs. #>
[CmdletBinding(DefaultParameterSetName = 'Cli')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Cli')][string[]]$CliArgs,
    [Parameter(Mandatory, ParameterSetName = 'Request')][string]$RequestFile,
    [Parameter(Mandatory, ParameterSetName = 'Request')][string]$OutputFile,
    [string]$CredentialPath,
    [string]$CliPath
)
$ErrorActionPreference = 'Stop'
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
if (!$CredentialPath) { $CredentialPath = Join-Path $codexRoot 'private/decodo-token.clixml' }
if (!$CliPath) { $CliPath = Join-Path $codexRoot 'tools/decodo/node_modules/@decodo/cli/build/esm/index.js' }
if (!(Test-Path -LiteralPath $CredentialPath)) {
    throw 'Decodo credential missing. Complete the local credential setup first.'
}
if (!(Test-Path -LiteralPath $CliPath)) {
    throw 'Official Decodo CLI missing. Install it as documented in references/decodo.md.'
}
$secret = Import-Clixml -LiteralPath $CredentialPath
if ($secret -isnot [System.Security.SecureString]) {
    throw 'The credential file must contain a Windows-encrypted SecureString.'
}
$previousToken = $env:DECODO_AUTH_TOKEN
try {
    $credential = New-Object System.Management.Automation.PSCredential('Decodo', $secret)
    $env:DECODO_AUTH_TOKEN = $credential.GetNetworkCredential().Password
    if ($PSCmdlet.ParameterSetName -eq 'Request') {
        & node (Join-Path $PSScriptRoot 'decodo-request.mjs') $CliPath $RequestFile $OutputFile
    } else {
        & node $CliPath @CliArgs
    }
    $cliExitCode = $LASTEXITCODE
} finally {
    $env:DECODO_AUTH_TOKEN = $previousToken
    $credential = $null
    $secret.Dispose()
}
exit $cliExitCode
