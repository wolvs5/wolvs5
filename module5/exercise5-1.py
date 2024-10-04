from random import randint

attempts = int(input("How many time you want to roll the dice: "))
sum = 0
i = randint(1,6)
for i in range(1,attempts+1):
  sum += i
print(f"The sum of {attempts} dices is {sum}.")