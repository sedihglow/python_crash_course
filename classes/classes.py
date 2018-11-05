class dog():
    def __init__(self,name,age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """ Simulate a dog sitting """
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog('willie', 6)
