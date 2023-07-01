import streamlit as st
import pandas as pd
import subprocess

# Execute PowerShell script and capture the output
result = subprocess.run(["powershell", "data.ps1"], shell=True, capture_output=True, text=True)

# Check if the PowerShell script executed successfully
if result.returncode == 0:
    # Convert the output to a string
    output = result.decode("utf-8")
    
    # Parse the CSV data and create a pandas DataFrame
    df = pd.read_csv(pd.compat.StringIO(output))
    
    # Display the DataFrame using Streamlit
    st.dataframe(df)
else:
    # Display the error message
    error_message = result.stderr if result.stderr else result.stdout
    st.error(f"PowerShell script execution failed:\n{error_message}")


