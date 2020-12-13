from time import sleep
import turtle


# setup screen size
# making turtle object 
sc = turtle.Screen() 
# setup the screen size 
sc.setup(700,700) 

# You can create a custom turtle shape with this line
anne_coloured = 'images/anne.gif'
anne_grey = 'images/anne_g.gif'
sc.register_shape(anne_coloured)
sc.register_shape(anne_grey)
alex_coloured = 'images/alex.gif'
alex_grey = 'images/alex_g.gif'
sc.register_shape(alex_coloured)
sc.register_shape(alex_grey)
maria_coloured = 'images/maria.gif'
maria_grey = 'images/maria_g.gif'
sc.register_shape(maria_coloured)
sc.register_shape(maria_grey)
charles_coloured='images/charles.gif'
charles_grey ='images/charles.gif'
sc.register_shape(charles_coloured)
sc.register_shape(charles_grey)
##############################################
# 
# Task 1 - register every image in the images folder as above
 



# instatiate turtle objects like this 
anne = turtle.Turtle() 
alex = turtle.Turtle()
maria = turtle.Turtle()
charles = turtle.Turtle()
##############################################
# Task 2 - Instantite every player on the board as a
#          seperate turtle as shown above




# This is a basic blueprint for a character - A CLASS!
class Character:

    def __init__(self, name, gender, pic):
        self.name = name
        self.gender = gender
        self.image = pic
        # You need more attributes here
        ######################################
        # Task 3 - Add the attributes

        
# This is an example of how to instantiate a character
anne_c = Character("Anne", "female", anne_coloured)        # each player
alex_c = Character("Alex", "male", alex_coloured)          # will need you
maria_c = Character("Maria", "female", maria_coloured)     # to add more attributes
charles_c = Character("Charles", "male", charles_coloured) # to their instances
##############################################
# Task 4 - Instatiate every player using the Character Class



###############################################
# Task 5 - You can add each character to a list.
#          You need to add 24 in total for this game.
eachChar = [alex_c, anne_c, charles_c, maria_c]



###############################################
# The proceure to display the board
# Some of the first row has been completed for you
# Task 6 - You complete the rest

def layoutBoard():
    # The images are 112x160
    # Position each turtle / image like this
    anne.penup()
    anne.setposition(-290,200) # -290 is the left most of the screen
    # add each image to the screen like this
    anne.shape(anne_c.image)
    alex.penup() # do this between each image in order to not see lines
    alex.setposition(-178,200)
    alex.pendown() # Pen must come down before you add an image to the layout
    alex.shape(alex_c.image)
    maria.penup()
    maria.setposition(-66,200)
    maria.pendown()
    maria.shape(maria_c.image)
    charles.penup()
    charles.setposition(46,200)
    charles.pendown()
    charles.shape(charles_c.image)

    
####################################################################################
# Task 7 - The program selects a random person from the array

# Task 8 - create a game loop that runs allowing the user to ask the program
#          if there are players who have particular attributes. (maybe 5 questions)

# Task 9 - The program should loop through & check each
#          instantiated object for the attributes

# task 10 - grayscale the shape for the characters without
#           those attributes

# task 11 - each time the player asks a question, the program
#           could ask if the player wants to guess who the person is.
#           If all 5 questions are exhuasted and the guess is wrong,
#           the program/CPU wins.



layoutBoard() # I use the procedure here to display the board
alex_c.image = alex_grey # using this line, i change the image for a person
sleep(2)
layoutBoard() # as you can see if I display the board again, Alex's colour changes

