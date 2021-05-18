from os import system
from random import choice
from random import seed


def main():

    system('clear')    

    # Weapons
    weapons = [{'weapon': 'rock', 'icon': '👊'}, {'weapon': 'paper', 'icon': '🖐'}, {'weapon': 'scissors', 'icon': '🖖'}]
    user_score = 0
    bot_score = 0
    rounds = 0

    # Game flow
    while rounds < 3:

        # Ask for user weapon avoiding invalid options
        while True:
            try:
                print("""               WELCOME
           TYPE YOUR OPTION

        ROCK   PAPER  SCISSORS
         👊     🖐       🖖
                """)
                user_weapon = input('').lower()

                for weapon in weapons:
                    
                    if user_weapon in weapon['weapon']:
                        user_weapon = weapon
                        break
                        
                    if weapon == weapons[len(weapons) - 1]:
                        raise ValueError('CHOOSE A VALID OPTION!')  

                break

            except ValueError as ve:
                system('clear')
                print(ve)

        # Select secure random weapon for bot
        seed()
        bot_weapon = choice(list(weapons))

        # Print selections
        system('clear')
        print(f"""          YOUR WEAPON       BOT WEAPON
            {user_weapon['weapon']}             {bot_weapon['weapon']}
            {user_weapon['icon']}                 {bot_weapon['icon']}
        """)

        # Game logic & Scores
        if user_weapon['weapon'] == bot_weapon['weapon']:
            print('                 TIE     ')
        elif user_weapon['weapon'] == 'rock' and bot_weapon['weapon'] == 'scissors':
            print('         USER WINS THE ROUND ')
            user_score += 1
        elif user_weapon['weapon'] == 'paper' and bot_weapon['weapon'] == 'rock':
            print('         USER WINS THE ROUND ')
            user_score += 1
        elif user_weapon['weapon'] == 'scissors' and bot_weapon['weapon'] == 'paper':
            print('         USER WINS THE ROUND ')
            user_score += 1
        else:
            print('         BOT WINS THE ROUND  ')
            bot_score += 1

        input('PRESS ENTER TO CONTINUE TO THE NEXT ROUND')
        system('clear')
        
        rounds += 1

    print(f'User: {user_score}\nBot: {bot_score}')

    # Determine winner or declare tie
    if user_score > bot_score:
        print('     YOU WIN!!     ')
    elif user_score < bot_score:
        print('     YOU LOSE!!      ')
    else:
        print('         TIE!!        ')


if __name__ == '__main__':
    main()