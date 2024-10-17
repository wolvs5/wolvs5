#Write a program that asks the user to enter names until he/she enters an empty string.
#After each name is read the program either prints out New name
#or Existing name depending on whether the name was entered for the first time.
#Finally, the program lists out the input names one by one, one below another in any order.
#Use the set data structure to store the names.

my_list = set()
while True:
    name = input("Enter a name to add to set or empty string to exit: ")
    if name != "":
        if name in my_list:
            print("Existing name")
        else:
            print("New name")
            my_list.add(name)
    else:
        break
print("Set of name: ")
for item in my_list:
    print(item)