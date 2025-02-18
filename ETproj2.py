# Program that asks the user for 2 positive integers
# If both numbers can be divided evenly to each other exits program and displays True with result
# Keeps asking for integer input until function results in True

# Asking user for positive integer input
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

# function that will test to see if the input integers can be divided by each other evenly

def division(a, b):
    while True:
        if a % b == 0:
            return f"Well done {a} divided by {b} divides evenly"
        elif b % a == 0:
            return f"Well done {b} divided by {a} divides evenly"
        else:
            a = int(input('Enter a number: '))
            b = int(input('Enter another number: '))
           

result = division(a, b)
print(result, a % b == 0 or b % a == 0)