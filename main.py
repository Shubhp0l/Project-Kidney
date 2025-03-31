from projectKidney import logger
from projectKidney.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from projectKidney.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

from projectKidney.pipeline.stage_03_training import TrainingPipeline

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

STAGE_NAME = "TRAINING"

try:
    logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e
