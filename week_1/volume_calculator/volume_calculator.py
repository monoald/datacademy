from os import system
from formulas.volume_formulas import *


def valid_variables(variable_name):
    while True:
        try:
            variable = float(input(f'Enter the {variable_name}: '))

            if variable <= 0:
                raise Exception(f'This is an invalid value for the {variable_name}')

            break 

        except ValueError as ve:
            print(ve)

    return variable
    

def main():
    system('clear')
    valid_options = ['1', '2', '3', '4']

    print('    WELCOME TO THE VOLUME CALCULATOR') 
    print('BE SURE THAT YOUR DATA HAVE THE SAME UNITS')

    # Ask the user for the figure
    while True:
        print("""SELECT THE FIGURE YOU WANT TO GET THE VOLUME:
        1. Circular Cylinder
        2. Cone
        3. Cube
        4. Sphere
        """)
        try:
            figure = input('')
            
            if figure not in valid_options:
                raise Exception('SELECT A VALID OPTION')

            break

        except Exception as e:
            system('clear')
            print(e)

    system('clear')

    # Get the volume
    if figure == '1':
        # Ask for the radius & height in the function
        volume = volume_circular_cylinder(valid_variables('radius'), valid_variables('height'))
    elif figure == '2':
        # Ask for the radius & height in the function
        volume = volume_cone(valid_variables('radius'), valid_variables('height'))
    elif figure == '3':
        # Ask for the prism on the function
        volume = volume_cube(valid_variables('prism'))
    elif figure == '4':
        volume = volume_sphere(valid_variables('radius'))

    # Print result
    print(f'The volume of the cilinder is {round(volume, 2)}')


if __name__ == '__main__':
    main()