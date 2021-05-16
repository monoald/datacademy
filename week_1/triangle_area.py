from os import system

def accept_posi_num(variable):
    """Ensures to receive a positive number from user

    Args:
    variable (str): Varibale name to print

    Returns:
    float: Positive number from user
    """
    while True:

        try:
            positive_number = float(input(f'Enter the {variable} of the triangle: '))

            if positive_number == 0:
                raise Exception(f'THE {variable.upper()} OF A TRIANGLE CAN NOT BE ZERO!')
            elif positive_number < 0:
                raise Exception(f'THE {variable.upper()} OF A TRIANGLE CAN NOT BE NEGATIVE!')

            break
            
        except ValueError as ve:
            system('clear')
            print('ENTER A NUMBER PLEASE!')
        
        except Exception as e:
            system('clear')
            print(e)

    return positive_number


def triangle_area(base_t, height_t):
    """Gets the area of a triangle

    Args:
    base_t (float): Triangle Base Positive float
    base_t (float): Triangle Height Positive float

    Returns:
    float: Triangle area
    """
    return (base_t * height_t)/2


def main():

    # Welcome message
    print('Welcome! In this program you will get the area of your triangle')
    system('clear')

    # Ask for the base of the triangle avoiding errors
    base = accept_posi_num('base')

    system('clear')

    print(f'Base: {base}')

    # Ask for the height of the triangle avoiding errors
    height = accept_posi_num('height')

    system('clear') 

    print(f'Base: {base}')
    print(f'Height: {height}')

    # Get area 
    area = triangle_area(base, height)

    print(f'The area of your triangle is: {area}')


if __name__ == '__main__':
    main()