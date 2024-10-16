import random

def random_dice_roll(max_value):
    return random.randint(1, max_value)


max_value = int(input("Enter the maximum value of your dice: "))
while True:
    print("Rolling dice ...")
    result = random_dice_roll(max_value)
    if result == max_value:
        print("Result is ",result, "End program!")
        break
    else:
        print("Result is", result, ". Reroll until", max_value)