'''class computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


com1 = computer('i5', 16)
com2 = computer('ryzen', 8)


com1.config()
com2.config()
'''


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.initialAge = age
        else:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.age < 13):
            print("You are young.")
        elif(13 <= self.age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        return self.age


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
