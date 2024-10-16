def list_to_remove_odd_number(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list



print("Create list")
my_list = []
while True:
    number = input("Enter list number or empty string to quit: ")
    if number == "":
        break
    else:
        my_list.append(int(number))

print("Old list:", my_list)
print("New list:", list_to_remove_odd_number(my_list))