import pandas as pd
import streamlit as st
import pyodbc
import os
import google.generativeai as genai
from SQLCredential import login, Pass

server = 'oibs-dev-server.database.windows.net'
database = 'OIBS'
username = login
password = Pass

# Establishing a connection to the SQL Server
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+password)

df = pd.read_sql(
    """
    SELECT TOP (100) * FROM DM_Foresight.VW_V4_DATES_REBUILD
    """
    , cnxn)

## Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Define Your Prompt
prompt=[
    """
    You are an expert in analyzing data and giving your valuable advice as per the user query.\n
    Please analyze the data first and give the answers as per your expertise.\n
    Also give the SQL code as a result to tell the user how to come to this particular conclusion.

    """
]


## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=df(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)