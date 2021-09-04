from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.traffic_car = []



    def build_car(self):
        # create every 6 chance a car to module the traffic
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-258,258)
            new_car.goto(280,random_y)
            self.traffic_car.append(new_car)

    def move_cars(self):
        for car in self.traffic_car:
            car.backward(STARTING_MOVE_DISTANCE)




