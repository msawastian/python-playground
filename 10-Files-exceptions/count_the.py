with open('alice.txt') as f_obj:
    contents = f_obj.read()

count_the = contents.lower().count('the')

print(count_the)