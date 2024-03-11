John_file = open('book of John Text.txt','r')
#print(John.read())
j = John_file.read() 
John_list = j.split()
Father_count = 0
God_count = 0
Christ_count = 0
Spirit_count = 0
spirit_count = 0
man_count = 0
life_count = 0


for i in John_list:
    if i == 'Father':
        Father_count += 1
    if i == 'God':
        God_count += 1
    if i == 'Christ':
        Christ_count += 1
    if i == 'Spirit' :
        Spirit_count += 1
    if i == 'spirit':
        spirit_count += 1
    if i == 'life':
        life_count += 1
    if i == 'man':
        man_count += 1


print(f'Father: {Father_count}')
print(f'God: {God_count}')
print(f'Christ: {Christ_count}')
print(f'Spirit: {Spirit_count}')
print(f'spirit: {spirit_count}')
print(f'Life: {life_count}')
print(f'Spirit: {man_count}')


John_file.close()