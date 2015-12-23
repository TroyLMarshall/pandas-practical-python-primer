from ..DAL.equipment_datastore import EquipmentDatastore
from ..Models.equipment import Equipment

class EquipmentController:

    def __init__(self):
        self.equipment_datastore = EquipmentDatastore()


    def list(self):
        return self.equipment_datastore.equipment()


    def get_item(self, id: int):
        return self.equipment_datastore.get_item(id)


    def add(self, data: dict):
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new equipment item resource.")

        required_elements = Equipment.required_elements
        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create an "
                             "equipment item was not present. The "
                             "following elements must be present to create "
                             "an equipment item: {}".format(required_elements))

        for element in data:
            if element not in required_elements:
                data.pop(element)

        # need a get_item with a name instead of id
        # if self.get_item(data['name']):
        #     raise ValueError("An equipment item already exists with the "
        #                      "`name` specified: {}".format(data['name']))

        item = Equipment(
            name=data['name'],
            complexity=data['complexity'],
            tech_level=data['tech_level'],
            price=data['price'],
            weight=data['weight'],
            value=data['value'])

        try:
            self.equipment_datastore.add(item)
        except ValueError:
            print("value error")
            raise

