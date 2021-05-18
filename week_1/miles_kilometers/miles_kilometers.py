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


def miles_to_others(length, convertion_longitude):
    """Convert from miles to other longitude.

    Args:
    length (float): Length you want to convert
    convertion_logitud (dict): Dict of the desired longitud

    Returns:
    float: Length in other longitude
    """
    return length * convertion_longitude['length']


def others_to_miles(length, convertion_longitude):
    """Convert from other longitude to miles.

    Args:
    length (float): Length you want to convert
    convertion_logitud (dict): Dict of the desired longitud

    Returns:
    float: Length in other longitude
    """
    return length / convertion_longitude['length']


def others_to_others(length, actual_longitude, convertion_longitude):
    """Convert from other longitude to other longitud.

    Args:
    length (float): Length you want to convert
    convertion_logitud (dict): Dict of the desired longitud

    Returns:
    float: Length in other longitude
    """
    convertion_number = convertion_longitude['length'] / actual_longitude['length']

    return convertion_number * length


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

    #print(longitude_miles[longitude_convertion])

    # Convertion Logic
    if actual_longitude == 1:
        length_converted = miles_to_others(actual_length, longitude_miles[longitude_convertion])
    elif longitude_convertion == 1:
        length_converted = others_to_miles(actual_length, longitude_miles[actual_longitude])
    elif actual_length != 1 and longitude_convertion != 1:
        length_converted = others_to_others(actual_length, longitude_miles[actual_longitude], longitude_miles[longitude_convertion])

    # Print final convertion
    system('clear')
    print(f"{actual_length} {longitude_miles[actual_longitude]['longitude']} are {round(length_converted, 2)} {longitude_miles[longitude_convertion]['longitude']}")


if __name__ == '__main__':
    main()