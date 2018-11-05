class restaurant():
    def __init__(self, name, ctype):
        self.name = name
        self.ctype = ctype
        self.num_served = 0

    def desc_restaurant(self):
        print("Restaraunt name is " + self.name.title())
        print("The type of food is " + self.ctype)

    def open_restaurant(self):
        print(self.name.title() + " is now open.")

    def set_num_served(self, num):
        if (num > 0):
            self.num_served = num
            print("Number served is now " + str(num))
        else:
            print("cannot serve a negetive value")

    def inc_num_served(self, num): 
        if (num > 0):
            self.num_served += num
            print("Number served is now " + str(self.num_served))
        else:
            print("Cannot incrememnt by a negetive value")

# NOTE: When doing child classes, the __init__ for the child should be below
#       the parent class, and call the parents constructor with super().__init__(x,y,z)

class ice_cream_stand(restaurant):
    def __init__(self, name, ctype, *flavors):
        super().__init__(name, ctype)
        self.flavors = [] # = falvors # makes a tuple
        for flavor in flavors:
            self.flavors.append(flavor)

    def disp_flavors(self):
        print("todays icecream flavors are " + str(self.flavors))
