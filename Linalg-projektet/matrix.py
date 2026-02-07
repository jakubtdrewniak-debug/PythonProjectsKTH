import numpy as np
import random
import time

from pointplacer import main
alpha = 0
omgivning = 25 
platta = 135 
unique_points = main()
#unique_points.remove(1)
n = len(unique_points)
A = np.zeros((n , n))
b = np.zeros((n, 1))


for i in range(0, n):
    """Skapar ekvationen för punkterna med z=0"""
    point = unique_points[i]
    if point[2] == 0:
        A[i, i] = 1
        b[i, 0] = platta
        
    else:
        adjacent_points = {"east": [point[0] - 1, point[1] , point[2]],
                           "west": [point[0] + 1, point[1] , point[2]],
                           "north": [point[0] , point[1] + 1 , point[2]],
                           "south": [point[0] , point[1] - 1 , point[2]],
                           "up": [point[0] , point[1] , point[2] + 1],
                           "down": [point[0] , point[1] , point[2] - 1]}
        adjacent_in = []
        adjacent_out = []
        for pair in adjacent_points.items():
            if pair[1] in unique_points:
                adjacent_in.append(pair)
            else:
                adjacent_out.append(pair)
        if len(adjacent_in) == 6:
            A[i, i] = 6
            for pair in adjacent_in:
                idx = unique_points.index(pair[1])
                A[i, idx] = -1
                b[i, 0] = 0
        
        if len(adjacent_in) == 5:
            A[i, i] = (6 + alpha)
            b[i, 0] = (alpha * omgivning)

            point_out = adjacent_out[0]
            symmetric_point = []
            if point_out[0] == "east":
                symmetric_point = adjacent_points["west"]
            elif point_out[0] == "west":
                symmetric_point = adjacent_points["east"]
            elif point_out[0] == "north":
                symmetric_point = adjacent_points["south"]
            elif point_out[0] == "south":
                symmetric_point = adjacent_points["north"]
            elif point_out[0] == "up":
                symmetric_point = adjacent_points["down"]
            elif point_out[0] == "down":
                symmetric_point = adjacent_points["up"]
            idx_symmetric = unique_points.index(symmetric_point)

            A[i, idx_symmetric] = -2
            for pair in adjacent_in:
                if not pair[1] == symmetric_point:
                    idx = unique_points.index(pair[1])
                    A[i, idx] = -1

        if len(adjacent_in) == 4:
            A[i,i] = (6 + alpha*2)
            b[i,0] = (2*alpha*omgivning)

            symmetric_points = []
            for point_out in adjacent_out:
                symmetric_point = []
                if point_out[0] == "east":
                    symmetric_point = adjacent_points["west"]
                elif point_out[0] == "west":
                    symmetric_point = adjacent_points["east"]
                elif point_out[0] == "north":
                    symmetric_point = adjacent_points["south"]
                elif point_out[0] == "south":
                    symmetric_point = adjacent_points["north"]
                elif point_out[0] == "up":
                    symmetric_point = adjacent_points["down"]
                elif point_out[0] == "down":
                    symmetric_point = adjacent_points["up"]
                symmetric_points.append(symmetric_point)
                idx_symmetric = unique_points.index(symmetric_point)

                A[i,idx_symmetric] = -2

            for point_in in adjacent_in:
                if not point_in in symmetric_points:
                    idx = unique_points.index(point_in[1])
                    A[i, idx] = -1
        if len(adjacent_in) == 3:
            A[i, i] = (6 + 3*alpha)
            b[i, 0] = (3*alpha*omgivning)
            
            symmetric_points = []
            for point_out in adjacent_out:
                symmetric_point = []
                if point_out[0] == "east":
                    symmetric_point = adjacent_points["west"]
                elif point_out[0] == "west":
                    symmetric_point = adjacent_points["east"]
                elif point_out[0] == "north":
                    symmetric_point = adjacent_points["south"]
                elif point_out[0] == "south":
                    symmetric_point = adjacent_points["north"]
                elif point_out[0] == "up":
                    symmetric_point = adjacent_points["down"]
                elif point_out[0] == "down":
                    symmetric_point = adjacent_points["up"]
                symmetric_points.append(symmetric_point)
                idx_symmetric = unique_points.index(symmetric_point)

                A[i,idx_symmetric] = -2

            """for point_in in adjacent_in:
                if not point_in in symmetric_points:
                    idx = unique_points.index(point_in[1])
                    A[i, idx] = -2"""

        if len(adjacent_in) == 2:
            A[i, i] = (2 + 4*alpha)
            b[i, 0] = (4*alpha*omgivning)

            symmetric_points = []
            for point_out in adjacent_out:
                symmetric_point = []
                if point_out[0] == "east":
                    symmetric_point = adjacent_points["west"]
                elif point_out[0] == "west":
                    symmetric_point = adjacent_points["east"]
                elif point_out[0] == "north":
                    symmetric_point = adjacent_points["south"]
                elif point_out[0] == "south":
                    symmetric_point = adjacent_points["north"]
                elif point_out[0] == "up":
                    symmetric_point = adjacent_points["down"]
                elif point_out[0] == "down":
                    symmetric_point = adjacent_points["up"]
                symmetric_points.append(symmetric_point)
                idx_symmetric = unique_points.index(symmetric_point)

                A[i,idx_symmetric] = -2

            """for point_in in adjacent_in:
                if not point_in in symmetric_points:
                    idx = unique_points.index(point_in[1])
                    A[i, idx] = -2"""

temperature_distribution = np.linalg.solve(A , b)

print(temperature_distribution)




                


        
         



"""start_time = time.time()

omgivning = 20
platta = 135

A = np.zeros((n , n))
for i in range(0,n):
    for j in range(0,n):
        A[i, j] = random.randint(0,6)
        

b = np.zeros((n, 1))
for i in range(0, n):
    b[i, 0] = random.randint(30,135)
    

 
x = np.linalg.solve(A, b)
print(x)
print("--- %s seconds ---" % (time.time() - start_time))"""
