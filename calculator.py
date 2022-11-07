# function to add,sub,mul,div and exp
def calculate():
    operation = input("  Please select operation -\n" \
        "  + for Add\n" \
        "  - for Subtract\n" \
        "  * for Multiply\n" \
		"  / for Divide\n" \
        "  % for Reminder\n" \
		"  ** for exponential\n")

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
	
    elif operation == '%':
        print('{} % {} = '.format(number_1,number_2))
        print(number_1 % number_2)

    elif operation == '**':
        print('{} ** {} = '.format(number_1,number_2))
        print(number_1 ** number_2)
    
		
    else:
        print('Invalid operator, please run the program again.')

    # Add again() function to calculate() function
    again()
#===============================================================
# function again() ask user if he wants to make another operation 
def again():
    calc_again = input(
"  Do you want to calculate again?\n \
   Please type Y for YES or N for NO.\n")

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('	See you later.')
    else:
        again()

		
		
def again_1():
    calc_again1 = input(
"  Do you want to convert number again?\n \
   Please type Y for YES or N for NO.\n")

    if calc_again1.upper() == 'Y':
        program_calc()
    elif calc_again1.upper() == 'N':
        print('	See you later.')
    else:
        again_1()
#===========================================================
# function that convert decimal number into binary , octal or hexadecimal
def program_calc():
	
	convert = input("  Please select type to convet number to it -\n" \
        "  b for binary\n" \
        "  h for hexadecimal\n" \
        "  o for octal\n")
	number = int(input('Please enter the number to convert : '))
	if convert == 'b':
		print("  The value of", number, "is:")
		print(bin(number), "in binary.")
		
	elif convert == 'o':
		print("  The value of", number, "is:")
		print(oct(number), "in octal.")

	elif convert == 'h':
		print("  The value of", number, "is:")
		print(hex(number), "in hexadecimal.")
		
	else :
		print('Invalid selection, please run the program again.')
	
	again_1()
#===========================================================
# main program
print(" 	***Welcome to Calculator***   ")
print("---------------------------------------------")
print('''  
  1 . scientific calculator.
  2 . programming calculator.
''')
print("---------------------------------------------")



select = int(input(" Enter 1 or 2 to select scientific or programming calculator : "))		
# calling function calculate ()
if select == 1:
	calculate()
# calling function program_calc()
elif select == 2:
    program_calc()


