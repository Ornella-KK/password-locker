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

    @classmethod
    def user_exist(cls,user_name):
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
            else:
                return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
        