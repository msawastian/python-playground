

while True:
    first_number = input('First number: ')
    second_number = input('Second number: ')
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('Please enter a number.')
    else:
        print(answer)
