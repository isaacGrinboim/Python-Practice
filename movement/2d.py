
import numpy as np
import math
import os
import time
size = 60
X = 0
Y = 1
class Rotation_2d:
    def __init__(self):
        self.rotation_matrix = self.generate_r_matrix(np.pi/6)
        self.points = self.create_line()
            
    def generate_r_matrix(self, theta):
        return np.matrix([[np.cos(theta),-np.sin(theta)],
                        [np.sin(theta),np.cos(theta)]])

    def create_line(self):
        return [np.array([[i],[int(size/2)]]) for i in range(int(size/4),int(size*3/4+1))]

    def center_of_mass(self,points):
        return np.mean(points)

    def rotate(self):
        c_o_m = self.center_of_mass(self.points)
        for i in range(len(self.points)):
            self.points[i] = self.points[i] - c_o_m
            self.points[i] = np.dot(self.rotation_matrix, self.points[i])
            self.points[i] = np.round(self.points[i])
            self.points[i] = self.points[i] + c_o_m

    def correct_coordinates(self,point):
        x,y = point
        if x<0:
            x = 0
        if x >= size:
            x = size-1
        if y<0:
            y = 0
        if y >= size:
            y = size-1
        return math.floor(x),math.floor(y)
        
    def create_screen(self):
        screen = [[' ' for j in range(size)] for i in range(size)]
        for point in self.points:
            x,y = self.correct_coordinates(point)
            screen[x][y] = '@'
        return screen

    def show_screen(self,screen):
        for row in screen:
            for char in row:
                print(char, end = '')
            print()
    
    def play(self):
        for i in range(1000):
            os.system('cls')
            screen = self.create_screen()
            self.show_screen(screen)
            self.rotate()
            time.sleep(0.3)
    
rotation = Rotation_2d()
rotation.play()

            



