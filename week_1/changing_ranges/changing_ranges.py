from os import system
def valid_numbers(variable_name):
    while True:
        try:
            number = float(input(f'Enter the {variable_name}: '))

            break
            
        except ValueError as ve:
            print('ENTER A NUMBER!')

    return number


def main():
    system('clear')

    # Ask the user foot parameters
    lower_limit = valid_numbers('lower limit')

    upper_limit = valid_numbers('upper limit')

    comparison = valid_numbers('comparison')

    # Program logic
    if comparison > lower_limit and comparison < upper_limit:
        print(f'{comparison} is between {lower_limit} and {upper_limit}')
    elif comparison < lower_limit:
        print(f'{comparison} is lower than {lower_limit}')
    elif comparison > upper_limit:
        print(f'{comparison} is upper than {upper_limit}')


if __name__ == '__main__':
    main()