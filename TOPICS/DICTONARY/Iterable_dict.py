

# Dicts are iterable:


person= {

    'id': 223,
    'name': "rahil",
    'email': 'rahil28@gmail.com',
    'address': "India"
    }

print(person)

person['state']= "Gujarat"

print(person)

print()

'''

.keys():  return key only
.values(): return values only
.items(): return key value pair

'''

# For Example:

for x in person.keys():
    print(x)

print()

for y in person.values():
    print(y)

print()

for i,j in person.items():
    print(f'{i}: {j}')

print()


# Return automatically keys :x
for x in person:
    print(x)
