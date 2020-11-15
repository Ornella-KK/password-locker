class Credential:
    credential_list = [] #empty credential list

    def __init__(self,password):
        self.password = password

    def save_credential(self):
        Credential.credential_list.append(self)
