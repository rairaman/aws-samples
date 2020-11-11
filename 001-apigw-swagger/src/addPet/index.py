import json
import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    pet_name = json.loads(event['body'])['name']
    pet_id = random.randint(1,101)

    new_pet = { 'id': pet_id, 'name': pet_name }
    pets = [new_pet]

    response = {
        'headers': {
            'Content-Type':'application/json'
        },
        'statusCode': 200,
        'body': json.dumps(pets)            
    }

    return response