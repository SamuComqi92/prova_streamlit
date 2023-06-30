import streamlit as st
import pandas as pd
import subprocess

# Execute PowerShell script
subprocess.run(["powershell", "./data.ps1"], shell=True)

# Read CSV data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Display the DataFrame using Streamlit
st.dataframe(df)