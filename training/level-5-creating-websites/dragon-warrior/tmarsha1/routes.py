import jsonpickle
from flask import Flask, jsonify

from gamma_world_api.Controllers import equipment_controller

app = Flask(__name__)

equipment_control = equipment_controller.EquipmentController()


@app.route('/api/v1/equipment', methods=["GET"])
def get_equipment():
    """
    Returns a representation of the collection of Equipment resources.

    Returns:
        A flask.Response object.
    """
    equipment_list = equipment_control.list()
    return jsonpickle.encode(equipment_list)
#    equipment_control.test()

@app.route('/api/v1/equipment', methods=["POST"])
def add_equipment():
    pass