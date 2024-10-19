from mlProject import logger
from mlProject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from mlProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

logger.info("Welcome to Diamond Price Prediction Project!")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e