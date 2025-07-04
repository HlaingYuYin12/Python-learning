# from car import Car #module
# bmw =Car('BMW',4)
# bmw.drive()

from Car.car import Car #package (need __init__.py)
from Car.functions import checkEngine

bmw =Car('BMW',4)
bmw.drive()
checkEngine()