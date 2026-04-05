'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.
'''

'''
snake beats water
water beats gun
gun beats snake 
so acc to user choice - computer choice
snake - water = 1 (User wins)
water - gun = 1 (User wins)
gun - snake = -2 (User wins)
water - snake = -1 (User Loses)
gun - water = -1 (User Loses)
snake - gun = 2 (User Loses)
this is possible if snake = 1 water = 0 and gun = -1
'''

# if you wish to understand this then paste this in GPT and understand it. 
#this particular result was the final iteration after multiple hours of toiling with this problem 

import random

def game():
    comp = random.choice(["Snake", "Water", "Gun"])
    user = input("\nEnter Choice (Snake, Water, Gun) or 'Exit': ").strip().capitalize()
    Dict = {"Snake": 1, "Water": 0, "Gun": -1}

    if user == "Exit":
        print("Thanks for playing!")
        return
    if user not in Dict:
        print("Invalid input, try again.")
        print("--------------------")
        return game()
    if Dict[user] != Dict[comp]:
        print(f"Computer chose: {comp}")
        if Dict[user] - Dict[comp] in {1, -2}:
            print(f"You Win, Lets Play Again")
            print("--------------------")
            return game()
        if Dict[user] - Dict[comp] in {-1, 2}:
            print(f"You Lose, Lets Play Again")
            print("--------------------")
            return game()
    else:
        print(f"Computer chose: {comp}")
        print(f"Draw, Lets Play Again")
        print("--------------------")
        return game()

game()
