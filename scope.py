name = 'Hlaing Yu Yin' #global variable

def sayMyName() :
    global name;
    #local variable
    name = 'Aye Aye'
    print(name)

sayMyName()
print(name)