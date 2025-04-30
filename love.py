# contoh  kode love # 
# 1. Love
```python
import turtle
import math

def draw_heart(t, size):
    t.fillcolor("red")
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size, 200)
    t.left(120)
    t.circle(-size, 200)
    t.forward(size)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)

    draw_heart(t, 100)

    t.hideturtle()
    turtle.done()


if __name__ == "__main__":

    main()