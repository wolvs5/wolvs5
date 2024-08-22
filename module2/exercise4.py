#Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
sum=num1+num2+num3
product=num1*num2*num3
average=(sum/3)
print("The product of ",num1,"and",num2,"and",num3,"is",product)
print("The average is",average)
print("the sum is",sum)