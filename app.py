import subprocess
import streamlit as st

def execute_powershell_script(script_path):
    # Run PowerShell script
    process = subprocess.Popen(["powershell.exe", "-File", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    # Decode the output
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    return output, error

# Streamlit app
st.title("PowerShell Script Execution")

# Path to the PowerShell script
script_path = "data.ps1"

# Execute the PowerShell script
output, error = execute_powershell_script(script_path)

# Display the output and error
st.subheader("Output:")
st.code(output)

st.subheader("Error:")
st.code(error)
