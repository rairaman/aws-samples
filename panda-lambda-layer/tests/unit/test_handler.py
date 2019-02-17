from collections import namedtuple
import json

import pytest

from panda-layer-demo import app


@pytest.fixture()
def panda_layer_demo_event():
    return 0


def test_lambda_handler(panda_layer_demo_event, mocker):

    assert panda_layer_demo_event == 0
