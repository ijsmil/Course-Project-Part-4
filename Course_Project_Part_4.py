# Ifetayo Sands
# CIS 261
# Course Project Part 4
from datetime import datetime
def Login():
       # read login information and store in a list
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter User Name ")
    UserRole =  "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName
        UserDetail = UserDetail.replace("\n", "") # remove carriage return from end of line
        UserList = UserDetail.split("|")
        if UserName == UserList[0]:
            UserRole = UserList[2] # user is valid, return role
            return UserRole, UserName
        return UserRole, UserName
   
    EmpFile = open("Users.txt", "r")
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
        EmpList = EmpDetail.split("|")
        startdate = EmpList[0]
        enddate = EmpList[1]
        name = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay, = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(startdate, enddate, name, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotalEmployees += 1
        TotalHours += hours
        TotalGrossPay += grosspay
        TotalTax += incometax
        TotalNetPay += netpay
        EmpTotals["TotalEmployees"] = TotalEmployees
        EmpTotals["TotalHours"] = TotalHours
        EmpTotals["TotalGrossPay"] = TotalGrossPay
        EmpTotals["TotalTax"] = TotalTax
        EmpTotals["TotalNetPay"] = TotalNetPay
        DetailsPrinted = True
    if (DetailsPrinted): # skip of no detail lines printed
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
if __name__ == "__main__":
    UserRole, UserName = Login()
    DetailsPrinted = False
    EmpTotals = {}
    if (UserRole.upper() == "NONE"): # user not found in user file
        print(UserName, " is invalid. ")
    else:
    # only admin users can enter data
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                name = GetName()
                if (name.upper() == "END"):
                        break
                startdate, enddate = GetDatesWorked()
                hours = GetTotalHours()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = startdate + "|" + enddate + "|" + name + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
                EmpFile.write(EmpDetail)
        # close file to save data
            EmpFile.close()
        printinfo(DetailsPrinted)

