class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name.title() + ' serves ' + self.cuisine.title() + ' food.')

    def open_restaurant(self):
        print(self.name.title() + ' is now open')


mykonos = Restaurant('mykonos', 'greek')
dolce_vita = Restaurant('dolce vita', 'italian')
fat_bob = Restaurant('fat bob', 'american')

mykonos.describe_restaurant()
mykonos.open_restaurant()
dolce_vita.describe_restaurant()
dolce_vita.open_restaurant()
fat_bob.describe_restaurant()
fat_bob.open_restaurant()