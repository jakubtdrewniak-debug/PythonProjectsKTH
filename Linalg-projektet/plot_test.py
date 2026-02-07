from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def read_file():
    node_lists = []
    with open("test_punkt.txt", "r", encoding= "utf8") as handle:
        node_lists = handle.read().splitlines()
    return node_lists

def base_gen(rad, Wid): 
    """Genererar punkter"""
    node_list = []
    y_mid = rad
    x_mid = rad
    z_end = Wid
    for y in range(y_mid-rad,y_mid+rad):
        for x in range(x_mid-rad,x_mid+rad):
            if (y - y_mid)**2 + (x - x_mid)**2 <= rad**2:
                for z in range(0,z_end):
                    node_list.append([x,y,z])
    return node_list

def placer_cylinder_shell(height: int, radius: int,  width: int):
    """"""
    node_list = []
    y_mid = radius
    x_mid = radius
    for y in range(y_mid-radius,y_mid+radius):
        for x in range(x_mid-radius,x_mid+radius):
            if (radius-width)**2 < (y - y_mid)**2 + (x - x_mid)**2 <= radius**2:
                for z in range(width, width + height):
                    node_list.append([x,y,z])
    return node_list

def plot(node_list:list):
    fig = plt.figure()
    ax = plt.axes(projection ="3d")
    
    x_list = []
    y_list = []
    z_list = []

    for element in node_list:
        x_list.append(element[0])
        y_list.append(element[1])
        z_list.append(element[2])

    print(x_list)
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

def main():
    #node_list = read_file()
    #print(node_list)
    #print(node_list[0])
    #print((node_list[0])[0])

    plot(placer_cylinder_shell(7,50,5))

if __name__ == "__main__":
    main()