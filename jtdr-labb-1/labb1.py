systolic = int (input("Vad är ditt systoliska blodtryck?  ")) 
diastolic = int (input("Vad är ditt diastoliska blodtryck?  "))

print ( "Ditt blodtryck är",systolic,"/" , diastolic, "mmHg" )
if systolic >180 or diastolic > 90:
    print ("Du har hypertensiv kris.")

elif 140 <= systolic or  90 <= diastolic:
    print ("Du har hypertoni stadium 2.")

elif 130 <= systolic < 140 or 90 > diastolic:
    print ("Du har hypertoni stadium 1.")

elif 120 <= systolic < 130 and 80 <= diastolic:
    print ("Ditt blodtryck är förhöjt.")

elif   120 > systolic  and 80 > diastolic:
    print ("Ditt blodtryck är normalt.")