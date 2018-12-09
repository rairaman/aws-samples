import crhelper
import boto3

# initialise logger
logger = crhelper.log_config({"RequestId": "CONTAINER_INIT"})
logger.info('Logging configured')
# set global to track init failures
init_failed = False

try:
    # Place initialization code here
    logger.info("Container initialization completed")
except Exception as e:
    logger.error(e, exc_info=True)
    init_failed = e


def create(event, context):
    """
    Updates the Firehose Destination configuration to enable Data Conversion
    """
    firehose_client = get_firehose_client()

    delivery_stream_name = event['ResourceProperties']['FirehoseDeliveryStreamName']
    glue_interaction_role_arn = event['ResourceProperties']['GlueInteractionRole']
    database_name = event['ResourceProperties']['InputGlueDatabaseName']
    table_name = event['ResourceProperties']['InputGlueTable']
    
    firehose_details = firehose_client.describe_delivery_stream(DeliveryStreamName=delivery_stream_name)

    version_id = firehose_details['DeliveryStreamDescription']['VersionId']
    dest_id = firehose_details['DeliveryStreamDescription']['Destinations'][0]['DestinationId']
    
    response = firehose_client.update_destination(
    DeliveryStreamName=delivery_stream_name,
    CurrentDeliveryStreamVersionId=version_id,
    DestinationId=dest_id,
    ExtendedS3DestinationUpdate={
        'BufferingHints': {
            'SizeInMBs': 64,
            'IntervalInSeconds': 60
        },
        'DataFormatConversionConfiguration': {
            'SchemaConfiguration': {
                'RoleARN': glue_interaction_role_arn,
                'DatabaseName': database_name,
                'TableName': table_name
            },
            'InputFormatConfiguration': {
                'Deserializer': {
                    'OpenXJsonSerDe': {
                        'CaseInsensitive': True
                    }
                }
            },
            'OutputFormatConfiguration': {
                'Serializer': {
                    'ParquetSerDe': {
                        'EnableDictionaryCompression': False
                    }
                }
            },
            'Enabled': True
        }
    })

    physical_resource_id = 'FirehoseRecordConvertor'
    response_data = {}
    return physical_resource_id, response_data


def update(event, context):
    """
    Place your code to handle Update events here
    
    To return a failure to CloudFormation simply raise an exception, the exception message will be sent to CloudFormation Events.
    """
    physical_resource_id = event['PhysicalResourceId']
    response_data = {}
    return physical_resource_id, response_data


def delete(event, context):
    """
    Disables Data Conversion on the Firehose delivery stream
    """
    firehose_client = get_firehose_client()

    delivery_stream_name = event['ResourceProperties']['FirehoseDeliveryStreamName']
    firehose_details = firehose_client.describe_delivery_stream(DeliveryStreamName=delivery_stream_name)

    version_id = firehose_details['DeliveryStreamDescription']['VersionId']
    dest_id = firehose_details['DeliveryStreamDescription']['Destinations'][0]['DestinationId']
    
    response = firehose_client.update_destination(
        DeliveryStreamName=delivery_stream_name,
        CurrentDeliveryStreamVersionId=version_id,
        DestinationId=dest_id,
        ExtendedS3DestinationUpdate={
            'DataFormatConversionConfiguration': {
                'Enabled': False
            }
    })

    return


def lambda_handler(event, context):
    """
    Main handler function, passes off it's work to crhelper's cfn_handler
    """
    # update the logger with event info
    global logger
    logger = crhelper.log_config(event)
    return crhelper.cfn_handler(event, context, create, update, delete, logger,
                                init_failed)

def get_firehose_client():
    return boto3.client('firehose')