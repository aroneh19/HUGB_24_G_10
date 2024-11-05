
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
    
    def unmatch(self, user1, user2):
        """
        Removes a match between two users.

        Parameters:
            user1 (str): The username of the first user.
            user2 (str): The username of the second user.
        """
        # Load existing matches from the database
        matches = self.database.load_data(self.database.matches_file)

        # Remove the match between user1 and user2
        matches = [match for match in matches if not (
            (match["user1"] == user1 and match["user2"] == user2) or
            (match["user1"] == user2 and match["user2"] == user1)
        )]

        # Save the updated matches back to the file
        self.database.save_data(self.database.matches_file, matches)
