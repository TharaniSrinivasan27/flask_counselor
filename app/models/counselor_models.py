from config import COUNSELLOR_TABLE_NAME
from app.utils.databaseutils import create_table_if_not_exists

# Define table parameters
counsellor_table_params = {
    'table_name': COUNSELLOR_TABLE_NAME,

    'attribute_definitions': [
        {'AttributeName': 'id',
          'AttributeType': 'S'},
    ],

    'key_schema': [
        {'AttributeName': 'id',
          'KeyType': 'HASH'},
    ],
}

# Call the function to ensure the table is created
create_table_if_not_exists(counsellor_table_params)