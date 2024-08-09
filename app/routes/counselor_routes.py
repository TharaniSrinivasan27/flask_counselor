from flask import request
from app.service.counselor_service import create_counsellor_service

def counselor_init_routes(app):
    @app.route('/create_counsellor', methods=['POST'])
    def create_counsellor():
        data = request.json
        return create_counsellor_service(data)