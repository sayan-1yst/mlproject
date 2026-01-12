import os
import sys
import pandas as pd
import pyodbc
from dotenv import load_dotenv
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

load_dotenv()

host = os.getenv("host")        # localhost\\SQLEXPRESS02
user = os.getenv("user")        # root
password = os.getenv("password")
db = os.getenv("db")            # college


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={host};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={password};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )

        logging.info("Connection established")

        query = "SELECT * FROM Students"
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    except Exception as ex:
        raise CustomException(ex, sys)
