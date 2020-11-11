import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    pet1 = { 'id': 1, 'name': "Fluffy the cat"}
    pet2 = { 'id': 2, 'name': "Bingo the dog"}
    pets = [pet1,pet2]

    response = {
        'headers': {
            'Content-Type':'application/json'
        },
        'statusCode': 200,
        'body': json.dumps(pets)            
    }

    return response