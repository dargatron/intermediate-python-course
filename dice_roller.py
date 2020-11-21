import random
def main():
    dice_rolls = int(input('\n\tHow many dice ya wanna throw? '))
    dice_size = int(input('\n\tHow many sides do those dice have? '))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'\n\tYou rolled a: {roll}...The lonliest number')
        elif roll == dice_size:
            print(f'\n\tYou rolled a: {roll} MAXIMUM ROLL!!!')
        else:
            print(f'\n\tYou rolled a: {roll}')
        print(f'\n\tYou rolled a: {roll}\n')
    print(f'\n\tYou have rolled a total of: {dice_sum}', '#&@' * dice_sum)

if __name__== "__main__":
  main()
