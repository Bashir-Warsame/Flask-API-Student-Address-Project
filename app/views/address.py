from flask import Blueprint, request, jsonify
from app.database import db
from app.models.address import Address

address_bp = Blueprint('address', __name__)


# Endpoint to create a new address
@address_bp.route('/api/address', methods=['POST'])
def create_address():
    data = request.get_json()
    new_address = Address(
        id=data['id'],
        student_id=data['student_id'],
        number=data['number'],
        house_name=data['house_name'],
        road=data['road'],
        city=data['city'],
        state=data['state'],
        country=data['country'],
        zipcode=data['zipcode']
    )
    db.session.add(new_address)
    db.session.commit()
    return jsonify({'message': 'Address created successfully'}), 201


# Endpoint to get all addresses
@address_bp.route('/api/address', methods=['GET'])
def get_addresses():
    addresses = Address.query.all()
    result = []
    for address in addresses:
        result.append({
            'id': address.id,
            'student_id': address.student_id,
            'number': address.number,
            'house_name': address.house_name,
            'road': address.road,
            'city': address.city,
            'state': address.state,
            'country': address.country,
            'zipcode': address.zipcode
        })
    return jsonify(result)


# Endpoint to get an address by ID
@address_bp.route('/api/address/<int:address_id>', methods=['GET'])
def get_address(address_id):
    address = Address.query.get(address_id)
    if address:
        return jsonify({
            'id': address.id,
            'student_id': address.student_id,
            'number': address.number,
            'house_name': address.house_name,
            'road': address.road,
            'city': address.city,
            'state': address.state,
            'country': address.country,
            'zipcode': address.zipcode
        })
    else:
        return jsonify({'message': 'Address not found'}), 404


# Endpoint to update an address
@address_bp.route('/api/address/<int:address_id>', methods=['PATCH'])
def update_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    data = request.get_json()
    if 'id' in data:
        address.id = data['id']
    if 'number' in data:
        address.number = data['number']
    if 'house_name' in data:
        address.house_name = data['house_name']
    if 'road' in data:
        address.road = data['road']
    if 'city' in data:
        address.city = data['city']
    if 'state' in data:
        address.state = data['state']
    if 'country' in data:
        address.country = data['country']
    if 'zipcode' in data:
        address.zipcode = data['zipcode']

    db.session.commit()
    return jsonify({'message': 'Address updated successfully'})


# Endpoint to delete an address
@address_bp.route('/api/address/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    # Assuming you have a function to delete the address
    db.session.delete(address)
    db.session.commit()

    return jsonify({'message': 'Address deleted successfully'})


