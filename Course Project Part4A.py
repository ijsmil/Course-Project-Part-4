# Ifetayo Sands
# CIS 261
# Course Project Part4A
def GetUserName():
    username = input("Enter user name: ")
    return username
def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd
def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
def printinfo():
    UserFile = open("Users.txt", "r")
    while True:
       UserDetail = UserFile.readline()
       if not UserDetail:
           break
       UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
       UserList = UserDetail.split("|")
       username = UserList[0]
       userpassword = UserList[1]
       userrole = UserList[2]
       print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
if __name__ == "__main__":
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole =GetUserRole()
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
    # close file to save data
    UserFile.close()
    printinfo()