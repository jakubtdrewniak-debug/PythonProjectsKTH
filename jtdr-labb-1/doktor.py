systolic = int (input ("Vad är ditt systoliska blodtryck?  ")) 
diastolic = int (input ("Vad är ditt diastoliska blodtryck?  "))

print ( "Ditt blodtryck är",systolic,"/" , diastolic, "mmHg" )
if systolic > 180 or diastolic > 90:
    print ("Du har hypertensiv kris.")

elif 140 <= systolic or  90 <= diastolic:
    print ("Du har hypertoni stadium 2.")

elif 130 <= systolic < 140 or 90 < diastolic:
    print ("Du har hypertoni stadium 1.")

elif 120 <= systolic < 130 and 80 <= diastolic:
    print ("Ditt blodtryck är förhöjt.")

elif   120 > systolic  and 80 > diastolic:
    print ("Ditt blodtryck är normalt.")


# Kolesterol

HDL = float (input ("Skrin in ditt HDL-kolesterolvärde: "))
LDL = float (input ("Skriv in ditt LDL-kolesterolvärde: "))
TRI = float (input ("Skriv in ditt triglicerinvärde: "))

VLDL = TRI / 5

print ("HDL-värde (mmol/L):", HDL)

print ("LDL-värde (mmol/L):", LDL)

print ("Triglicerinvärde (mmol/L):", TRI)

total = HDL + LDL + VLDL 


print("Totalt kolesterol: {:.2f} mmol/L".format(total))

if 4 <= LDL: 
    print ("LDL-kolesterolvärdet är för högt.")
    
if 7 <= total:
        print ("Kolesterolvärdet är mycket högt.")

elif 7 > total >= 6: 
        print ("Kolesterolvärdet är högt.")

elif 6 > total >= 5: 
        print ("Kolesterolvärdet är förhöjt.")

elif 5 > total: 
        print ("Kolesterolvärdet är normalt.")

# Insulin

import random

glukos = float (input("Ditt glukosvärde första dagen: "))
insulin = float (input("Ditt insulin värde första dagen: "))
dagar = int(input("Hur många dagar ska simulationen köras? "))

HOMA = (glukos*insulin) / 22.5

print ("Glukos: {:.2f} mmol/L".format(glukos) , "Insulin: {:.2f} mU/L".format(insulin), "HOMA-IR: {:.2f}".format(HOMA))

