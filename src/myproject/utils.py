import os 
import sys 
from src.myproject.exception import CustomException
from src.myproject.logger import logging

import pandas as pd 
from dotenv import load_dotenv
import pymysql


#Loading the Data from .env file inorder to use the same credentials  in all the files
logging.info("Loading the Data from .env file")
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password= os.getenv('password')
db = os.getenv('db')




def read_sql_data():
    logging.info("Reading the Data from MySQL has started.")
    # this will basically retutn the dataset from the database
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection has been established")
        df =  pd.read_sql_query('Select * from kidney_disease', mydb)
        print(df.head())

        return df


    except Exception as e:
        raise CustomException(e,sys)

