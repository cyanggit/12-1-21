class MyDog():

    def __init__(self, breed, name, age, color, is_asleep=False):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.is_asleep = is_asleep

    def walk(self):
        return print("{} is walking!".format(self.name))

    def eat(self):
        return print("{} is eating food!".format(self.name))

    def sleep(self):
        self.is_asleep = True
        return print("Buddy is sleeping!")

dog = MyDog("shiba", "Buddy", 1, "dirty red")
dog.walk()
dog.eat()
print(dog.sleep())