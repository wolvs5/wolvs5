#the program ask the user to enter the username and password again.
#This continues until the login information is correct or
# wrong credentials have been entered five times.
#If the information is correct, the program prints out Welcome.
#After five failed attempts the program prints out Access denied.
#The correct username is python and password rules.
username="python"
password= "rules"
attempts = 0

while attempts<5:
    name=str(input("enter the username"))
    passw=str(input("enter the password"))
    if password==passw and name==username:
        print("welcome user")

        break
    else:
        attempts+=1
        print("please try again again")
if attempts==5:
    print("please try again later")