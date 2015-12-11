from ..DAL import equipment_datastore

class EquipmentController:

    def __init__(self):
        self.equipment_list = equipment_datastore.load()

    def list(self):
        return self.equipment_list

    def add(self):
        self.equipment_list.append()
        equipment_datastore.save(self.equipment_list)
