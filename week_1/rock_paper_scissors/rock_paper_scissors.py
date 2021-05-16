from os import system
from random import choice
from random import seed


def main():

    system('clear')    

    weapons = {'rock': '👊', 'paper': '🖐', 'scissors': '🖖'}

    print("""   WELCOME
TYPE YOUR OPTION

ROCK   PAPER  SCISSORS
 👊     🖐      🖖""")

    while True:
        try:
            user_weapon = input('').lower()

            if user_weapon not in weapons:
                raise ValueError('CHOOSE A VALID WEAPON!!')

            break

        except ValueError as ve:
            print(ve)

    seed()
    bot_weapon = choice(list(weapons.values()))
    
    print(f'The bot weapon is {bot_weapon}')


if __name__ == '__main__':
    main()