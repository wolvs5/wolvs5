#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä),
# pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and


#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.
talent=float(input("Enter your Talent: "))
pounds=float(input("Enter your Pounds: "))
lot=float(input("Enter your Lot: "))
kg= (talent*20*32*13.3 + pounds*32*13.3 + lot*13.3)
kg1=kg//1000
gram=kg%1000
print(f"The weight in modern units:\n{kg1} kilograms and {gram:.2f} grams")