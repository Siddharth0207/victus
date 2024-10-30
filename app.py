from src.myproject.logger import logging
from src.myproject.exception import CustomException
import sys
from src.myproject.components.data_ingestion import DataIngestion
from src.myproject.components.data_ingestion import DataIngestionConfig

if __name__ == '__main__':
    logging.info('The execution of the program has started')

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception has been raised")
        raise CustomException(e,sys)