#pair of key and value means dictionary
person ={
    'name' : 'HYY',
    'age' : 23
}
# print(person['name'])

# person['hair_color']='black';
# print(person)

print('name' in person ) #if has, return True
print('nothing' in person ) #if don't have, return False

if 'name' in person :
    print('a student')


# change to list
person_keys = list(person.keys())
print(person_keys)

person_values = list(person.values())
print(person_values)