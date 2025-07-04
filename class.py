# name = 'Hyy'
# print(name.upper())

class Car : #must be capital letter
    def __init__(self, name ,wheels) : #must include init() to build class and they are methods in a class
        self.name = name
        self.wheels = wheels
    
    def drive(self):
        print(f'{self.name} is driving')

    def stop(self):
        print(f'{self.name} is stopped')


# print(bmw.name)
bmw =Car('BMW',4)
bmw.drive()

mcd =Car('Mercedes', 4)
mcd.stop()


