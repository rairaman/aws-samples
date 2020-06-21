import pytest
import mockito
import time

from src import index
from mockito import when
from src.index import get_wait_status, is_job_complete

@pytest.mark.parametrize("wait_timeout, input_secs_before_timeout, expected",[
    (0, 0, {'seconds_before_timeout': 0 , 'wait_status': 'JOB_WAIT_TIMEOUT'}),
    (0, 10, {'seconds_before_timeout': 0 , 'wait_status': 'JOB_WAIT_TIMEOUT'}),
    (-1, 0, {'seconds_before_timeout': 0 , 'wait_status': 'JOB_WAIT_TIMEOUT'}),
])
def test_get_wait_status_with_unlikely_time_waits(wait_timeout, input_secs_before_timeout, expected):

    when(index).is_job_complete().thenReturn(False)
    actual = get_wait_status(wait_timeout, input_secs_before_timeout)
    assert actual == expected


@pytest.mark.parametrize("wait_timeout, input_secs_before_timeout, expected_status",[
    (15, 8, 'KEEP_WAITING'),
    (15,0, 'JOB_WAIT_TIMEOUT')
])
def test_get_wait_status_expected_time_waits(wait_timeout, input_secs_before_timeout, expected_status):
    when(index).is_job_complete().thenReturn(False)
    total_secs_before_timeout = int(time.time()) + input_secs_before_timeout
    actual = get_wait_status(wait_timeout, total_secs_before_timeout)['wait_status']
    assert actual == expected_status

def test_get_wait_status_job_completed():
    when(index).is_job_complete().thenReturn(True)
    actual = get_wait_status(15, 0)['wait_status']
    assert actual == 'JOB_COMPLETED'
    