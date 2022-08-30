from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.position = float(0)
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for n in range(3):
            self.add_segment()

    def add_segment(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setposition(self.position, 0)
        self.position += -20
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment()

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            co_or = self.snake_body[seg_num - 1].position()
            self.snake_body[seg_num].goto(co_or)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
