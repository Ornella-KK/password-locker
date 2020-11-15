class User:
    user_list=[] 

    def __init__(self,user_name):
        self.user_name = user_name

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    
    def delete_user(self):
        User.user_list.remove(self)