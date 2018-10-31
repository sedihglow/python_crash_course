players = ['charles', 'martina', 'martin', 'florence', 'eli']
print(players[0:3])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#hard copy a list
pcopy = players[:]
print(pcopy)

print("Three items from the middle of the list are:")
print(pcopy[1:4])

print("The last three items in the list are")
print(pcopy[-3:])

pcopy.append('newplayer')

print(pcopy)
print(players)

# use a for loop to print the seperate lists
for p in pcopy:
    print(p)

for p in players:
    print(p)

# copy a pointer to a list
ptr = players
players.append('both')
print(ptr)
