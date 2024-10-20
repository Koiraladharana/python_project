import random

print("Welcome,To the Dice Rolling Game!")
choice=input("Do you want to roll the dice.(y/n):")

while choice == 'y':
    roll=random.randint(1,6)
    if roll == 1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")
    elif roll == 2:
        print("-----")
        print("     ")
        print(" 00  ")
        print("     ")
        print("-----")
    elif roll == 3:
        print("-----")
        print("     ")
        print(" 000 ")
        print("     ")
        print("-----")
    elif roll == 4:
        print("-----")
        print("     ")
        print(" 000 ")
        print("  0  ")
        print("-----")
    elif roll == 5:
        print("-----")
        print("     ")
        print(" 000 ")
        print(" 00  ")
        print("-----")
    else:
        print("-----")
        print("     ")
        print(" 000 ")
        print(" 000 ")
        print("-----")
    choice1=input("Do you want to play again!(y/n):")
    if choice1 == 'n':
        break
print("Thank you for playing.")
