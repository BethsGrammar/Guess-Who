from turtleImages import layoutBoard

# This is a basic blueprint for a character
class Character:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# This is an example of how to instantiate a character
anne = Character("Anne", "female")

# You can add each character to a list. You need to add 24 in total for this game.
eachChar = [anne]


# This code simply demonstrates how you can access attributes from each item/character stored in the list
for i in eachChar:
    print(f"{i.name} is {i.gender}")

