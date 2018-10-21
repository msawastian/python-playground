class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' kilometers on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(100)


class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + ' kWh battery.')


my_new_car = Car('skoda', 'citigo', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(18700)
my_new_car.read_odometer()
my_new_car.update_odometer(0)
my_tesla = ElectricCar('tesla', 'model 3', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
