#Write a program that converts inches to centimeters until the user inputs a negative value.
#Then the program ends.
inches = int(input("Enter the number of inches: "))
while inches < 0:
      print("it cannot be less than zero")
      inches = int(input("Enter the number of inches: "))

print(f"{inches} inches is {inches *2.54}centimeters")