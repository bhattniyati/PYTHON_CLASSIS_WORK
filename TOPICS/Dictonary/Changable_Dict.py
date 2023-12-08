

# Dicts are Mutable/Changable:



person= {

    'id': 2020,
    'name': "Keys",
    'email': 'keys@gmail.com',
    'address': "Ahmedabad"
    }


print(person)

person['email']= "Kys@gmail.com"


# 2 method through declared..
print(person['email'])
print(person.get('email'))
