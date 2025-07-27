import random

computer = random.choice([-1, 0, 1])
you = int(input("Enter your choice (-1(water), 0(gun), 1(snake)): "))
youdict = {1: "Snake", 0: "Gun", -1: "Water"}
print(f"Your choice is {youdict[you]}")
print(f"Computer choice is {youdict[computer]}")
if (you == computer):
    print("It is a draw.")
else:
    if (you == 1 and computer == 0):
        print("Computer wins.")
    if (you == 1 and computer == -1):
        print("You win.")
    if (you == -1 and computer == 0):
        print("You win.")
    if (you == -1 and computer == 1):
        print("Computer wins.")
    if (you == 0 and computer == 1):
        print("You wins.")
    if (you == 0 and computer == -1):
        print("Computer wins.")
