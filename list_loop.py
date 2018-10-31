names = ['alice', 'david', 'carolina']

for name in names:
    print(name.title() + " with a cat string")

print("post loop")

# square values in range
squares = []
for value in range(1,11):
    squares.append(value**2) # Store value squared into squares list

# Or do it in one line
squares = [value**2 for value in range(1,11)]

print("\n\n")
print(squares)


print(max(names)) #only goes by first letter value
print(min(names)) #only goes by first letter value
print(sum(squares)) #does not work with string

print("\n")

#print 0-20
for value in range(0,20):
    print(value)

# make a list of 0 - 100, odd
HUNDRED = 100
ml = list(range(1,HUNDRED,2))
print(ml)

# make list of multiples of 3 to 30, use for loop to print list
mult_three = [value*3 for value in range(0,11)]

for value in mult_three:
    print(value)


