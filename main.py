from projectKidney import logger
from projectKidney.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x"
        )

    except Exception as e:
        logger.exception(e)
        raise e
