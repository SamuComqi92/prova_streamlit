# data.ps1

# Generate sample data
$data = @"
Name,Age,Country
John,25,USA
Jane,30,UK
Alex,28,Canada
"@

# Save data as a CSV file
$data | ConvertFrom-Csv | Export-Csv -Path "data.csv" -NoTypeInformation