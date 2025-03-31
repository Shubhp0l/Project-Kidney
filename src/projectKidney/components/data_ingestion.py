import os
import zipfile
import gdown
from projectKidney import logger
from projectKidney.utils.common import get_size
from projectKidney.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        try:
            url = self.config.source
            zip_dir = self.config.local_data_dir
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {url} into {zip_dir}")

            file_id = url.split("/")[-2]
            prefix = ""
            gdown.download(prefix + file_id, zip_dir)

            logger.info(f"Data Downloaded to {zip_dir}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_dir, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
