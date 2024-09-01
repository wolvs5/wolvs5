#Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.


year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")