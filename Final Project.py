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
        import csv
        with open(filename) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.UserList)
    def display_user_list(self):
        print("{:>10s} {:>10s}".format("Username", "Password"))
        print("{:>10s} {:>10s}".format(10 * "-",10 * "-"))
        for i in range(len(self.UserList)):
            print("{:>10s} {:>10s}".format(self.UserList[i].UserName, self.UserList[i].Password))
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
        index = self.find_user(username)
        del self.UserList[index]

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
        found = myUserList.find_username(name)
        if name == found :
            print("Username Already Exists.")
        else:
            input("Enter a Password: ")
#           test password strength
            myUserList.add_user()
            print("User Added.")
    if choice == 2:
        name = print("Enter a Username: ")
        found = myUserList.find_username(name)
        if name != found:
            print("Username Not Found.")
        else:
            myUserList.delete_user(name)
            print("User Deleted.")
    if choice == 3:
        name = print("Enter a Username: ")
        found = myUserList.find_username(name)
        if name != found:
            print("Username Not Found.")
        else:
            password = print("Enter a Password: ")
#           test password strength
            myUserList.change_password(password)
            print("Password Changed")
    if choice == 4:
        myUserList.display_user_list()
    if choice == 5:
        myUserList.write_user_file()
        print("Changes Saved.")
    if choice == 6:
        break
    if choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 6:
        print("Invalid Selection.")

    print()
    menu()
    choice = int(input("Enter Selection: "))