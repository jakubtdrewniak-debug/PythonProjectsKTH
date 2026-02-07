import sys


"""Skapar en global lista av alla ord från filen och tar bort mellanslag och \n"""
with open("/home/jtdrhome/projekt/jtdr-labb-4/ordlista.utf8.txt", "r", encoding="utf8") as handle:
    v = []
    for line in handle: 
        words = line.strip()
        v.append(words)
        
#print(v)


"""Returnerar True om word finns i v"""
def linear_search(v, word):
    return word in v

    
    
def binarsok(v, word):
    """Returnerar True om word finns i v.
    Denna implementation anvÃ¤nder binÃ¤rsÃ¶kning"""
    low = 0
    high = len(v) - 1
    while low <= high:
        mid = (low + high)//2
        if word < v[mid]:
            high = mid - 1
        elif word > v[mid]:
            low = mid + 1
        else:
            return True
    return False


#def testbinarsok():
#    for i in range(10):
#        v = list(range(i))
#        for j in range(i):
#            if not binarsok(v, j):
#                print("Jag hittade inte", j, "inuti", v)
#    print("Vi klarade alla tester.")


#if __name__ == '__main__':#
#    testbinarsok()



def br_search(v, target):
    """Returns True if the sorted list v contains target and False otherwise.
    Undefined behaviour if v is not sorted"""
    return _helper(v, 0, len(v), target)


def _helper(v, start, end, target):
    if start > end or start >= len(v):
        return False
    mid = (start+end) // 2
    if v[mid] == target:
        return True
    if v[mid] < target:
        return _helper(v, mid+1, end, target)
    else:
        return _helper(v, start, mid-1, target)

def kuperade_ord(v, sokfunktion):
    
    result = dict()
    for word in v: 
        matching_words = []
        kuperingar = []
        """Hittar alla möjliga kuperingar av ordet i en lista genom att skapa alla möjliga kombinationer"""
        for i in range(1, len(word)):
            first_part = word[:i]
            second_part = word[i:]
            kuperingar.append(second_part + first_part)
            """Söker alla kuperingar som finns på listan v"""
        for kupering in kuperingar: 
            if sokfunktion(v, kupering) and not kupering in result.keys():
                matching_words.append(kupering)
        """Lägger till de kuperingarna som finns på listan v"""
        if len(matching_words) > 0:
            result.update({word : matching_words})
    list_result = []
    """Skapar en lista av par, dvs orginella ord samt deras kuperingar i en gemensam lista"""
    for key in result.keys():
        list_result.append([key, result.get(key)[0]])
    return list_result


def print_result(word, result):
    """Formaterat utskrift av resultatet. """
    str = "Ditt ord: " + word + "\n" +  word + " finns"
    if not result: 
        str = str + " inte"
    print(str)



def menu():
    while True:
        
        print("1. Linjärsökning"
              "\n2. Binärsökning"
              "\n3. Rekursiv binärsökning"
              "\n4. Kuperade ord - Linjärsökning"
              "\n5. Kuperade ord - Binärsökning"
              "\n6. Kuperade ord - Rekursiv binärsökning"
              "\nAnnan input.  Avsulta programmet")
        option = input("Ange ditt val: ")
        if option.isnumeric(): 
            numoption = int(option)
            if 1 <=  numoption <= 3: 
                word = input("Ange ett ord att hitta: ")
                if numoption == 1:
                    print_result(word, linear_search(v,word))
                elif numoption == 2: 
                    print_result(word, binarsok(v,word))
                elif numoption == 3: 
                    print_result(word, br_search(v,word))
            elif 4 <= numoption <= 6:
                if numoption == 4:
                    print(kuperade_ord(v, linear_search)) 
                elif numoption == 5:
                    print(kuperade_ord(v, binarsok)) 
                elif numoption == 6:
                    print(kuperade_ord(v, br_search))
            else:
                print("Felaktig val, programmet avsultas. Ditt val: " + option)
                break 
        else:
            print("Felaktigt val, programmet avsultas. Ditt val: " + option) 
            break
            

menu()


    



#hittad_kupering = kuperade_ord(v, br_search)
#print (hittad_kupering)



    
#def test_br_search():
#    TEST_SIZE = 10
#    for length in range(TEST_SIZE):
#        v = []
#        for i in range(length):
#            v.append(i)
#        for current in v:
#            assert br_search(v, current)
#        assert not br_search(v, TEST_SIZE)
#    return True


#if __name__ == '__main__':
#    if test_br_search():
#        print("All tests passed")


#def main():
 #   if linear_search == True:


