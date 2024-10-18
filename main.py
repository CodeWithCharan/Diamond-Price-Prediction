from mlProject import logger
from mlProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

logger.info("Welcome to Diamond Price Prediction Project!")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"\n>>>>>> {STAGE_NAME} started <<<<<<\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n>>>>>> {STAGE_NAME} completed <<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e