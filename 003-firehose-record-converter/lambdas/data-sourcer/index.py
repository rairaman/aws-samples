import base64
import json
import logging
import time
import urllib.request as requests
import os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

output = []

source_api_endpoint = 'https://data.melbourne.vic.gov.au/resource/d6mv-s43h.json'
firehose_client = boto3.client('firehose')

def get_pedestrian_data(count):

    try:
        #Get the data from the API
        request_obj = requests.Request(source_api_endpoint)
        raw_response = requests.urlopen(request_obj).read()
        pesdestrian_counts = json.loads(raw_response.decode('utf-8'))
    except:
        #Handle exception with a retry. Fail on second retry (failure is just a cloudwatch error)
        if count == 0:
            logger.warning('Failed to retrieve pedestrian data. Retrying in 3 seconds...')
            time.sleep(3)
            get_pedestrian_data(1)
        else:
            logger.error('Failed to retrieve pedestrian data. Not retrying.')

    return pesdestrian_counts

def chunk_up_sensor_counts(sensor_counts, chunk_size):
    number_of_sensor_counts = len(sensor_counts)
    chunks = []

    if number_of_sensor_counts > chunk_size:
        chunk_start = 0
        chunk_end = chunk_size

        while number_of_sensor_counts >= chunk_size:
            
            logger.debug('Getting records %d to %d',chunk_start, chunk_end)
            chunks.append(sensor_counts[chunk_start:chunk_end])

            chunk_start += chunk_size
            chunk_end += chunk_size
            number_of_sensor_counts -= chunk_size
    else:
        chunks.append(sensor_counts)

    return chunks

def send_to_firehose(chunks, firehose_name):

    for chunk in chunks:
        chunk_records = []

        for record in chunk:
            delimited_record = json.dumps(record) + '\n'
            chunk_records.append({'Data': delimited_record.encode('utf-8')})
            
        firehose_response = firehose_client.put_record_batch(
            DeliveryStreamName=firehose_name,
            Records=chunk_records
        )

        logger.info(firehose_response)

def lambda_handler(event, context):

    firehose_name = os.environ['FirehoseName']

    # Call API to get data
    logger.debug('Calling the %s endpoint',source_api_endpoint)
    sensor_counts = get_pedestrian_data(0)

    #Chunk up the sensor counts into batches of 500 records
    chunks = chunk_up_sensor_counts(sensor_counts, 500)

    #Send each batch to firehose
    send_to_firehose(chunks, firehose_name)

    return