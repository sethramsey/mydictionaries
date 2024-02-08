import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


''''''''''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {}  #will create an empty dictionart

mydictionary = dict(m=8,n=9)   #m and n are the keys and 8 and 9 are the values
print(mydictionary)

print()
print('*****  end section 1 ********')
print()


''''''''


print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'chris'

if name in phonebook:              #in defualt search options, it will only look at keys
    print(f'Name:{name} Phone Number: {phonebook[name]}')       #pyhton is case sensitive so make sure that the key matches what you are looking for

else:
    print(f'{name} is not in the phonebook')



print()
print('*****  end section 2 ********')
print()



''''''''''''



print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)

phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()


''''''



print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Chris']

print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:           #key is a variable
    print(f'Name: {key} Phone number: {phonebook[key]}')


for value in phonebook.values():
    print(value)


#.iteams produces a typone (2 values together like ('xxxx','yyyy')) so if you give it two vairables it will split it bwteen the two
for k,v in phonebook.items():
    print(f'Name: {k} Phone number: {v}')

                    
print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chris",'555-5555')
print(phone)

phonebook.clear()
print(phonebook)

print()
print('*****  end section 6 ********')
print()

''''''''

print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
phone = phonebook.pop("Chris",'name not found')
print(phone)
print(phonebook)




print()
print('*****  end section 7 ********')
print()

'''''''

print()
print('*****  start section 8 - using popitem ********')
print()

phone = phonebook.popitem()
print(phone)

print(phonebook)




print()
print('*****  end section 8 ********')
print()

'''''

print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])


#alternatively as one line of code
print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()


''''''''





