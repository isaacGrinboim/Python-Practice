import os
import math
import time

class Ball:
    def __init__(self, location, velocity, acceleration, radius):
        self.radius = radius
        self.x = location[0]
        self.y = location[1]
        self.v_x = velocity[0]
        self.v_y = velocity[1]
        self.a_x = acceleration[0]
        self.a_y = acceleration[1]


class Frame:
    def __init__(self, height, width, initial_ball, delta_t):
        self.height = height
        self.width = width
        self.ball = initial_ball
        self.delta_t = delta_t
        self.picture = [[' ' for j in range(width)] for i in range(height)]
        if self.ball_is_in_range():
            self.picture[self.ball_x()][self.ball_y()] = '*'


    def move_ball(self):
        new_x, new_y = (self.ball.x + self.delta_t*self.ball.v_x + 0.5*self.ball.a_x**2 , self.ball.y + self.delta_t*self.ball.v_y + 0.5*self.ball.a_y**2)
        new_v_x, new_v_y = (self.ball.v_x + self.delta_t*self.ball.a_x, self.ball.v_y + self.delta_t*self.ball.a_y)
        if new_x <= 0 or new_x >= self.width:
            new_v_x = -new_v_x
        if new_y <= 0 or new_y >= self.height:
            new_v_y = -new_v_y
        if self.ball_is_in_range():
            self.picture[math.floor(self.ball_x())][math.floor(self.ball_y())] = ' '
        self.ball.x = new_x
        self.ball.y = new_y        
        self.ball.v_x = new_v_x
        self.ball.v_y = new_v_y
        if self.ball_is_in_range():
            self.picture[math.floor(self.ball_x())][math.floor(self.ball_y())] = '*'


    def print_frame(self):
        for j in range(self.width):
            for i in range(self.height):
                print(self.picture[i][j], end="")
            print('')
            

    def ball_is_in_range(self):
        return (self.ball.x >= 0 and self.ball.x  <= self.width) and (self.ball.y >= 0 and self.ball.y <= self.height) 
    
    def ball_x(self):
        return self.ball.x
    def ball_y(self):
        return self.ball.y
    
    def animate(self):
        
        while True:

            os.system('cls')
            self.print_frame()
            self.move_ball()
            time.sleep(0.2)
            


ball = Ball((7,7),(100,-1) , (0,2),1)
frame = Frame(20,20, ball, 0.05)
frame.animate()