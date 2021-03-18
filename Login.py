# User/Pass CSV to be loaded in for access upon login
# Can login (search csv for user) and create account (Creates a User)
from User import User
import pyinputplus as pyip
import pickle

class Login():
    def __init__(self, user, password):
        self.attempted_user = user
        self.attempted_pass = password
        self.valid = False

        users = []
        with open('loginData.pickle', 'rb') as input:
            while 1:
                try:
                    users.append(pickle.load(input))
                except EOFError:
                    break
        for user in users:
            if user.username == self.attempted_user and user.password == self.attempted_pass:
                self.valid = True
                logged_in = user

        
        # Compare user/pass to saved directory
        # then define Bool self.valid
        # If valid, self.User 

def create_user():
    name = pyip.inputStr("Input your name:\n")
    username = pyip.inputStr("Input your desired username:\n")
    password = pyip.inputPassword("Input your desired password:\n")
    if pyip.inputYesNo("Would you like to add a hint? (Y/N)\n") == "yes":
        hint = pyip.inputStr("Enter your desired hint:\n")
    else:
        hint = "You didn't set a hint!"
    user = User(name, username, password, hint)
    user.save_user()


def attemptLogin(user, password):
    login = Login(user, password)
    if login.valid:
        print("Log in sucessful!")
    else:
        # 'Incorrect'. ask if would like hint. if Y, username = inputStr(). load pickle and iterate through objects comparing username/user.username
        hint_query = pyip.inputYesNo("Incorrect. Would you like a hint? (Y/N)\n")
        if hint_query == "yes":
            attempted_user = pyip.inputStr("Input a valid username to access its hint:\n")
            giveHint(attempted_user)
        else:
            quit()

def giveHint(attempted_user):
    users = []
    valid_user = False
    with open('loginData.pickle', 'rb') as input:
         while 1:
            try:
                users.append(pickle.load(input))
            except EOFError:
                break
    for user in users:
        if attempted_user == user.username:
            valid_user = True
            print(f"Your hint is: {user.hint}")
    if valid_user == False:
        print("Not a valid username. Try logging in again.")


print("Welcome to Jackson's rudimentary login page!")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
choice = pyip.inputNum("Would you like to:\n\n[1] Log In\n[2] Create an Account\n\n", min = 1, max = 2)
if choice == 1:
    user = pyip.inputStr("Username:\n")
    password = pyip.inputPassword("Password:\n")
    attemptLogin(user, password)
else:
    create_user()
