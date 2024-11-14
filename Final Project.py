class UserList():
    def __init__(self,filename):
        self.UserList = []
        self.FileName = filename

    def read_user_file(self):
        userfile = open(self.FileName)
        x = userfile.readline()