from math import sqrt
number = int(input("what number do you want to prime check? "))
sqr_num = int(sqrt(number))
if number == 1:
    print("not prime")
else:
    for i in range(2,sqr_num+1):
        if number % i == 0:
            print(number,"is not prime!")
            break
        elif i == sqr_num:
            print(number, "is prime")