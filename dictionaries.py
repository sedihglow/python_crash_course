alien_0 = { #defines key : value
    'color': 'green', 
    'points': 5
    } 

print(alien_0['color'])  # green
print(alien_0['points']) # 5

# keys value can be anything, list, string, dictionary

# Adding key value pairs
print("\nadding key value pairs")
alien_0['x_pos'] = 0
alien_0['y_post'] = 25
print(alien_0)

# change value
alien_0['color'] = 'yellow'
print("alien is now " + alien_0['color'])

# Can add speed and have an if else block to give an x/y increment value then
# use addition to increment the value in the dictionary

del alien_0['points']
alien_0['points'] = 10

# Method .items returns key value pairs and stores them in k,v
# Or .keys(), sorted(xxx.keys()), .values, 
# set(xxx.values) no repeated values in a set, like discrete math
for key, value in alien_0.items(): 
    print("\nkey: " + key)
    print("value: " + str(value))
