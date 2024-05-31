# ###

# יצירת מערך תלת מימדי עם פרטים על קוביה

# להבין איך אני עושה הכפלה במטריצה שמסובבת את הקובייה

# להדפיס על ידי הטלה על תת מרחב דו מימדי
# לאתחל דו מימד, וכל מקום לשים תו רווח ואז לעבור נקודה נקודה בתלת מימדי, ולהטיל. זה נותן לי נקודה על המישור
# ואני יכול לחשב גם מרחק. אז אני אכתוב את המרחק הזה בדו מימד.
# אם כבר יש מספר אז רק אם אני קטן יותר אני אכתוב. ככה יישמרו רק הנקודות הקרובות ביותר 
# ###




# הבעיה היא המיקומים
# צריך שהצורה תהיה ממורכזת תאורטית, כלומר אוסף הנקודות יהיה כזה שממורכז סביב איזו נקודה, ואז צריך גם שההכנסה למערך תעשה את זה במרכזו













import numpy as np
import math
import os
import time
size = 16
x_offset = 0
y_offset = 0
z_offset = 0
k1 = 100
X,Y,Z = (0,1,2)
def generate_r_matrix(axis, theta):
    if axis == 'x':
        return np.matrix([[1   ,     0                 ,0],
                          [0,np.cos(theta),-np.sin(theta)],
                          [0,np.sin(theta),np.cos(theta) ]])
    elif axis == 'y':
        return np.matrix([[np.cos(theta)   ,0 ,np.sin(theta)],
                          [0,       1,                     0],
                          [-np.sin(theta), 0, np.cos(theta) ]])
    
    elif axis == 'z':
        return np.matrix([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0 , 0,  1 ]])
    else:
        return None
def create_stick():
    return [np.array([30,30,30]), np.array([30,30,30])]
    # return [np.array([k1+i,1,k1*2]) for i in range(1, size)]

def project_points(points, width, height):
    screen = [[float('inf') for j in range(width)] for i in range(height)]

    for point in points:
        new_x = point[X]*k1/point[Z]
        new_y = point[Y]*k1/point[Z]
        screen[math.floor(point[X]*k1/point[Z])][math.floor(point[Y]*k1/point[Z])] = '@'
    return screen

def center_of_mass(points):
    return np.mean(points)

def rotate(points, rotate_matrix):
    c_o_m = center_of_mass(points)
    for i in range(len(points)):
        points[i] = points[i] - c_o_m
        points[i] = np.dot(rotate_matrix, points[i])
        points[i] = points[i] + c_o_m


def show_screen(screen):
    print("start")
    for row in screen:
        for char in row:
            if char == float('inf'):
                print(' ', end = '')
            else:
                print(char, end = '')
        print()

r_x_theta = generate_r_matrix('x' , np.pi/3)
r_y_theta = generate_r_matrix('y' , np.pi/6)
r_z_theta = generate_r_matrix('z' , np.pi/3)
r_matrix = r_x_theta*r_y_theta*r_z_theta
points = create_stick()


while True:
    screen = project_points(points,100,100)
    os.system('cls')
    show_screen(screen)
    rotate(points, r_matrix)
    time.sleep(1)
    break


# while(True):
#     # project_points_on_surface()
#     # rotate_points()
#     # clear_screen()
#     None


def rotate():
    None
    #need to multiply every vector by matrices

def project():
    None
    #need to create a 2d board representation, in a logical way. every cell is a tuple: (distance, angle) figure out about the angle
    #then go through vectors, every vector gives us a 2d point, distance, and angle.
    #then to make sure that the color is determined by the angle. if its more perpendicular to light source then brighter


















    # [np.array([0+x_offset,i+y_offset,size]) for i in range(size)] + [np.array([i+x_offset,size+y_offset,size]) for i in range(size)] +[np.array([size+x_offset,i+y_offset,size]) for i in range(size)] +[np.array([i+x_offset,0+y_offset,size]) for i in range(size)] +[np.array([0+x_offset,0+y_offset,i]) for i in range(size)] +[np.array([0+x_offset,size+y_offset,i]) for i in range(size)] +[np.array([size+x_offset, 0+y_offset, i]) for i in range(size)] +[np.array([size+x_offset, size+y_offset, i]) for i in range(size)] +[np.array([0+x_offset, i+y_offset, 0]) for i in range(size)] +[np.array([i+x_offset, size+y_offset, 0]) for i in range(size)]  +[np.array([size+x_offset, i+y_offset, 0]) for i in range(size)] 
