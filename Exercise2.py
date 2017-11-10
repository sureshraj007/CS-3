# pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    hours = float(hours)
    rate = float(rate)
    print('Both are integer')
except:
    print('Error, please enter numeric input')

hours = input('Enter Hours: ')
try:
    hours = float(hours)
    print('Hours is integer')
except:
    print('Error, please enter numeric input')
