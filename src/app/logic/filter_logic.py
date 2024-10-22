from app.models.database import Database

class FilterLogic:
    def __init__(self):
        self.db = Database()

    def apply_filters(self, filters):
        """
        Apply filters to the loaded user data.

        Parameters:
        filters (dict): A dictionary containing the filters to be applied. 
        The filters include interests, age and location.

        Returns:
        list: A list of users that satisfy the filters.
        """
        users = self.db.load_users()
        filtered_users = users

        # Interest filter
        if filters.get("interests"):
            filtered_users = [user for user in filtered_users if any(interest in user['interests'] for interest in filters['interests'])]

        # Age filter
        if filters.get("age"):
            age_range = filters['age']
            filtered_users = [user for user in filtered_users if age_range[0] <= user['age'] <= age_range[1]]

        # Location filter
        if filters.get("location"):
            filtered_users = [user for user in filtered_users if user['location'] == filters['location']]

        return filtered_users
