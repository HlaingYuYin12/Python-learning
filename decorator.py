# def greet(fun):
#     def wrapper():
#         #before
#         print('hello')
#         fun()  #sayName()
#         #after
#         print('good bye')

#     return wrapper

# @greet #decorator
# def sayName():
#     print('Hlaing Yu Yin')

# sayName()



def greet(fun):
    def wrapper(name):
        #before
        print('hello')
        fun(name)  #sayName()
        #after
        print('good bye')

    return wrapper

@greet #decorator
def sayName(name):
    print(name)

sayName('Hlaing Yu')