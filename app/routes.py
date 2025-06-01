from flask import Blueprint, request, jsonify
from .models import db, License

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "License server is running!"

@main.route('/check_license', methods=['POST'])
def check_license():
    data = request.json
    license_key = data.get('license_key')
    device_name = data.get('device_name')

    license = License.query.filter_by(license_key=license_key, device_name=device_name).first()
    if license and license.is_active:
        return jsonify({'status': 'valid'})
    return jsonify({'status': 'invalid'}), 403
