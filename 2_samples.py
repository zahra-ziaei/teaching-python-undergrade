#--------------------------------
# These are some sophisticated data types that are native to Python.
#--------------------------------

# 1) Lists.
print('--------------')
print('Lists')
animals = ['lions', 'tigers', 'bears']
animals[0] = 'elk'
print(animals)
print(animals[0])

# 2) Tuple. These are like frozen lists.
print('--------------')
print('Tuples: these are immutable.')
animals = ('lions', 'tigers', 'bears')
print(animals)
print(animals[0])
# NOTE: Because they are immutable, you cannot do this:
# animals[1] = 'elk'
animals = list(animals) # Can change a tuple to a list like so.

# 3) Sets.
print('--------------')
print('Sets')
animals_scary = {'lions', 'tigers'}
animals_scary.add('honey_badgers') # Adds an element.
animals_scary.add('lions')         # Does nothing. Lions already in the set.
animals_cats  = {'lions', 'tigers', 'house_cats'}
animals_union = animals_scary.union(animals_cats)
animals_diff  = animals_scary.difference(animals_cats)
print(animals_union)
print(animals_diff)

# 4) Dictionary.
print('--------------')
print('Dictionary')
animals = {'lions': 3,
           'tigers': 4,
           'bears': 5}
print(animals)
print(animals['tigers'])
print(animals.keys())
print(animals.values())

#--------------------------------
# Note: Types can contain other types.
#--------------------------------
# Lists of tuples
print('--------------')
print('Lists of tuples.')
animals = [('lions', 3, 5),
           ('tigers', 4, 6),
           ('bears', 5, 8)]
print(animals)
print(animals[0])
print(animals[0][0])

# Dictionary of lists.
print('--------------')
print('Dictionary of lists.')
animals = {'lions':  ['Frank', 'Al', 'George'],
           'tigers': ['Alex', 'Jenny', 'Sue'],
           'bears':  ['Kevin', 'Audrey']}
print(animals)
print(animals['bears'])
print(animals['bears'][1])
