# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
# Initialize empty lists to store the numbers
i=1
while True:
    number_string = input("Enter a number: ")
    if i == 1:
        if number_string != "":
            number_float = float(number_string)
            largest_number = smallest_number = number_float
            i = 2
        else:
            print("No number entered")
            break
    elif i == 2:
        if number_string == "": #next state exit
            print("largest number", largest_number)
            print("smallest number", smallest_number)
            break
        else:   #next state
            number_float = float(number_string)
            if number_float > largest_number:
                largest_number = number_float
            if number_float < smallest_number:
                smallest_number = number_float