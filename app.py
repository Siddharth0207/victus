from src.myproject.logger import logging
from src.myproject.exception import CustomException
import sys
from src.myproject.components.data_ingestion import DataIngestion
from src.myproject.components.data_ingestion import DataIngestionConfig
from src.myproject.components.data_transformation import DataTransformation
from src.myproject.components.data_transformation import DataTransformationConfig

if __name__ == '__main__':
    logging.info('The execution of the program has started')

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        #data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        
    except Exception as e:
        logging.info("Custom Exception has been raised")
        raise CustomException(e,sys)