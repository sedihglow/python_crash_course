from restaurant_class import restaurant, ice_cream_stand


my_rest = restaurant('heath', 'french')

print(my_rest.name)
print(my_rest.ctype)

my_rest.desc_restaurant()
my_rest.open_restaurant()

my_rest.set_num_served(10)
my_rest.inc_num_served(10)

stand = ice_cream_stand('ice shop', 'ice cream', 'vanilla', 'chocolate')
stand.disp_flavors()
