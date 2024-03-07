

import sys
from cnnClassifier import logger
from ExceptionFile.exception import CustomException
from cnnClassifier.pipeline.stage_01_DataIngestion import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        raise CustomException(e , sys)