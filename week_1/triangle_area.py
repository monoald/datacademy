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


def triangle_type(side_a, side_b, base):
    """Identify the type of a triangle

    Args:
    side_a (float): Triangle Side Positive float
    side_b (float): Triangle Side Positive float
    """
    if side_a == side_b and side_a == base:
        triangle = 'Equilateral'
    elif side_a == side_b and side_a != base:
        triangle = 'Isosceles'
    else:
        triangle = 'Scalene'

    print(f'The triangle is {triangle}')


def main():

    # Welcome message
    print('Welcome! In this program you will get the area of your triangle')
    system('clear')

    # Ask for the base of the triangle avoiding errors
    base = accept_posi_num('base')

    system('clear')

    # Ask for the height of the triangle avoiding errors
    height = accept_posi_num('height')

    system('clear') 

    print(f'Base: {base}')
    print(f'Height: {height}')

    # Get area 
    area = triangle_area(base, height)

    print(f'The area of your triangle is: {area}')

    # Ask the user to know the triangle type
    print('\nYou wan\'t to know the type of the triangle?')
    print('     1. YES      2. NO')

    while True:
        try:
            option = input('')
            
            if option == '1' or option == '2':
                break
            
            raise Exception('ENTER A VALID OPTION!')
        except Exception as e:
            print(e)

    system('clear')

    if option == '1':
        a_side = accept_posi_num('first side') 

        b_side = accept_posi_num('second side') 

        triangle_type(a_side, b_side, base)
    
    print('Thanks to use our program!')



if __name__ == '__main__':
    main()