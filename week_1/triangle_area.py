from os import system

def triangle_area(base_t, height_t):
    return (base_t * height_t)/2

def main():

    # Welcome message
    print('Welcome! In this program you will get the area of your triangle')
    system('clear')

    # Ask for the base of the triangle avoiding errors
    while True:

        try:
            base = int(input('Enter the base of the triangle: '))

            if base == 0:
                raise Exception('THE BASE OF A TRIANGLE CAN NOT BE ZERO!')
            elif base < 0:
                raise Exception('THE BASE OF A TRIANGLE CAN NOT BE NEGATIVE!')

            break
            
        except ValueError as ve:
            system('clear')
            print('ENTER A NUMBER PLEASE!')
        
        except Exception as e:
            system('clear')
            print(e)

    system('clear')

    # Ask for the height of the triangle avoiding errors
    while True:

        print(f'Base: {base}')

        try:
            height = int(input('Enter the height of the triangle: '))

            if height == 0:
                raise Exception('THE HEIGHT OF A TRIANGLE CAN NOT BE ZERO!')
            elif height < 0:
                raise Exception('THE HEIGHT OF A TRIANGLE CAN NOT BE NEGATIVE!')

            break
            
        except ValueError as ve:
            system('clear')
            print('ENTER A NUMBER PLEASE!')
        
        except Exception as e:
            system('clear')
            print(e)

    system('clear')
    print(f'Base: {base}')
    print(f'Height: {height}')

    # Get area 
    area = triangle_area(base, height)

    print(f'The area of your triangle is: {area}')


if __name__ == '__main__':
    main()