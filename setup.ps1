# Create all necessary directories
$baseDir = "C:\Users\langh\FinDoV2"

# Main directories
$directories = @(
    "frontend",
    "backend\api-gateway",
    "backend\auth-service",
    "backend\todo-service",
    "backend\expense-service",
    "ml-service",
    "deploy"
)

# Create each directory
foreach ($dir in $directories) {
    $fullPath = Join-Path -Path $baseDir -ChildPath $dir
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        Write-Host "Created directory: $fullPath"
    } else {
        Write-Host "Directory already exists: $fullPath"
    }
}

Write-Host "Project structure created successfully!"
