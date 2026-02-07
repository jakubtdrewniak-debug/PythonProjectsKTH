from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
"""Börjar försöka med kod för punkt placering"""


RADIUS = 8
HEIGHT = 8
WIDTH = 4
LENGHT_HANDLE = 8
WIDTH_HANDLE = 4
NODE_DISTANCE = 1
CONTROL_POINT_COORD = 2 * RADIUS + LENGHT_HANDLE -1
"""kontrollvärde för att placera handtaget på ett korrekt ställe"""

def base_area_placer(rad: int, Wid: int):
    """"""
    node_list = []
    y_mid = rad
    x_mid = rad
    z_end = Wid
    for y in range(y_mid-rad,y_mid+rad):
        for x in range(x_mid-rad,x_mid+rad):
            if (y - y_mid)**2 + (x - x_mid)**2 < rad**2:
                for z in range(0,z_end):
                    node_list.append([x,y,z])
    print(len(node_list))
    return node_list


    
def placer_cylinder_shell(height: int, radius: int,  width: int):
    """Ändrade villkoret för radien för att eliminera fall 5 helt och hållet"""
    node_list = []
    y_mid = radius
    x_mid = radius
    for y in range(y_mid-radius,y_mid+radius):
        for x in range(x_mid-radius,x_mid+radius):
            if (radius-width)**2 < (y - y_mid)**2 + (x - x_mid)**2 < radius**2:
                for z in range(width, width + height):
                    node_list.append([x,y,z])
    print(len(node_list))
    return node_list


def placer_handle(height: int, radius: int,  width: int, handle_width: int, handle_length: int):
    node_list = []
    y_mid = radius
    x_start = 2*radius - width//2
    half_handle_width = handle_width//2
    z_mid = height - half_handle_width
    handle_length = handle_length
    for y in range(y_mid-half_handle_width, y_mid+half_handle_width):
        for x in range(x_start, x_start+handle_length):
            for z in range(z_mid-half_handle_width, z_mid+half_handle_width):
                node_list.append([x, y, z])
    print(len(node_list))
    return node_list

def main():

    list_points = [NODE_DISTANCE]
    list_points += base_area_placer(RADIUS, WIDTH)+placer_cylinder_shell(HEIGHT, RADIUS, WIDTH)+placer_handle(HEIGHT + WIDTH, RADIUS, WIDTH, WIDTH_HANDLE,LENGHT_HANDLE)
    unique_points = []
    for list in list_points:
        if list not in unique_points:
            unique_points.append(list)
    #print(unique_points)
    print(len(list_points))
    print(len(unique_points))
    plot(unique_points)
    return unique_points

def plot(node_list:list):
    fig = plt.figure()
    ax = plt.axes(projection ="3d")
    
    x_list = []
    y_list = []
    z_list = []
    del node_list[0]
    for element in node_list:
        x_list.append(element[0])
        y_list.append(element[1])
        z_list.append(element[2])
    x_list.append(CONTROL_POINT_COORD)
    y_list.append(CONTROL_POINT_COORD)
    z_list.append(0)
    #print(x_list)
    xa = np.array(x_list)
    ya = np.array(y_list)
    za = np.array(z_list)
    

    
    #print(xa)
    #print(type(xa)) 
    #print(ya)
    #print(za)   

    ax.scatter3D(xa,ya,za, color = "green")
    plt.title("simple 3D scatter plot")
    plt.show()


if __name__ == "__main__":
    main()
