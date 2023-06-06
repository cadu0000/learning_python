import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def main():
    result = ""
    choose = input("choose one: rock, paper or scissor\n").lower()

    if choose == "rock":
        choose = rock
    elif choose == "paper":
        choose = paper
    elif choose == "scissor":
        choose = scissor
    else:
        print("invalid choice!!")
        main()

    print(f"you chose {choose}\n")
    possibilities = [rock, paper, scissor]

    enemy = possibilities[random.randint(0, 2)]

    if enemy == rock and choose == rock:
        result = "DRAWN"
    elif enemy == rock and choose == paper:
        result = "YOU LOST"
    elif enemy == rock:
        result = "YOU WIN"

    if enemy == paper and choose == paper:
        result = "DRAWN"
    elif enemy == paper and choose == scissor:
        result = "YOU LOST"
    elif enemy == paper:
        result = "YOU WIN"

    if enemy == scissor and choose == scissor:
        result = "DRAWN"
    elif enemy == scissor and choose == rock:
        result = "YOU LOST"
    elif enemy == scissor:
        result = "YOU WIN"

    print("the enemy chose:\n" + enemy)
    print("\n" + result)
