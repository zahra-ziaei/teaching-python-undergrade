#---------------------------------
# Shows some examples related to functions and error handling.
# Important Rule 1: Any code that is repeated more than twice should be put in a function.
# Important Rule 2: Error handling is an extremely important but under appreciated aspect of Python.
#---------------------------------


# An example of a function. Note that there are no braces. The function interior is just tabbed in.
def add(x, y):
    print("Helloooo! I'm inside a function.")
    return x + y


# This function will cause problems due to divide by zero.
def divide_unsafe(x, y):
    return x / y


# This function will not cause problems (but may not be logically correct).
def divide_safe(x, y):
    try:
        return x / y
    except Exception as e:
        print(e)
        print('STOP: HERE\'S AN ERROR')
        return 0


print('-----------------------')
print('The addition function.')
number = add(1, 1)
print(number)

print('-----------------------')
print('An unsafe function')
#number = divide_unsafe(1, 0)

# SOLUTION 1: Error handling in the function. This is best if it makes logical sense.
print('-----------------------')
print('Error handling in the function')
number = divide_safe(1, 0)
print(number)

# SOLUTION 2: Error handling when calling the function. This is suboptimal but often necessary.
print('-----------------------')
print('Error handling in the call to the function')
try:
    number = divide_unsafe(1, 0)
except:
    print('Division error...')
    number = -1
print(number)



