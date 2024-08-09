import boto3
from botocore.exceptions import ClientError
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, COUNSELLOR_TABLE_NAME

def get_dynamodb_table():
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    table = dynamodb.Table(COUNSELLOR_TABLE_NAME)
    return table

def create_table_if_not_exists():
    dynamodb = boto3.client(
        'dynamodb',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    
    table_config = {
        'attribute_definitions': [
            {'AttributeName': 'id',
              'AttributeType': 'S'},
        ],
        'key_schema': [
            {'AttributeName': 'id', 
             'KeyType': 'HASH'},
        ],
        'provisioned_throughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    }
    try:
        # Check if the table exists
        response = dynamodb.describe_table(TableName=COUNSELLOR_TABLE_NAME)
        print(f"Table '{COUNSELLOR_TABLE_NAME}' already exists.")
        return response
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            # Table does not exist, create it
            print(f"Table '{COUNSELLOR_TABLE_NAME}' does not exist. Creating table...")
            try:
                response = dynamodb.create_table(
                    TableName=COUNSELLOR_TABLE_NAME,
                    AttributeDefinitions=table_config['attribute_definitions'],
                    KeySchema=table_config['key_schema'],
                    ProvisionedThroughput=table_config['provisioned_throughput']
                )
                print("Table creation initiated.")
                return response
            except ClientError as e:
                print(f"Error creating table: {e}")
                raise
        else:
            # Other errors
            print(f"Unexpected error: {e}")
            raise