try:
    with open('cats.txt') as cats:
        cat_names = cats.read()
    with open('dogs.txt') as dogs:
        dog_names = dogs.read()
except FileNotFoundError:
    pass
else:
    print(cat_names)
    print(dog_names)