

class Credentials:
    """Class that generates new instances of credentials"""
    credentials_list=[]
    def __init__(self,account,username,password):
        """define properties for our objects."""

        """object instantiaton"""
        self.account= account
        self.username = username
        self.password = password
 
        """function to add a new account to the credentials list"""
    def save_credential(self):
        Credentials.credentials_list.append(self)
    
        """function to display all available accounts"""
    
    def display_credential():
        """
        method that returns the credential array
        """
        return Credentials.credentials_list

    def del_account(credential):
        Credentials.credentials_list.remove(credential)
        return credential
    
    def find_account(account):
        for credential in Credentials.credentials_list:
            if credential.account == account:
                
                return credential
       

        

    