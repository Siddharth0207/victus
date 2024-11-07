import os 
import sys 
from src.myproject.exception import CustomException
from src.myproject.logger import logging

import pandas as pd 
from dotenv import load_dotenv
import pymysql


import pickle
import numpy as np 
import pandas as pd


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

def save_object(file_path, obj):
    """
    This function is responsible for saving the object as a pickle file
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object has been saved at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)
