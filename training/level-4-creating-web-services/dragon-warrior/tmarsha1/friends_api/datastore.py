"""
some doc string
"""

import sqlite3

class Datastore:
    """
    Provides an interface to the SQLite database.
    """

    def __init__(self):
        self.connection = sqlite3.connect('/tmp/friends.db')


    def friends(self) -> list:
        """
        Return the current list of friends.

        Returns:
            Fill this in.
        """
        cursor = self.connection.execute(
            'SELECT id, firstName, lastName, telephone, email, notes '
            'FROM friends')

        friends = []
        for row in cursor.fetchall():
            friends.append(
                {"id": row[0],
                 "firstName": row[1],
                 "lastName": row[2],
                 "telephone": row[3],
                 "email": row[4],
                 "notes": row[5]})
        return friends


    def friend(self, id: str) -> dict:
        """
        Return a specific friend resource.

        Args:
            id: The unique identifier of a specific friend.

        Returns:
            A dict of the specific friend.
        """
        cursor = self.connection.execute(
            'SELECT id, firstName, lastName, telephone, email, notes '
            'FROM friends '
            'WHERE lower(id) = ?', [id.lower()])

        friend_row = cursor.fetchone()

        if friend_row:
            return {"id": friend_row[0],
                 "firstName": friend_row[1],
                 "lastName": friend_row[2],
                 "telephone": friend_row[3],
                 "email": friend_row[4],
                 "notes": friend_row[5]}

        raise ValueError("No existing friend was found matching id: {}".format(id))


    def create_friend(self, data: dict):
        """
        Create a new friend entry is our datastore of friends.

        Args:
            data: A dictionary of data for our new friend.  Must have
                the following elements: ['id', 'firstName', 'lastName',
                'telephone', 'email', 'notes']

        Raises:
            ValueError: If data is None, doesn't contain all required
                elements, or a duplicate id already exists in `friends`.
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new friend resource.")

        required_elements = {}
        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))

        for element in data:
            if element not in required_elements:
                data.pop(element)

        try:
            if self.friend(data['id']):
                raise ValueError("A friend already exists with the "
                                 "`id` specified: {}".format(data['id']))
        except ValueError:
            self.connection.execute(
                'INSERT into friends(id, firstName, lastName, telephone, email, notes) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                    [data['id'],
                     data['firstName'],
                     data['lastName'],
                     data['telephone'],
                     data['email'],
                     data['notes']
                     ])

            self.connection.commit()

    def update_friend(self, id: str, data: dict):
        """
        Update an existing friend entry is our datastore of friends.

        Args:
            data: A dictionary of data to update an existing friend entry with.

        Raises:
            ValueError: If data is None or if no matching friend entry is found.
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to update an existing friend resource.")

        #TODO: Remove extraneous data elements.

        try:
            matched_friend = self.friend(id)
        except ValueError:
            raise
        else:
            self.connection.execute(
                'UPDATE friends '
                'SET id=?, firstName=?, lastName=? '
                'WHERE lower(id) = ?',
                    [data['id'],
                     data['firstName'],
                     data['lastName'],
                     data['telephone'],
                     data['email'],
                     data['notes'],
                     data['id']
                     ])

        self.connection.commit()

    def destroy_friend(self, id: str):
        """
        Destroy a friend entry in our datastore of friends.

        Args:
            id:

        Returns:

        """
        # try:
        #     matched_friend = friend(id)

        try:
            matched_friend = self.friend(id)
        except ValueError:
            raise
        else:
            self.connection.execute(
                'DELETE '
                'FROM friends '
                'WHERE lower(id) = ?',
                [id.lower()])

            self.connection.commit()