import streamlit as st
import functions.variables
#from functions.variables import database_schema_variables, destination_selection

st.sidebar.header('Data Connection Variables')
destination = functions.variables.DESTINATION
database, schema = functions.variables.DATABASE, functions.variables.SCHEMA

# Read the README contents
with open("README.md", "r") as f:
    readme_content = f.read()

# Render the README as markdown in the app
st.markdown(readme_content)
