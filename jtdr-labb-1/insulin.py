import random

glukos = float (input("Ditt glukosvärde första dagen: "))
insulin = float (input("Ditt insulin värde första dagen: "))
dagar = int(input("Hur många dagar ska simulationen köras? "))

if glukos <= 0 or insulin <= 0 or dagar <= 0: 
      print ("Angivna värden är inkorrekta.")
      exit(1)

for i in range(dagar):
    HOMA = (glukos*insulin) / 22.5
    print ("Dag {}: Glukos: {:.2f} mmol/L Insulin: {:.2f} mU/L HOMA-IR: {:.2f}".format(i+1 , glukos, insulin , HOMA))
    rand = (random.random()-0.5 )/ 10
    glukos = glukos * (rand + 1)
    rand = (random.random() -0.5)/ 5
    insulin = insulin * (rand + 1)


