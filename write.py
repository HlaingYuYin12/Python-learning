with open('./about.txt', 'w') as file : #w mean write
    file.write('I am Hlaing Yu Yin')
    file.write('\nI am an IT student')

#other work
with open('./about.txt', 'a') as file: #a mean among(add)
    file.write('\nI am 23 years old') 

lists = ['\nI am YuYu','\nI am 33 years old']
with open('./about.txt', 'a') as file:
    file.writelines(lists)
