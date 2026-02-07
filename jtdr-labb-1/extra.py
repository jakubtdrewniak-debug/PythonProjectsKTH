import random

import matplotlib.pyplot as plt
import numpy as np

glukos = float (input("Ditt glukosvärde första dagen: "))
insulin = float (input("Ditt insulin värde första dagen: "))
limit = float(input("Vilket HOMA-IR-värde ska programmet understiga: "))


HOMA = (glukos*insulin) / 22.5

if HOMA < limit: 
    print("HOMA-IR värdet är redan under begränsningen: {:.2f}".format (HOMA))
    

if glukos <= 0 or insulin <= 0 or HOMA  < limit: 
      print ("Angivna värden är inkorrekta.")
      exit(1)

i = 1

g_list =[]
i_list =[]
h_list =[]

while HOMA >= limit:

    HOMA = (glukos*insulin) / 22.5
    g_list.append(glukos)
    i_list.append(insulin)
    h_list.append(HOMA)
    print ("Dag {}: Glukos: {:.2f} mmol/L Insulin: {:.2f} mU/L HOMA-IR: {:.2f}".format(i , glukos, insulin , HOMA))
    rand = (random.random()-0.5 )/ 10
    glukos = glukos * (rand + 1)
    rand = (random.random() -0.5)/ 5
    insulin = insulin * (rand + 1)
    
    i = i+1

print("Glukosvärden: {}".format(g_list))
print("Insulinvärden: {}".format(i_list))
print("HOMA-IR värden: {}".format(h_list))

fig,ax= plt.subplots()
ax.plot(list(range (1,i)) ,g_list, label="Glukos")
ax.plot(list(range (1,i)) ,i_list, label="Insulin")
ax.plot(list(range (1,i)) ,h_list, label="HOMA-IR")
plt.legend()
plt.show()
