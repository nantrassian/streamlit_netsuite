import streamlit as st
# variables.py

# Remove options for other databases and schemas
# Set default values to your BigQuery database and schema
DATABASE = 'fivetranintegration-393217'
SCHEMA = 'netsuite_suiteanalytics_netsuite'
DESTINATION = 'BigQuery'
def database_schema_variables():
        st.session_state.database = DATABASE
        st.session_state.schema = SCHEMA
