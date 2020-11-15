class Credential:
    credential_list = [] #empty credential list

    def __init__(self,password):
        self.password = password

    def save_credential(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def credential_exist(cls,password):
        for credential in cls.credential_list:
            if credential.password == password:
                return True
            else:
                return False
    
    @classmethod
    def display_credential(cls):
        return cls.credential_list
