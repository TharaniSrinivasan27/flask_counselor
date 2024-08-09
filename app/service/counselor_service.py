from app.utils.database_utils import get_dynamodb_table
from botocore.exceptions import ClientError

def create_counsellor_service(data):
    table = get_dynamodb_table()

    counsellor_id = data.get('id')
    name = data.get('name')
    education_history = data.get('education_history')
    experience = data.get('experience')
    about = data.get('about')
    specialization = data.get('specialization')
    mailid = data.get('mailid')

    if not counsellor_id or not name or not mailid:
        return {'error': 'Required fields are missing.'}, 400
    try:
        response = table.put_item(
            Item={
                'id': counsellor_id,
                'name': name,
                'education_history': education_history,
                'experience': experience,
                'about': about,
                'specialization': specialization,
                'mailid': mailid
            }
        )
        return {'message': 'Counsellor created successfully.', 'response': response}, 201
    except ClientError as e:
        print(f"Error inserting item: {e}")
        return {'error': 'Error creating counsellor.'}, 500