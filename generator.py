words = ['apple','orange','lemon','lime','banana']


from random import randint; #random module ,randint function
def randomSentenceGenerator(word):
    randomIndex = randint(0,len(words)-1) #dynamically
    return f'{words[randomIndex]} {word}'


with open('./text.txt') as file :
    # print(file.read())
    paragraph = file.read()
    wordLists = paragraph.split() #words split
    sentenseList = list(map(randomSentenceGenerator,wordLists))
    paraCount = int(input('paragraph count: '))

    for count in range(paraCount):
        with open('./generator.txt','a') as write_file :
            write_file.write(''.join(sentenseList)+'\n\n')#change list[] to string and use 'join' method