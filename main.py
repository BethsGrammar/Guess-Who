import turtle

turtle.register_shape('images/anne.gif')
# turtle object 
anne = turtle.Turtle() 
anne2 = turtle.Turtle()
# changing the cursor 
# shape to cirlce 
#anne.shape('images/anne.gif')
anne.setposition(0,200)
anne.shape('images/anne.gif')
anne2.setposition(-200,200)
anne2.shape('images/anne.gif')


# Instantiate each turtle with a custom shape

# Place each turtle on the screen next to one another

# Instantiate each character based on their attributes

# add each object to an array possibly

# The program selects a random person from the array

# create a game loop that runs allowing the user to ask the program
# if there are players who have particular attributes. (maybe 5 questions)

# The program should check each instantiated object for the attributes

# grayscale the shape for the characters without those attributes

# each time the player asks a question, the program could ask if the player
# wants to guess who the person is.
# If all 5 questions are exhuasted and the guess is wrong, the program/CPU wins.