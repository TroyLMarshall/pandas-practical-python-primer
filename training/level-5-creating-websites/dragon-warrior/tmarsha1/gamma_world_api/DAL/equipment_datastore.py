import sqlite3

from ..Models.equipment import Equipment

class EquipmentDatastore:
    def __init__(self):
        self.connection = sqlite3.connect('/tmp/gammaworld.db')
        self.connection.row_factory = sqlite3.Row
        self.connection.execute('PRAGMA FOREIGN_KEYS = ON;')


    def equipment(self) -> list:
        equipment_list = []

        results = self.connection.execute(
            'SELECT name, complexity, tech_level, price, weight, value '
            'FROM equipment_view')


        for row in results.fetchall():
            item = Equipment(
                name=row['name'],
                complexity=row['complexity'],
                tech_level=row['tech_level'],
                price=row['price'],
                weight=row['weight'],
                value=row['value']
            )
            equipment_list.append(item)

        return equipment_list


    def get_item(self, id: int):
        results = self.connection.execute(
            'SELECT name, complexity, tech_level, price, weight, value '
            'FROM equipment_view '
            'WHERE id = ?', [id])

        item_row = results.fetchone()

        if item_row:
            return Equipment(
                name=item_row['name'],
                complexity=item_row['complexity'],
                tech_level=item_row['tech_level'],
                price=item_row['price'],
                weight=item_row['weight'],
                value=item_row['value'])

        raise ValueError(
            "No existing item was found matching id: {}".format(id))


    def add(self, item: Equipment):
        try:
            self.connection.execute(
                'INSERT INTO equipment( '
                '  name, '
                '  complexity, '
                '  tech_level_fk, '
                '  price, '
                '  weight, '
                '  value) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                    [item.name,
                     item.complexity,
                     item.tech_level,
                     item.price,
                     item.weight,
                     item.value])

            self.connection.commit()
        except Exception as error:
            if (str(error).lower() == 'foreign key constraint failed'):
                raise ValueError(
                    "Invalid tech level {}".format(item.tech_level))
            else:
                raise
