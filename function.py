# def greet(name) :
#     print(f'good night,{name}')

# greet('Hlaing Yu')
# greet('Yin')

# def greet(name,time) : #parameter
#     print(f'{time},{name}')

# greet('Hlaing Yu','Morning')
# greet('Yin','hello') #argument

def greet(name='Yu', time='morning') :
    print(f'good {time},{name}')

greet('Hlaing Yu')
greet(name='Yu',time='night')
