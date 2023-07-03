import os
import logging

def initialize_logger(program_name : str = __name__ ) -> logging.Logger:
    if program_name == "___main__":
        # get script filename
        program_name = os.path.basename(__file__).split('.')[0]
        
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(program_name)

    logger_blocklist = [
        "azure.core.pipeline.policies.http_logging_policy",
    ]

    for module in logger_blocklist:
        logging.getLogger(module).setLevel(logging.WARNING)

    return logger