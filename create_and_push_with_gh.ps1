<#
create_and_push_with_gh.ps1

Usage: run this in PowerShell from the project root. The script will:
 - ensure GitHub CLI (gh) is installed (via winget if available)
 - run `gh auth login` (interactive browser flow)
 - create the repo under the provided GitHub username and push current branch

This script is interactive and does not store credentials. It uses the web auth flow.
#>

param(
    [string]$GitHubUser = 'gatorMiner',
    # Default repo name to current folder name so the script works when this folder is a standalone project
    [string]$RepoName = (Split-Path -Leaf (Get-Location).Path),
    [ValidateSet('public','private')]
    [string]$Visibility = 'public',
    # Use -Force to allow creating a nested git repo inside another repo (not recommended)
    [switch]$Force
)

function Write-Info($msg){ Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Err($msg){ Write-Host "[ERROR] $msg" -ForegroundColor Red }

$cwd = (Get-Location).Path.TrimEnd('\')

# Detect if we are already inside an existing git repository (could be a parent repo)
$insideRepo = $false
$toplevel = $null
try {
    $toplevel = git rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -eq 0 -and $toplevel) { $insideRepo = $true; $toplevel = $toplevel.TrimEnd("`r","`n") }
} catch {}

if ($insideRepo) {
    # Compare paths; on Windows paths may differ in case — normalize to lower for comparison
    if (([io.path]::GetFullPath($toplevel).TrimEnd('\').ToLower()) -ne ([io.path]::GetFullPath($cwd).TrimEnd('\').ToLower()) ) {
        if (-not $Force) {
            Write-Err "This directory appears to be inside another git repository at: $toplevel."
            Write-Err "Move this folder outside the parent repo or re-run with -Force to create a nested repo (not recommended). Aborting."
            exit 1
        } else {
            Write-Info "Force: creating nested git repository inside parent repo at $toplevel."
        }
    } else {
        Write-Info "Current directory is the top-level git repository. Continuing..."
    }
} else {
    Write-Info "No existing git repository detected. Initializing repository in current folder..."
    git init
}

# Ensure there is at least one commit
try {
    git rev-parse --verify HEAD > $null 2>&1
    $hasHead = $true
} catch {
    $hasHead = $false
}
if (-not $hasHead){
    Write-Info "No commits found. Creating initial commit..."
    git add -A
    # Best-effort commit; if user identity isn't set this may still fail — keep output visible
    git commit -m "chore: initial scaffold for $RepoName" --author="$GitHubUser <${GitHubUser}@users.noreply.github.com>" > $null 2>&1
}

# Check for gh
$ghPath = (Get-Command gh -ErrorAction SilentlyContinue)
if (-not $ghPath) {
    Write-Info "GitHub CLI (gh) not found. Attempting to install via winget..."
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($winget) {
        Write-Info "Installing gh with winget (requires admin or user acceptance)..."
        winget install --id GitHub.cli -e --accept-package-agreements --accept-source-agreements
        Start-Sleep -Seconds 2
        # re-check
        $ghPath = (Get-Command gh -ErrorAction SilentlyContinue)
        if (-not $ghPath) {
            Write-Err "gh still not available. Please restart your shell or install gh manually from https://github.com/cli/cli/releases/latest"
            exit 1
        }
    } else {
        Write-Err "winget not available. Please install gh manually: https://github.com/cli/cli/releases/latest and re-run this script."
        exit 1
    }
}

Write-Info "gh found: $($ghPath.Path)"

# Ensure authenticated
$authOk = $false
try {
    gh auth status > $null 2>&1
    if ($LASTEXITCODE -eq 0) { $authOk = $true }
} catch {}

if (-not $authOk) {
    Write-Info "You need to authenticate gh. We'll run 'gh auth login' now. Follow the browser prompts."
    gh auth login --web
    if ($LASTEXITCODE -ne 0) {
        Write-Err "gh auth login failed. Please run 'gh auth login' manually and re-run this script."
        exit 1
    }
}

# Confirm we are authenticated as expected
$login = gh api user --jq .login 2>$null
if (-not $login) {
    Write-Err "Unable to detect authenticated user from gh. Run 'gh auth login' and try again."
    exit 1
}
Write-Info "Authenticated as $login"

# Create the repo via gh
$fullRepo = "$GitHubUser/$RepoName"
Write-Info "Creating GitHub repo $fullRepo (visibility=$Visibility) and pushing current branch..."

# Attempt creation. If it already exists, gh will exit non-zero.
Write-Info "Running: gh repo create $fullRepo --$Visibility --source . --remote origin --push"
gh repo create $fullRepo --$Visibility --source . --remote origin --push > $null 2>&1
$createExit = $LASTEXITCODE

if ($createExit -eq 0) {
    Write-Info "Repository created and pushed successfully."
    exit 0
}

Write-Info "gh repo create failed or repo may already exist. Falling back to manual remote setup and push."

# Fallback: ensure remote exists and push
$remoteUrl = "https://github.com/$GitHubUser/$RepoName.git"
# remove existing origin if any
git remote remove origin 2>$null
git remote add origin $remoteUrl

Write-Info "Pushing main branch to $remoteUrl ..."
# Ensure branch is main or get current branch
$currentBranch = (git branch --show-current) -replace '\r',''
if (-not $currentBranch) { $currentBranch = 'main' }

# If local branch is not named main, push current branch to main
if ($currentBranch -ne 'main') {
    Write-Info "Current branch is '$currentBranch' — pushing it to remote as 'main' (create remote main)."
    git push -u origin $currentBranch:main
    $pushExit = $LASTEXITCODE
} else {
    git push -u origin main
    $pushExit = $LASTEXITCODE
}

if ($pushExit -eq 0) {
    Write-Info "Push succeeded. Verify repository at: https://github.com/$fullRepo"
    exit 0
} else {
    Write-Err "Push failed with exit code $pushExit. Ensure you have permission to create/push to the repository and that the remote exists."
    exit $pushExit
}
