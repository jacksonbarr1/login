import pickle

class User():
    def __init__(self, name, username, password, hint):
        self.name = name
        self.username = username
        self.password = password
        self.hint = hint
        print(f"Thanks for joining {self.name}!")

    def save_user(self):
        with open('loginData.pickle', 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
    def get_name(self):
        return self.name
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
