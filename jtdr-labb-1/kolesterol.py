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
        