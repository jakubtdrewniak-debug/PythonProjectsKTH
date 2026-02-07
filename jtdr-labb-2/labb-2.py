from tkinter import *
from random import randint
import math

WIDTH = 400
HEIGHT = 300
EPSILON = 0.0001

# pixelerar x värden
def ntp(n: float) -> int:
    return int(n * WIDTH)

#pixelerar y värden
def ntpy(n: float) -> int:
    return int(n * HEIGHT)

#normaliserar värden från pixelnr
def ptn(p: tuple[int, int]) -> tuple[float, float]:
    return (p[0] / WIDTH , p[1]/ HEIGHT)

def ptn_r(p: tuple[int]) -> tuple[float]:
    return (p[0] / WIDTH , p[1]/ HEIGHT)

def rectangle(img, upper_left: tuple[float, float], lower_right: tuple[float, float], color: str):
    for x in range(ntp(upper_left[0]), ntp(lower_right[0])):
        for y in range(ntpy(upper_left[1]), ntpy(lower_right[1])):
            img.put(color, (x,y))

def ram(img, upper_left: tuple[float, float] , lower_right: tuple[float, float], thickness: int, color: str):
    for t in range(thickness):
        for x in range(ntp(upper_left[0]) + t, ntp(lower_right[0]) - t):
            img.put(color, (x , t + ntpy(upper_left[1])))
            img.put(color, (x , ntpy(lower_right[1]) - t)) 
        for y in range(ntpy(upper_left[1]) + t, ntpy(lower_right[1]) - t):
            img.put(color, (t + ntp(upper_left[0]), y))
            img.put(color, (ntp(lower_right[0]) - t, y)) 


def area_tr(a: tuple[float, float], b: tuple[float, float] , c: tuple[float, float]) -> float:
    a_x = ntp(a[0])
    a_y = ntpy(a[1])
    b_x = ntp(b[0]) 
    b_y = ntpy(b[1])
    c_x = ntp(c[0])
    c_y = ntpy(c[1]) 
    #beräknar avståndet mellan triangelns olika punkter
    dab = math.sqrt ( pow((a_x)-(b_x), 2) + pow((a_y)-(b_y), 2))
    dbc = math.sqrt ( pow((b_x)-(c_x), 2) + pow((b_y)-(c_y), 2))
    dac = math.sqrt ( pow((a_x)-(c_x), 2) + pow((a_y)-(c_y), 2))
    s = (dab + dbc + dac) / 2
    return math.sqrt(s* (abs(s-dab))*(abs(s-dbc))*(abs(s-dac)))

#ger instruktioner senare i triangel funktionen att inte printa ut pixlar som inte följer villkoret nedan
def isintriangle(a: tuple[float, float], b: tuple[float, float] , c: tuple[float, float], p: tuple[int, int]):
    area = area_tr(a, b, c)
    a_pbc = area_tr(ptn(p), b, c)
    a_apc = area_tr(a, ptn(p), c)
    a_abp = area_tr(a, b, ptn(p))
    return abs(area - a_abp - a_apc - a_pbc) < EPSILON
    


        
def triangle(img, a: tuple[float, float], b: tuple[float, float] , c: tuple[float, float], color: str):
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            if isintriangle(a, b, c, ( x, y )):
                img.put(color, ( x, y ))

def circle(img, o: tuple[float, float], r: float, color: str):
    
        sx = ntp(o[0])
        sy = ntpy(o[1])
        rk = ntpy(pow( r, 2))
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if pow( (x-sx) , 2) + pow( (y-sy), 2) <= rk:
                    img.put( color, (x, y))


def gran(img, upper_left: tuple[float, float], height: float, width: float, tcolor: str, bcolor : str):
    
    t_height = height * 0.2
    t_width = width * 0.1

    t_upper_left = (upper_left[0] + width * 0.45, upper_left[1] + height *0.8)
    t_lower_right =(t_upper_left[0] + t_width, t_upper_left[1] + t_height) 
    
    rectangle(img, t_upper_left, t_lower_right, tcolor)

    base_y = upper_left[1] + height *  0.8

    layers = 7 
    layer_height = ( height * 0.8) /  layers 

    for i in range(layers):

        top_y = base_y - (i + 1 + ((layers - i - 1) / (2* layers))) * layer_height 
        bottom_y = base_y - (( i * layer_height ) * 0.9 )
        current_width = width * ( 1- ( i / layers  ) )

        triangle(img,
                (upper_left[0] + (width - current_width) / 2, bottom_y),
                (upper_left[0] + (width + current_width) / 2, bottom_y), 
                (upper_left[0] + width / 2, top_y),
                bcolor)

            
            

def main(): 

    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=img, state="normal")
    rectangle(img, (0, 0.4), (1 , 1), "#2e6f40")
    rectangle(img, (0,0), (1, 0.4), "#90d5ff")
    circle(img, (0.1, 0.1), (1), "#ffed29")
    rectangle(img, (0.5, 0.35), (0.9, 0.8), "#be5103" )
    triangle(img, (0.45, 0.35),(0.95, 0.35),(0.7, 0.2), "#332216")
    rectangle(img,(0.55, 0.55) , (0.65, 0.8), "#ffffff" )
    rectangle(img, (0.7, 0.4), (0.85, 0.6), "#8fd9fb")
    ram(img, (0.7, 0.4), (0.85, 0.6), 3, "#6d3b07")
    gran(img, (0.05 , 0.15), (0.6), (0.4), "#583927" , "#06402b")

    mainloop()

if __name__ == "__main__":
    main()
    

  