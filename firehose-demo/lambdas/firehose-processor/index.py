import base64
import json
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

output = []

def lambda_handler(event, context):

    for record in event['records']:

        try:
            #Input data is base64 encode, need to decode it
            decodedData = base64.b64decode(record['data'].encode('utf-8'))
            originalData = json.loads(decodedData.decode('utf-8'))

            #Enrich data
            enrichedOutput = {
                'First_Name': originalData['First_Name'],
                'Last_Name': originalData['Last_Name']
            }

            #Prepare Output
            outputData = base64.b64encode(json.dumps(enrichedOutput).encode('utf-8')).decode('utf-8')

            #Object back to firehose
            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': outputData
            }

            logger.info("Success")
        except Exception as e:
            logger.error('Exception: ' + str(e))
            #Processingfailed
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            }

        output.append(output_record)

    return {'records': output}