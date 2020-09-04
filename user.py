class User:
    """Class that generates new instances of users"""
    user_list=[]
    def __init__(self,username,password):
        """define properties for our objects."""

        self.username = username
        self.password = password


    def save_login(self):
        """
        save login method to save new user to user list
        """
        User.user_list.append(self)

    def confirm(username,password):
        ifexists=''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                    ifexists = user.username
        return ifexists


    