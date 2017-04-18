import matplotlib.pyplot as plt
import numpy as np
plt.title("Better Phase Plane Practice")
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.axis([-100, 100, -100, 100])
plt.grid(True)
ax = plt.axes()
Coefficient_Matrix=np.array([[2, 1], [-1, 1]])
MAGNITUDE=5 #How long we want each arrow to be
def distance(start, end):
    return ((start[0]-end[0])**2+(start[1]-end[1])**2)**0.5
def get_vector(point):
    return np.dot(Coefficient_Matrix, point)
point = [1, 3] #Randomly chosen point
step = 1
count=0
while point[0] < 100 and point[1] < 100 and step < 50 and step > 0.0001 and count < 100:
    vector = get_vector(np.array(point))
    calc_point = point
    point = vector
    count+=1
    step = distance(calc_point, vector)
    change = MAGNITUDE/step
    relative_x1, relative_x2 = (calc_point[0]+vector[0])*change, (calc_point[1]+vector[1])*change
    ax.arrow(calc_point[0], calc_point[1], relative_x1, relative_x2, width=0.00001, head_width=2, head_length=3)
plt.show()