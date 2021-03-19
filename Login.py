
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
        print("Log in successful!")
    else:
        # 'Incorrect'. ask if would like hint. if Y, username = inputStr(). load pickle and iterate through objects comparing username/user.username
        print("Incorrect.\n\n")
        startLogin(True)
        
        

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
        print("Not a valid username")
        startLogin(True)

def startLogin(attempted):
    if attempted == False:
        print("Welcome to Jackson's rudimentary login page!")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
    choice = pyip.inputNum("Would you like to:\n\n[1] Log In\n[2] Create an Account\n[3] Forgot Password\n\n", min = 1, max = 3)
    if choice == 1:
        user = pyip.inputStr("Username:\n")
        password = pyip.inputPassword("Password:\n")
        attemptLogin(user, password)
    elif choice == 2:
        create_user()
    else:
        hint_query = pyip.inputYesNo("Would you like a hint? (Y/N)\n\n")
        if hint_query == "yes":
            attempted_user = pyip.inputStr("Input a valid username to access its hint:\n")
            giveHint(attempted_user)
        else:
            startLogin(True)

startLogin(False)
