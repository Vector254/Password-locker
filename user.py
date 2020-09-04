class User:
    """Class that generates new instances of users"""
    user_list=[]
    def __init__(self,username,password):
        """define properties for our objects."""

        self.username = username
        self.password = password

    def save_login(self):
        """
        save_contact method to save new user to user list
        """
        User.user_list.append(self)
