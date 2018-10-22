filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in mmddyy format.')
if birthday in pi_string:
    print('Birthday in first million digits of pi!')
else:
    print('Birthday not in first million digits of pi.')
