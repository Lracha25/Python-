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

# Hide the turtle and display the result
heart.hideturtle()
turtle.done()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)