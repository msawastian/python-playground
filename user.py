class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("This user's name is: " + self.first_name.title() + ' ' + self.last_name.title() + '.')

    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


john_smith = User('john', 'smith')
jane_doe = User('jane', 'doe')

john_smith.describe_user()
john_smith.greet_user()
jane_doe.describe_user()
jane_doe.greet_user()
john_smith.increment_login_attempts()
john_smith.increment_login_attempts()
john_smith.increment_login_attempts()
john_smith.increment_login_attempts()
print(john_smith.login_attempts)
john_smith.reset_login_attempts()
print(john_smith.login_attempts)
