import csv
import string

class User():
    def __init__(self, username, password):
        self.UserName = username
        self.Password = password

class UserList():
    def __init__(self,filename):
        self.UserList = []
        self.FileName = filename
    def read_user_file(self, filename):
        userfile = open(filename)
        x = userfile.readline()
        while x != "":
            y = x.split(",")
            myUser = User(y[0], y[1])
            self.UserList.append(myUser)
            x = userfile.readline()
        userfile.close()
    def write_user_file(self, filename):
        add = csv.writer(open(filename,"w"))
        add.writerows(self.UserList)
    def display_user_list(self):
        print("{:>10s} {:>10s}".format("Username", "Password"))
        print("{:>10s} {:>10s}".format(10 * "-",10 * "-"))
        for i in range(len(self.UserList)):
            print("{:<10s} {:>10s}".format(self.UserList[i].UserName, self.UserList[i].Password))
    def find_username(self,username):
        for i in range(len(self.UserList)):
            if self.UserList[i].UserName == username:
               return i
        return -1
    def change_password(self, username, password):
        index = self.find_username(username)
        self.UserList[index].Password += password
        return self.UserList[index].Password
    def add_user(self, username, password):
        index = self.find_username(username)
        if not index:
            myUser = User(username, password)
            self.UserList.append(myUser)
    def delete_user(self, username):
        index = self.find_username(username)
        del self.UserList[index]
    def strength(self, password):
        points = 0
        if len(password) >= 8:
            points += 1
        if any(char.isupper() for char in password) == "True":
            points += 1
        if any(char.islower() for char in password) == "True":
            points += 1
        if any(char.isdigit() for char in password) == "True":
            points += 1
        if any(char in string.punctuation for char in password) == "True":
            points += 1
        return points


myUserList = UserList("Final Project Passwords.txt")
myUserList.read_user_file("Final Project Passwords.txt")

def menu():
    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on an Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")


menu()
choice = int(input("Enter Selection: "))

while choice != 0:
    if choice == 1:
        name = input("Enter a Username: ")
        if myUserList.find_username(name) != -1:
            print("Username Already Exists.")
        else:
            pas = input("Enter a Password: ")
            if myUserList.strength(pas) >= 5:
                myUserList.add_user(name, pas)
                print("User Added.")
            else:
                while myUserList.strength(pas) < 5:
                    pas = input("Enter a Password: ")
    if choice == 2:
        name = input("Enter a Username: ")
        if myUserList.find_username(name) == -1:
            print("Username Not Found.")
        else:
            myUserList.delete_user(name)
            print("User Deleted.")
    if choice == 3:
        name = input("Enter a Username: ")
        if myUserList.find_username(name) == -1:
            print("Username Not Found.")
        else:
            pas = input("Enter a Password: ")
            if myUserList.strength(pas) >= 5:
                myUserList.change_password(pas)
                print("Password changed.")
            else:
                pas = input("Enter a Password: ")
    if choice == 4:
        myUserList.display_user_list()
    if choice == 5:
        myUserList.write_user_file("Final Project Passwords.txt")
        print("Changes Saved.")
    if choice == 6:
        break
    if choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 6:
        print("Invalid Selection.")

    print()
    menu()
    choice = int(input("Enter Selection: "))