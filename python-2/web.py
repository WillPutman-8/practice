class Robot:

    def __init__(self, given_color, given_name, given_weight):
        self.name = given_name
        self.color = given_color
        self.weight = given_weight

    def introduce_self(self):
        print(f"Hello my name is {self.name}, I am a {self.color} robot, and I weigh {self.weight} lbs.")


r1 = Robot(given_weight=30, given_color="Red", given_name="Timmy")
r1.introduce_self()

r2 = Robot(given_name="Tommy", given_color="blue", given_weight=45)
r2.introduce_self()


class Person:
    def __init__(self, name, personality, is_sitting, own_robot):
        self.name = name
        self.personality = personality
        self.sit = is_sitting
        self.robot = own_robot

    def intro(self):
        if self.sit:
            stand = "sitting"
        else:
            stand = "standing"
        print(f"My name is {self.name}, I'm kind of a {self.personality},I am {stand} right now and "
              f"{self.robot.name} is my robot!")

    def change_positon(self):
        if self.sit:
            self.sit = False
        else:
            self.sit = True


p1 = Person(name="Alice", personality="Agressive", is_sitting=False, own_robot=r2)
p1.intro()
p1.change_positon()
p1.intro()

p2 = Person(name="Becky", personality="Talkative", is_sitting=True, own_robot=r1)
p2.intro()
p2.change_positon()
p2.intro()

