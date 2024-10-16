def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print("list is created")
my_list = []
while True:
    num = input("Enter list number or empty string to exit: ")
    if num == "":
        break
    else:
        my_list.append(int(num))

print("The sum of your list is",sum_of_list(my_list))