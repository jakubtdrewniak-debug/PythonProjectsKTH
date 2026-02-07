import random

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

while HOMA >= limit:

    HOMA = (glukos*insulin) / 22.5
    print ("Dag {}: Glukos: {:.2f} mmol/L Insulin: {:.2f} mU/L HOMA-IR: {:.2f}".format(i , glukos, insulin , HOMA))
    rand = (random.random()-0.5 )/ 10
    glukos = glukos * (rand + 1)
    rand = (random.random() -0.5)/ 5
    insulin = insulin * (rand + 1)
    
    i = i+1