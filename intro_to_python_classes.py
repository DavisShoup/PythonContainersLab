# Let's define a Python Class

# class Dog():
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'Dog Object with a name of {self.name} is {self.age} years old'

#     def bark(self):
#         print(f'{self.name} says woof')

# class ShowDog(Dog):
#     def __init__(self, name, age = 0, total_earnings = 0):
#         Dog.__init__(self, name, age)

#         self.total_earnings = total_earnings

#     def add_prize_money(self, amount):
#         self.total_earnings += amount
#         print(f'''{self.name} has just earned {amount}, bringing total earnings to {self.total_earnings}''')

# binky = ShowDog('Binky', 5, 1500)

# print(binky)
# binky.bark()
# binky.add_prize_money(500)

######################################################
# class Vehicle():

#     vehicle_id = 1

#     def __init__(self, vin, make, model):
#         self.vin = vin
#         self.make = make
#         self.model = model
#         self.running = False
#         self.id = Vehicle.vehicle_id

#         Vehicle.vehicle_id += 1

#     def __str__(self):
#         return f'Vehicle VIN({self.vin}) is a {self.make} {self.model}'

#     def start(self):
#         self.running = True
#         print('...running')

#     def stop(self):
#         self.running = False
#         print('...stopped')

#     @classmethod
#     def get_total_vehicles(cls):
#         return f'There are currently {cls.vehicle_id -1} vehicle objects'

# tesla = Vehicle('abc123', 'Tesla', 'Model S')
# super_bike = Vehicle('xyz-456', 'BMW', 's1000rr', )

# # print(tesla)
# # tesla.start()
# # tesla.stop()

# # print(tesla.__dict__)
# # print(super_bike.__dict__)

# print(Vehicle.get_total_vehicles())