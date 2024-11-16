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
        while x != " ":
            y = x.split(",")
            myUser = User(y)
            self.UserList.append(myUser)
        userfile.close()
    def write_user_file(self, filename):
        import csv
        with open(filename) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.UserList)
    def display_user_list(self):
#        print(self.UserName)
#        print(self.Password)
    def find_username(self,username):
        for i in range(len(self.UserList)):
#            index = UserList.index(username)
            if self.UserList[i].UserName == username:
#                return index
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

