import logging
import time
import json
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

wait_timeout = int(os.environ.get('JOB_WAIT_TIMEOUT',1800))

def is_job_complete():
    # Check for completion of your long running job here
    return True

def get_wait_status(time_to_wait, input_secs_before_timeout):
    if is_job_complete():
        return {'seconds_before_timeout': 0 , 'wait_status': 'JOB_COMPLETED'}
    else:
        if time_to_wait <= 0:
            return {'seconds_before_timeout': 0 , 'wait_status': 'JOB_WAIT_TIMEOUT'}

        if input_secs_before_timeout == -1:
            seconds_before_timeout = int(time.time()) + time_to_wait
        else:
            seconds_before_timeout = input_secs_before_timeout - int(time.time())
            
        if seconds_before_timeout > 0:
            return {'seconds_before_timeout': seconds_before_timeout, 'wait_status': 'KEEP_WAITING'}
        else:
            return {'seconds_before_timeout': seconds_before_timeout, 'wait_status': 'JOB_WAIT_TIMEOUT'}

def lambda_handler(event, context):
    input_secs_before_timeout = event.get('seconds_before_timeout',-1)
    return get_wait_status(wait_timeout, input_secs_before_timeout)

