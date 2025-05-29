from flask import Blueprint, jsonify

employee_bp = Blueprint('employee', __name__)

# Example hardcoded employee data
EMPLOYEES = [
    {"id": 1, "name": "Alice", "role": "Manager"},
    {"id": 2, "name": "Bob", "role": "Chef"},
    {"id": 3, "name": "Charlie", "role": "Waiter"}
]

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees": EMPLOYEES})
