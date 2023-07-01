# Generate sample data
$data = @"
Name,Age,Country
John,25,USA
Jane,30,UK
Alex,28,Canada
"@

# Convert data to objects
$objects = $data | ConvertFrom-Csv

# Format the data and convert it to a string
$output = $objects | Format-Table | Out-String

# Print the output on the screen
Write-Output $output
