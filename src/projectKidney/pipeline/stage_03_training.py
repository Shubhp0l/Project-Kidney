from projectKidney.config.configuration import configurationManager
from projectKidney.components.training import Training
from projectKidney import logger


STAGE_NAME = "TRAINING"


class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = configurationManager()
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()

        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x"
        )

    except Exception as e:
        logger.exception(e)
        raise e
