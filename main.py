from projectKidney import logger
from projectKidney.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from projectKidney.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x")


except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "PREPARE BASE MODEL"

try:
    logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e
