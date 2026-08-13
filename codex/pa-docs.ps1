param(
  [Parameter(Position=0,Mandatory=$true)][ValidateSet('search','update','status','import-koi')] [string]$Command,
  [Parameter(ValueFromRemainingArguments=$true)] [string[]]$Arguments
)
$projectRoot = $PSScriptRoot
$python = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $python) {
  $candidate = 'C:\Users\yarin.s\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
  if (Test-Path -LiteralPath $candidate) { $python = $candidate }
}
if (-not $python) { throw 'Python 3.10+ was not found.' }
switch ($Command) {
  'search' { & $python "$projectRoot\scripts\search.py" @Arguments }
  'update' { & $python "$projectRoot\scripts\ingest.py" @Arguments }
  'status' { & $python "$projectRoot\scripts\status.py" @Arguments }
  'import-koi' { & $python "$projectRoot\scripts\import_koi.py" @Arguments }
}
exit $LASTEXITCODE
