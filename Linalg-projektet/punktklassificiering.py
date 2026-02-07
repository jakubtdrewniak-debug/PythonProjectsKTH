import numpy as np
epsilon = 0.1

"""Konceptet bakom punktklassificieringen är att ta in en lista med alla punkter 
och sedan skapa en ny lista som innehåller listor av de olika fall
Fall 0: Basplattan 
Fall 1-8: se dokumentet"""

"""Error codes:
error 1: case 3 occured in a point
error 2: case 6 occured in a point"""

"""Search function"""
def sok(t, v, element):
    if t == "linjar":
        x = np.array(element)
        print("x = " + str(x))
        for i in range(0, len(v), 1):
            print(i)
            y = np.array(v[i])
            print("y = " + str(y))
            if np.linalg.norm(y - x) < epsilon:
                return True 
            
        return False

def pointnum(point, num, d):
    point[num%3] = point[num%3] + ((-1)**(num//3))*d
    return point

def main():
    finallist = [[],[],[],[],[],[],[],[],[]]
    """Fixa listan"""
    with open('punkter.txt', 'r', encoding="utf-8") as handle:
        punktlista = handle.read().splitlines()
        # print(punktlista)
        d = float(punktlista[0])
        punktlista = punktlista[1:]
        for i in range(0, len(punktlista)):
            punktlista[i] = punktlista[i].split()
        for i in range(0, len(punktlista)):
            for j in range(3):
                punktlista[i][j] = float(punktlista[i][j])
            # print(punktlista[i])
    # print(punktlista)


    """Fall 0"""
    for point in punktlista:
        if point[0] == 0:
            finallist[0].append
            punktlista.remove(point)
    """Räkna antalet punkter som saknas av närliggande punkterna och lägger till de saknande"""
    """Antalet punkter som saknas = index"""

    templist = [[],[],[],[],[],[],[]] 
    for point in punktlista:
        antal = 0
        for i in range(6):
            for check in punktlista:
                x = np.array(check)
                y = np.array(pointnum(point, i, d))
                print(str(np.linalg.norm(x-y)))
                if np.linalg.norm(x-y) < epsilon:
                    antal += 1
                    point.append(y)

        print(antal)
        templist[antal].append(point)


    # for point in punktlista: #Might not work because of float point imprecision
    #     antal = 0
    #     if not sok("linjar", punktlista, [point[0]+d, point[1], point[2]]):
    #         antal += 1
    #         point.append([point[0]+d, point[1], point[2]])
    #     if not sok("linjar", punktlista, [point[0], point[1]+d, point[2]]):
    #         antal += 1
    #         point.append([point[0], point[1]+d, point[2]])
    #     if not sok("linjar", punktlista, [point[0], point[1], point[2]+d]):
    #         antal += 1
    #         point.append([point[0], point[1], point[2]+d])
    #     if not sok("linjar", punktlista, [point[0]-d, point[1], point[2]]):
    #         antal += 1
    #         point.append([point[0]-d, point[1], point[2]])
    #     if not sok("linjar", punktlista, [point[0], point[1]-d, point[2]]):
    #         antal += 1
    #         point.append([point[0], point[1]-d, point[2]])
    #     if not sok("linjar", punktlista, [point[0], point[1], point[2]-d]):
    #         antal += 1
    #         point.append([point[0], point[1], point[2]-d])
    #     print(antal)
    #     templist[antal].append(point)




    finallist[0].append(templist[0])
    finallist[1].append(templist[1])
    finallist[8].append(templist[5])
    """Min ide är att ta någon form av differens av närligande punkterna med centerpunkten för att skilja mellan fall"""

    """Testa att fall 3 inte händer"""
    for point in templist[2]:
        x = np.array(point[:2])
        a = np.array(point[3])
        b = np.array(point[4])
        if np.linalg.norm(a - x + b - x) < epsilon:
            print("error 1")
            finallist[3].append(point)
        else:
            finallist[2].append(point)
    
    """Skilja mellan de 2 fall med 3 saknade punkter"""
    for point in templist[3]:
        x = np.array(point[:2])
        a = np.array(point[3])
        b = np.array(point[4])
        c = np.array(point[5])
        if np.linalg.norm(a + b + c - (3 * x)) - 1 < epsilon:
            if np.linalg.norm(a + b  - (2 * x)) < epsilon:
                point[3:] = [point[5], point[3], point[4]]
            if np.linalg.norm(a + c  - (2 * x)) < epsilon:
                point[3:] = [point[4], point[3], point[5]]
            else:
                point[3:] = [point[3], point[5], point[4]]
            finallist[5].append(point)
        else:
            finallist[4].append(point)
    """Testa att fall 6 inte händer"""
    for point in templist[4]:
        x = np.array(point[:2])
        a = np.array(point[3])
        b = np.array(point[4])
        c = np.array(point[5])
        d = np.array(point[6])
        if np.linalg.norm(a + b + c + d - (4 * x)) < epsilon:
            print("error 2")
            finallist[6].append(point)
        else:
            if np.linalg.norm(a + b - (2 * x)) < epsilon:
                point[3:] = [point[5], point[6], point[3], point[4]]
            if np.linalg.norm(b + c  - (2 * x)) < epsilon:
                point[3:] = [point[3], point[6], point[4], point[5]]
            if np.linalg.norm(c + d  - (2 * x)) < epsilon:
                point[3:] = [point[3], point[4], point[5], point[6]]
            if np.linalg.norm(d + a  - (2 * x)) < epsilon:
                point[3:] = [point[4], point[5], point[3], point[6]]
            if np.linalg.norm(a + c  - (2 * x)) < epsilon:
                point[3:] = [point[4], point[6], point[5], point[3]]
            else:
                point[3:] = [point[3], point[5], point[4], point[6]]
            finallist[7].append(point)
    print("We have", str(len(finallist[0])), "of case 0")
    print("We have", str(len(finallist[1])), "of case 1")
    print("We have", str(len(finallist[2])), "of case 2")
    print("We have", str(len(finallist[3])), "of case 3")
    print("We have", str(len(finallist[4])), "of case 4")
    print("We have", str(len(finallist[5])), "of case 5")
    print("We have", str(len(finallist[6])), "of case 6")
    print("We have", str(len(finallist[7])), "of case 7")
    print("We have", str(len(finallist[8])), "of case 8")
                
        



        



        



if __name__ == "__main__":
    main()