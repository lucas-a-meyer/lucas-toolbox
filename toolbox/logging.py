import os
import logging

def initialize_logger(program_name : str = __name__ ) -> logging.Logger:
    if program_name == "___main__":      
        # get the filename of the main script that is calling this function
        program_name = os.path.basename(__import__("__main__").__file__)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program_name)

    logger_blocklist = [
        "azure.core.pipeline.policies.http_logging_policy",
    ]

    for module in logger_blocklist:
        logging.getLogger(module).setLevel(logging.WARNING)

    return logger