
# Simple for loop.
print('-------------')
print('For loop')
for i in range(0, 5):
    print(i)

# Can also iterate over a list.
print('-------------')
print('For loop over list')
numbers = [1, 2, 3, 4, 5]
print(numbers)
for number in numbers:
    print(number)

# A while loop.
print('-------------')
print('While loop')
done = False
i = 0
while not done:
    i = i + 1
    if i > 5:
        print('done')
        done = True
print(i)

#--------------------------
# Illustrates more sophisticated iterations.
#--------------------------
# Now suppose we want to select all list elements that are less than 4.
# We could do it like this, but it's awkward.
print('-------------')
print('Subsetting a list manually.')
new_list = []
for number in numbers:
    if number < 4:
        new_list.append(number)
print(new_list)

# Let's use a "list comprehension" instead.
print('-------------')
print('Subsetting a list via a list comprehension.')
new_list = [number for number in numbers if number < 4]
#new_list = [     x for      x in numbers if      x < 4] # NOTE: This is the same as the previous, but less Pythonic.
print(new_list)

# # List comprehensions are magical.
print('-------------')
print('Subsetting a list via a list comprehension.')
new_list = [number + 10 for number in numbers if number < 4]
print(new_list)


#--------------------------
# Sorting a list.
#--------------------------
print('-------------')
print('Sorting a list')
numbers = [5, 2, 1, 4, 3]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

