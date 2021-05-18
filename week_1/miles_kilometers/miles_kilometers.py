from os import system

def validate_option(message):
    """Ensures to receive only a valid option.

    Returns:
    int: Valid option
    """
    valid_options = ['1', '2', '3', '4', '5']

    while True:
        try:
            print(message)
            option = input('')

            if option not in valid_options:
                raise ValueError('SELECT A VALID OPTION!')

            break
        except ValueError as ve:
            system('clear')
            print(ve)

    return int(option)


def convertion_miles(length, convertion_longitude):
    """Convert from miles.

    Args:
    word (str): Word to operate

    Returns:
    str: Word without accent marks
    """
    return length * convertion_longitude['length']


def main():

    # Longitude in relation to 1 mile
    longitude_miles = ['empty',
        {'longitude': 'miles', 'length': 1}, {'longitude': 'kilometers', 'length': 1.60934}, {'longitude': 'meters', 'length': 1609.34}, 
        {'longitude': 'yard', 'length': 1760}, {'longitude': 'feet', 'length': 5280}
    ]

    options = """
    1. Miles.
    2. Kilometers.
    3. Meters.
    4. Yards.
    5. Feets.
    """

    # Ask for actual longitude
    system('clear')
    al_message = f"""Select the longitude you have:
    {options}
    """
    actual_longitude = validate_option(al_message)

    # Ask for the length to convert
    system('clear')
    lc_messagae = 'What is length you have?'
    while True:
        try:
            print(lc_messagae)
            actual_length = float(input(''))

            break
        except ValueError as ve:
            print('THE VALUE YOU ENTER CAN NOT BE A LENGTH')

    # Ask for the longitude to convert to
    system('clear')
    lconverter_message = f"""Select the longitude you want to convert to:
    {options}
    """
    longitude_convertion = validate_option(lconverter_message)

    # Convertion Logic
    if actual_length == 1:
        my_length = convertion_miles(actual_length, longitude_miles[longitude_convertion])
        print(my_length)


if __name__ == '__main__':
    main()