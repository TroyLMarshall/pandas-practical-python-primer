import pickle
from ..Models import equipment

def load():
    equipment_list = []
    try:
        data_file = open(__filename(), 'rb')
        equipment_list = pickle.load(data_file)
    except FileNotFoundError:
        pass
    return equipment_list

    # equipment_list = []
    # item1 = equipment.Equipment("Accelra Dose", "E", 2, 100, .1, 100)
    # item2 = equipment.Equipment("Adhesive Paste", "A", 2, 2, .2, 50)
    # equipment_list.append(item1)
    # equipment_list.append(item2)
    # return equipment_list


def save(equipment_list):
    data_file = open(__filename(), 'wb')
    pickle.dump(equipment_list, data_file, pickle.HIGHEST_PROTOCOL)


def __filename():
    filename = "gamma_world_api/DAL/" + __name__ + ".dat"
    return filename