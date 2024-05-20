import os
import dotenv
import logging
import logging.config

from datetime import datetime

env_file = dotenv.find_dotenv()
dotenv.load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration."""
    log_configs = {"dev": "logging.dev.init", "prod": "logging.prod.init"}
    config = log_configs.get(os.environ["ENV"], "logging.dev.init")
    config_path = f"{CONFIG_DIR}/{config}"

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )
