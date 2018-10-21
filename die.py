from random import randint

x = randint(1, 6)


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


ten_sided_die = Die(10)
twenty_sided_die = Die(20)

i = 0
while i <= 10:
    twenty_sided_die.roll_die()
    i += 1
