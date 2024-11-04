
class MatchesLogic:
    """
    Logic for handling user matches.
    """

    def __init__(self, database):
        """
        Initializes MatchesLogic with an instance of Database.

        Args:
            database (Database): Instance of the Database class.
        """
        self.database = database

    def get_matches(self, username):
        """
        Retrieves a list of matches for a given user.

        Args:
            username (str): The username of the current user.

        Returns:
            list: A list of matched usernames.
        """
        matches_data = self.database.load_data(self.database.matches_file)
        user_matches = []
        for match in matches_data:
            if match['user1'] == username:
                user_matches.append(match['user2'])
            elif match['user2'] == username:
                user_matches.append(match['user1'])
        return user_matches
