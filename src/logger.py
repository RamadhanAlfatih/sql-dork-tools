import logging
import os

def setup_logger():
    """
    Set up logging configuration.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=os.path.join(log_dir, "app.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )