class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This user's name is: " + self.first_name.title() + ' ' + self.last_name.title() + '.')

    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + '!')


john_smith = User('john', 'smith')
jane_doe = User('jane', 'doe')

john_smith.describe_user()
john_smith.greet_user()
jane_doe.describe_user()
jane_doe.greet_user()
