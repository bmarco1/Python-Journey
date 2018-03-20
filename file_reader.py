with open ('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#new test

filename = 'pi_digits.txt'
with open (filename) as file_object:
    for line in file_object:
        print(line.strip())

#new test

filename = 'pi_digits.txt'
with open (filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#new test

filename = 'pi_digits.txt'
with open (filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#new test