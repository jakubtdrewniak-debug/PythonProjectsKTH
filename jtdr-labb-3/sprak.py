import sys

def sprak_input(message):
    ord = input(message)
    return ord

def stjarnsprak2(inrad):
    """Returnerar inrad där vartannat tecken är en stjärna. Denna
    implementation är mer effektiv eftersom den använder en förändringsbar
    lista och inte längre och längre strängobjekt som är oföränderliga."""
    letters = ["*"]
    for tkn in inrad:
        letters.append(tkn)
        letters.append("*")
    return "".join(letters)

vokaler = ['A','E','I','O','U','Y','Å','Ä','Ö','a','e','i','o','u','y','å','ä','ö']


def visksprak(inrad):
    letters = [] 
    for tkn in inrad:
        if not tkn in vokaler:
            letters.append(tkn)
    return "".join(letters)

def rovarsprak(inrad):
    letters = []
    for tkn in inrad: 
        letters.append(tkn)
        if tkn not in vokaler and tkn.isalnum():
            letters.append("o")
            letters.append(tkn)
    return "".join(letters)

def rovarsprak2(inrad):
    letters = []
    removeletters = 0
    for tkn in inrad:
        if not tkn.isalnum():
            letters.append(tkn)
        elif removeletters  == 0 and tkn not in vokaler:
            letters.append(tkn)
            removeletters = 1
        elif removeletters == 1: 
            removeletters = 2
        elif removeletters == 2:
            removeletters = 0
        else: 
            letters.append(tkn)
    return "".join(letters)
            
def bebissprak(inrad):
    words = inrad.split(" ")
    #print(words)
    result = []
    for word in words:
        letters = []
        """Bygger ord till första vokalen"""
        for tkn in word:
            letters.append(tkn)
            if tkn in vokaler:
                break
        
        bebisword = []
        """Repeterar de första boksträver 3 gånger, bokstav efter bokstav"""
        for i in range(3):
            for letter in letters: 
                bebisword.append(letter)
        #print(bebisword)
        result.append("".join(bebisword))
    #print(" ".join(result))
    return " ".join(result)

def allsprak(inrad):
    
    all= ['a','l','l']
    words = inrad.split(" ")
    result = []
    for word in words:
        före_vokal = []
        efter_vokal = []
        vokalen_hittad = False
        for tkn in word: 
            if tkn in vokaler:
                vokalen_hittad = True
            if vokalen_hittad:
                efter_vokal.append(tkn)
            else:
                före_vokal.append(tkn)
    #    print(före_vokal)
    #    print(efter_vokal)
        efter_vokal.extend(före_vokal)
        efter_vokal.extend(all)
    #    print(efter_vokal)
        result.append("".join(efter_vokal))
    #print(result)
    return " ".join(result)


def fikonsprak(inrad):
    fi = ['f', 'i']
    kon = ['k','o','n']
    words = inrad.split(" ")
    result = []
    for word in words:
        före_vokal = []
        efter_vokal = []
        vokalen_hittad = False

        for tkn in word: 
            if vokalen_hittad:
                efter_vokal.append(tkn)
            else:
                före_vokal.append(tkn)
            if tkn in vokaler:
                vokalen_hittad = True
    #    print(före_vokal)
    #    print(efter_vokal)
        fikonword = []
        fikonword.extend(fi)
        fikonword.extend(efter_vokal)
        fikonword.extend(före_vokal)
        fikonword.extend(kon)       
    #    print(efter_vokal)
        result.append("".join(fikonword))
    #print(result)
    return " ".join(result)            
            

def menu():
    while True:
        print("Välj språk: "
            "\n\t1. Stjärnspråket"
            "\n\t2. Viskspråket"
            "\n\t3. Rövarspråket"
            "\n\t4. Översätt rövarspråket"
            "\n\t5. Bebispråket"
            "\n\t6. Allspråket"
            "\n\t7. Fikonspråket"
            "\n\t8. Avsluta ")
        option = input("Ange ditt val: ")
        if not option.isnumeric():
            print("Inkorrekt val. Välj en siffra mellan 1 och 8")
            continue
        option = int(option)
        
        if option == 8:
            break
        if  1 <= option <= 7:
            inrad = sprak_input("Ange en sträng att översätta: ")
            if option == 1:
                print(stjarnsprak2(inrad))
            elif option == 2:
                print(visksprak(inrad))
            elif option == 3:
                print(rovarsprak(inrad))
            elif option == 4:
                print(rovarsprak2(inrad))
            elif option == 5:
                print(bebissprak(inrad))
            elif option == 6:
                print(allsprak(inrad))
            elif option == 7:
                print(fikonsprak(inrad))
        else:
            print("Inkorrekt val.")






#print(ord)
#print(sys.argv[0])
#print(len(sys.argv))
#print(rovarsprak2(ord))

def errormessage():
    print("Alternativ för terminalkommandon: "   
         # "\n echo \"<Sträng att översätta>\" | python3 sprak.py -<språk>"
          "\n\t-s: Stjärnspråket"
          "\n\t-v: Viskspråket"
          "\n\t-r: Rövarspråket"
          "\n\t-ö: Översätt rövarspråket"
          "\n\t-b: Bebispråket"
          "\n\t-a: Allspråket"
          "\n\t-f: Fikonspråket")

if len(sys.argv) == 1: 
    menu()
else:
    while True:
        try:

            ord = sprak_input("")
            if len(sys.argv) != 2:
                errormessage()    
            elif sys.argv[1] == "-s":
                print(stjarnsprak2(ord))
            elif sys.argv[1] == "-v":
                print(visksprak(ord))
            elif sys.argv[1] == "-r":
                print(rovarsprak(ord))
            elif sys.argv[1] == "-ö":
                print(rovarsprak2(ord))
            elif sys.argv[1] == "-b":
                print(bebissprak(ord))
            elif sys.argv[1] == "-a":
                print(allsprak(ord))
            elif sys.argv[1] == "-f":
                print(fikonsprak(ord))
            else:
                errormessage() 
        except EOFError:
            break



