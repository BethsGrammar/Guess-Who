import turtle

# You can create a custom turtle shape with this line
turtle.register_shape('images/anne.gif')


# instatiate turtle objects like this 
anne = turtle.Turtle() 
anne2 = turtle.Turtle()

def layoutBoard(): 
    # Position each turtle / image like this 
    anne.setposition(0,200)
    # add each image to the screen like this
    anne.shape('images/anne.gif')
    turtle.penup() # do this between each image in order to not see lines
    anne2.setposition(-200,200)
    turtle.pendown() # Pen must come down before you add an image to the layout
    anne2.shape('images/anne.gif')
