class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + ' serves ' + self.cuisine.title() + ' food.')

    def open_restaurant(self):
        print(self.name.title() + ' is now open')

    def set_numbers_server(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


mykonos = Restaurant('mykonos', 'greek')
dolce_vita = Restaurant('dolce vita', 'italian')
fat_bob = Restaurant('fat bob', 'american')

mykonos.describe_restaurant()
mykonos.open_restaurant()
dolce_vita.describe_restaurant()
dolce_vita.open_restaurant()
fat_bob.describe_restaurant()
fat_bob.open_restaurant()
print(mykonos.number_served)
mykonos.number_served = 1
print(mykonos.number_served)
mykonos.set_numbers_server(2)
print(mykonos.number_served)
mykonos.increment_number_served(1)
print(mykonos.number_served)