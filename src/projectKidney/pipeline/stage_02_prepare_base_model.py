from projectKidney.config.configuration import configurationManager
from projectKidney.components.prepare_base_model import PrepareBaseModel
from projectKidney import logger


STAGE_NAME = "PREPARE BASE MODEL"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = configurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x"
        )

    except Exception as e:
        logger.exception(e)
        raise e
