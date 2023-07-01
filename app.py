import subprocess

# Execute the PowerShell script
subprocess.run(["pwsh", "-File", "data.ps1"], shell=True)

# Read the CSV file generated by the PowerShell script
csv_file_path = "output.csv"
with open(csv_file_path, "r") as file:
    csv_content = file.read()

# Display the CSV content using Streamlit
import streamlit as st

st.code(csv_content, language="csv")
