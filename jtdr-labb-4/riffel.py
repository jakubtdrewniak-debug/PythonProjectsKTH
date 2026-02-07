"""Halverar kortleken och returnerar en blandad kortlek"""
def riffel_blandning(kort):
    halv = len(kort)//2
    blandade_kort = []
    for i in range(halv):
        blandade_kort.append(kort[i])
        blandade_kort.append(kort[halv + i])
    return blandade_kort 

def antal_riffel(antal_kort):
    start = list(range(antal_kort))
    """Skapar en shallow copy"""
    nuvarande = start[:]
    riffel_antal = 0
    while True: 
        nuvarande = riffel_blandning(nuvarande)
        riffel_antal += 1
        #print(nuvarande)
        if nuvarande == start: 
            break
    return riffel_antal



antal_kort = int(input("Ange ett jämnt antal kort att blanda: "))
"""Saniterar input"""
if antal_kort %2 == 0:
    riffel = antal_riffel(antal_kort)
    print("Det kommer ta {} stycken riffelblandningar för att komma till startpunkten.".format(riffel))
else:
    print("Du måste ange ett jämnt antal kort.")



    