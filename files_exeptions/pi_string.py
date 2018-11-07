filename = 'pi_digits.txt'

# once file reaches EOF, the object closes .readline for single lines
with open(filename) as file_object:
    contents = file_object.read()

print(contents.rstrip())


with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# save the contents of the file in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip()) # rstrip prevents empty line 

print(str(lines))

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:20] + "...")
print(len(pi_string))

birthday = input("Enter your birthday (mmddyy): ")
if birthday in pi_string: # Wow, compares everything in the string
    print("Your birthday is in the first few digit of pi")
else:
    print("Your birthday is not in the first few digits of pi")
