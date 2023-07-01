# Import the module
Import-Module -Name MicrosoftPowerBIMgmt

# Authenticate to Power BI
Connect-PowerBIServiceAccount

# Specify the workspace ID of the desired workspace
$workspaceId = "your_workspace_id"

# Retrieve reports from the specified workspace
$reports = Get-PowerBIReport -WorkspaceId $workspaceId

# Specify the output file path and name for the CSV file
$csvFilePath = "output.csv"

# Export the reports to a CSV file
$reports | Export-Csv -Path $csvFilePath -NoTypeInformation

# Confirmation message
Write-Host "Reports saved to $csvFilePath"
