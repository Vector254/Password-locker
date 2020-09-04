

class Credentials:
    """Class that generates new instances of credentials"""
    credentials_list=[]
    def __init__(self,account,username,password):
        """define properties for our objects."""

        self.account= account
        self.username = username
        self.password = password
 
    def save_credential():
        Credentials.credentials_list.append(self)

    
    def display_credential():
        """
        method that returns the credential array
        """
        return Credentials.credentials_list

    