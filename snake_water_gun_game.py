import random

computer = random.choice([-1, 0, 1])

youstr = input("enter your choice (s/w/g): ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

if youstr not in youDict:
    print("Invalid input! Choose only s, w, or g.")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

elif (computer == -1 and you == 1) or \
     (computer == 1 and you == 0) or \
     (computer == 0 and you == -1):
    print("🎉 You Win!")

else:
    print("😢 You Lose!")
