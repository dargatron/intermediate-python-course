import random
def main():
    dice_rolls = 2
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,12)
        dice_sum += roll
        print(f'\n\tYou rolled a: {roll}\n')
    print(f'\n\tYou have rolled a total of: {dice_sum}', '@' * dice_sum)

if __name__== "__main__":
  main()
