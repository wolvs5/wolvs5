import random


def random_dice_roll():
    return random.randint(1,6)

while True:
    print("Rolling dice ...")
    result = random_dice_roll() #4 => result =4
    if result == 6:
        print("Result is ",result, "End program!")
        break
    else:
        print("Result is", result, ". Reroll until 6")