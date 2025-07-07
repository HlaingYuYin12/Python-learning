file = open('./text.txt')

for line in file :
    print(line)


file.seek(0) # cursor in front of first letter
lineLists = file.readlines()
print(lineLists)


file.seek(34) #from
paragraph = file.read(100) #to
print(paragraph)

# file.close()
#or
with open('./text.txt') as file : #close sa yar ma lo (must use)
    for line in file :
        print(line)
print('other work')