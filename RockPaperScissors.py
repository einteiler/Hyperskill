import random
with open('rating.txt', 'r+') as file:
    scoreboard = dict(x.split() for x in file.read().split('\n'))
conditions = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
rating = 0
name = input("Enter your name: ")
print(f"Hello, {name}")
if name in scoreboard.keys():
    rating = int(scoreboard[name])
while True:
    user_move = input()
    computer_move = random.choice(["rock", "paper", "scissors"])
    try:
        if conditions.get(user_move) == None:
            raise Exception
        elif conditions.get(user_move) == computer_move:
            print(f"Well done. Computer chose {computer_move} and failed")
            rating += 100
        elif user_move == computer_move:
            print(f"There is a draw ({computer_move})")
            rating += 50
        elif conditions.get(user_move) != computer_move:
            print(f"Sorry, but computer chose {computer_move}")
    except:
        if user_move == "!exit":
            print("Bye!")
            break
        elif user_move == "!rating":
            print(f"Your rating: {rating}")
        else: 
            print("Invalid input")