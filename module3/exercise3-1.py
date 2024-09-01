#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake and
# notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

length=int(input("Enter the length of the string: "))

if length>=42:
    print("your string has the fulfilled length")
else:
    ex= 42-length
    print(f"your string has the wrong length and you need {ex} more")