import logging
import time
from time import sleep

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    print(event)

    sleep(5.0)
    
    return "KEEP_WAITING"