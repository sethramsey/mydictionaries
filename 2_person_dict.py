person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child below are two options to do this
#list_of_children = (person['childern'])
#print(list_of_children(1))

#print = (person['children']['1'])


# print out the name of the cat

#print(person["pets"]['cat'])



# use a loop to print out the names of each child



for i in person['children']:
    print(i)

# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for k in person ['pets']:
    print(f'The type of pet is {k} and the name of the pet is {person['pets'][k]}')
          
#or do this
for k,v in person['pets'].iteam():
    print(f'The type of pet is {k} and the name of the pet is {person['pets'][k]}')