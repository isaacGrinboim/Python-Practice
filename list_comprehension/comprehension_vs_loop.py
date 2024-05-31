import time
import matplotlib.pyplot as plt
mult = 10000
num_points = 100*mult
def comp(n):
    start = time.time()
    lst = [i for i in range(n)]
    end = time.time()
    return end-start

def loop(n):
    start = time.time()
    lst = []
    for i in range(n):
        lst.append(i)
    end = time.time()
    return end-start

x_vec = [i for i in range(num_points)]
loop_vec = [loop(i) for i in range(num_points-5, num_points)] 
comp_vec = [comp(i) for i in range(num_points-5, num_points)]
y_vec = [round(i/j,3) for i,j in zip(loop_vec,comp_vec)]
print(y_vec)