import turtle

# Create a turtle object
heart = turtle.Turtle()

# Set the speed of the turtle
heart.speed(1)

# Draw a heart shape
heart.begin_fill()
heart.fillcolor('red')
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

# Write the text
heart.penup()
heart.goto(-100, -220)
heart.color('black')
heart.write("I LOVE PYTHAGOREAN THEOREM", font=("Arial", 20, "bold"))

# Hide the turtle and display the result
heart.hideturtle()
turtle.done()