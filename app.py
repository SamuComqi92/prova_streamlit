import subprocess
import streamlit as st

def execute_powershell_script(script_path):
    # Run PowerShell script
    process = subprocess.Popen(["powershell", "data.ps1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    # Decode the output
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    return output, error

# Streamlit app
st.title("PowerShell Script Execution")

# Upload the PowerShell script
script_file = st.file_uploader("Upload PowerShell Script", type=".ps1")

if script_file is not None:
    # Save the uploaded script to a temporary file
    with open("temp_script.ps1", "wb") as f:
        f.write(script_file.read())

    # Execute the PowerShell script
    output, error = execute_powershell_script("temp_script.ps1")

    # Display the output and error
    st.subheader("Output:")
    st.code(output)

    st.subheader("Error:")
    st.code(error)
