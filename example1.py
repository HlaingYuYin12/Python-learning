person = {}

while True :
    name = input('name: ')
    age = input('age: ')
    person[name] = age

    another = input('another y/n: ')
    if another == 'y' :
        continue;
    else :
        break;

# print(person)

for (key,value) in person.items() : #dict mar item a yin swal htote ya mal
    print(f'{key} is {value} years old')
