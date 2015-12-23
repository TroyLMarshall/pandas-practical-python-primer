import jsonpickle
from flask import Flask, jsonify, make_response, Response, request
from werkzeug.exceptions import BadRequest

from gamma_world_api.Controllers.equipment_controller import EquipmentController

app = Flask(__name__)

#equipment_controller = EquipmentController()


@app.route('/api/v1/equipment', methods=["GET"])
def get_equipment() -> Response:
    """
    Returns a representation of the collection of Equipment resources.

    Returns:
        A flask.Response object.
    """
    equipment_controller = EquipmentController()
    equipment_list = equipment_controller.list()
    return jsonpickle.encode(equipment_list)


@app.route('/api/v1/equipment/<id>', methods=["GET"])
def get_item(id: int) -> Response:
    equipment_controller = EquipmentController()
    try:
        item = equipment_controller.get_item(id)
        return jsonpickle.encode(item)
    except ValueError as error:
        error_response = make_response(
            jsonify({"Item Not Found": str(error)}), 404)
        return error_response


@app.route('/api/v1/equipment', methods=["POST"])
def add_equipment() -> Response:
    try:
        request_payload = request.get_json()
    except BadRequest as error:
        response = make_response(
            jsonify({"error": "JSON payload contains syntax errors. "
                              "Please fix and try again."}), 400)
        return response

    try:
        equipment_controller = EquipmentController()
        equipment_controller.add(request_payload)
    except ValueError as error:
        error_response = make_response(jsonify(
            {"error": str(error)}), 400)
    except Exception as base_error:
        error_response = make_response(jsonify(
            {"error": str(base_error)}), 400)

    response = make_response(
        jsonify({"message": "Equipment item created."}), 201)
    return response

