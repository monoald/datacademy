from os import system

def validate_option():

    valid_options = ['1', '2', '3', '4', '5']
    while True:
        try:
            option = input('')

            if option != valid_options:
                raise ValueError('SELECT A VALID OPTION!')

            break
        except ValueError as ve:
            system('clear')
            print(ve)

    return option


def main():

    # Longitude in relation to 1 mile
    longitude_miles = [{'miles': 1}, {'kilometers': 1.60934}, {'meters': 1609.34}, {'yard': 1760}, {'feet': 5280}]

    options = """
    1. Miles.
    2. Kilometers.
    3. Meters.
    4. Yards.
    5. Feets.
    """

    print(f"""Select the longitude you have:
    {options}
    """)
    actual_longitude = validate_option()

    print("""What is length you have?
    """)
    actual_length = float(input(''))

    print(f"""Select the longitude you want to convert to:
    {options}
    """)
    longitude_convertion = validate_option()


if __name__ == '__main__':
    main()