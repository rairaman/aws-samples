import json
import numpy as np
# import pandas as pd


def lambda_handler(event, context):
    data = pd.Series([1,3,5,7,9])

    print(data)
