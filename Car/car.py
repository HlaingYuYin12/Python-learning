# name = 'Hyy'
# print(name.upper())

class Car : #must be capital letter
    sterringWheel = 1 #class level attribute
    def __init__(self, name ,wheels) : #must include init() to build class and they are methods in a class
        self.name = name #instant level attribute(not the same obj)
        self.wheels = wheels
    
    def drive(self):
        print(f'{self.name} is driving')

    def stop(self):
        print(f'{self.name} is stopped and it has {self.wheels} wheels')

    @classmethod #decorator (creating class level method)
    def common(cls) :
        print(f'all car have only {cls.sterringWheel} sterring wheel')

# print(bmw.name)
bmw =Car('BMW',4)
bmw.drive()


mcd =Car('Mercedes', 4)
mcd.stop()
mcd.sterringWheel
mcd.common()


Car.common()

