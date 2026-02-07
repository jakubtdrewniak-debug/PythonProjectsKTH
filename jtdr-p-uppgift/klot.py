import numpy as np
import sys
import math
import os 
from enum import Enum
from tkinter import *  
from tkinter import ttk, messagebox
from PIL import Image
from tkinter.filedialog import asksaveasfile

class Klot:
    """Representerar klotet med angivgen radie."""
    def __init__(self, radie):
        self.radie = radie

    def beräkna_z(self ,  x, y):
        """Beräknar värdet av z med givna x- och y-koordinater på klotet. Returnerar värdet z som en float"""
        return math.sqrt(pow( self.radie , 2 ) - pow( x , 2 ) - pow( y , 2 ))

    def in_klot(self , x, y):
        """Kontrollerar att en given punkt finns i klotet"""
        return pow( self.radie , 2 ) - pow( x , 2 ) - pow( y , 2 ) >= 0


class Scen:
    """Representerar scenen som innehåller två objekt, i det här fallet klotet och ljuskällan"""
    def __init__(self, klot, x_0, y_0):
        """Konstruerar scenen och returnerar Exception i fall ljuskällan inte ligger på klotet."""
        self.klot = klot
        self.x_0 = x_0
        self.y_0 = y_0
        if not self.klot.in_klot(x_0 , y_0):
            raise Exception("Ljuskällan ligger inte på klotet")
        else:
            self.z_0 = self.klot.beräkna_z(x_0, y_0)

    def belysning_styrka(self,  x , y , z ):
        """Räknar ut belysningspunkter för angivna koordinater, tar in z för att beräkna belysningsstyrkan
        Returnerar ljus_styrka som en float och denna float representerar belysningsstyrkan. """
        return ( x * self.x_0 + y * self.y_0 + z * self.z_0 )/ pow( self.klot.radie , 2 )
    
    
class TextVisualisering:
    """Implementation av visualisering som använder terminalgrännsnittet. Sparar filer som textdokument."""
    antal_steg = 70

    def __init__(self, scen):
        """Konsturerar textvisualiseringen av scenen"""
        self.scen = scen

    def belysning_char(self, ljus_styrka ):
        """Räknar ut tecknet som ska skrivas ut med hjälp av värdet b som 
        representerar belysningsstyrkan. Skriver sedan ut olika tecken 
        beroende på bs värde."""
        if ljus_styrka <= 0:
            return 'M'
        elif 0 < ljus_styrka <= 0.3:
            return '*'
        elif 0.3 < ljus_styrka <= 0.5:
            return '+'
        elif 0.5 < ljus_styrka <= 0.7:
            return '-'
        elif 0.7 < ljus_styrka <= 0.9:
            return '.'
        elif 0.9 < ljus_styrka <= 1:
            return ' '    
        
    def scen_som_sträng(self):
        """Returnerar textrepresentationen av klotet som en lista av linjer"""
        result = []
        for y_s in reversed(range( 0 , self.antal_steg )):
            y = - self.scen.klot.radie + self.scen.klot.radie * y_s * 2 / ( self.antal_steg - 1 )
            linje = []
            for x_s in range( 0 , self.antal_steg ):
                x = - self.scen.klot.radie + self.scen.klot.radie * x_s * 2 / ( self.antal_steg - 1 )
                if self.scen.klot.in_klot( x , y ):
                    z = self.scen.klot.beräkna_z( x , y )
                    b = self.scen.belysning_styrka( x , y , z )
                    c = self.belysning_char(b)
                    linje.append(c)
                else: 
                    linje.append(self.belysning_char(0))
            result.append(" ".join(linje))
        return result   
    
    def utskrivning(self):
        """Skriver ut scenen i terminalen"""
        linjer = self.scen_som_sträng()
        for linje in linjer:
            print(linje)

    def spara_som_text(self):
        """Sparar textrepresentationen av klotet som en textfil"""
        with open("klot.txt" , "w", encoding="utf-8") as handle:
            for linje in self.scen_som_sträng():
                handle.write(linje)
                handle.write('\n')


class TkinterVisualisering:
    """Implementation av visualiseringen som använder tkinter som visualiseringslösning. Sparar den som en png-fil """
    canvas_size = 500
    radie = 100

    def __init__(self):
        """Konstuerar visualiseringsobjekt med angiven scen, Använder värdet canvas_size för att initialisera tkinter canvas"""
        self.klot = Klot(self.radie)
        master = Tk()
        master.title("Klot")
        message = Label(master, text="Välj ljuskällan")
        message.pack(side=TOP)
        self.canvas = Canvas(master,
                        width = self.canvas_size,
                        height = self.canvas_size,
                        background="#202020")
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind("<Button>", self.teckna)
        self.canvas.create_oval(0, 0, self.canvas_size, self.canvas_size, outline="#ffffff")
        knapp = Button(master,
                       text = "Spara som fil",
                       command = self.spara_som_bild)
        knapp.pack(anchor = "s" , side = "right")
        mainloop()

    def färg(self, b ):
        """Räknar ut färgen för angiven belysningsstryrka använder värdet b 
        för att måla in pixlar på klotet med olika nyanser för att 
        representera ljuset"""
        if b <= 0:
            return "#000000"
        else:
            result = ["#"]
            b_256 = (int)(b * 255)
            for i in range(0, 3):
                result.append(f"{b_256:02x}")
            return "".join(result)
        
    def teckna(self , event):
        """Skapar ett klot och målar in den med hjälp av tkinter. Tar 
        ljuskällan från en click-event."""
        self.canvas.create_oval(0, 0, self.canvas_size, self.canvas_size, outline="#000000")
        x_0 = 2 * self.klot.radie * event.x / self.canvas_size - self.klot.radie
        y_0 = 2 * self.klot.radie * (self.canvas_size - event.y) / self.canvas_size - self.klot.radie
        if self.klot.in_klot(x_0, y_0):
            scen = Scen( self.klot , x_0 , y_0 )
            #print(z_0)
            for y_c in range(0, self.canvas_size + 10):
                y = - self.klot.radie + self.klot.radie * (self.canvas_size - y_c) * 2 / (self.canvas_size - 1)
                #y = - self.klot.radie + self.klot.radie * y_c * 2 / (self.canvas_size - 1)
                for x_c in range(0, self.canvas_size + 10 ):
                    x = - self.klot.radie + self.klot.radie * x_c * 2 / (self.canvas_size - 1)
                    if self.klot.in_klot( x , y ):
                        z = self.klot.beräkna_z( x, y )
                        b = scen.belysning_styrka( x, y , z )
                        c = self.färg( b )
                        #print(x, y, b, c)
                        self.canvas.create_oval(x_c, y_c, x_c + 1 , y_c + 1, outline=c)
                    else:
                        self.canvas.create_rectangle(x_c, y_c, x_c + 1 , y_c + 1, outline="#202020" , fill = "#202020") 

    def spara_som_bild(self):
        """Sparar TkInter canvas som en png fil"""
        files = [("PNG", "*.png")]
        path = asksaveasfile(filetypes = files , defaultextension= files, initialfile= "klot.png")
        tempfile = path.name + '.eps'
        self.canvas.postscript(file = tempfile)
        bild = Image.open(tempfile)
        bild.save(path.name, 'png')
        os.remove(tempfile)
        messagebox.showinfo(title=None, message= "Filen har sparats!")
        


class App:
    """Representerar fungerande programmet med grafiskt eller text visualisation"""
    def __init__(self):
        """Skapar klassen för programmet"""
    def run(self, visualiserings_typ):
        """Metoden som startar programmet med angiven visualiseringsmetod"""
        if visualiserings_typ == Alternativ.TEXT:
            radie = float(input("Ange klotets radie: "))
            klot = Klot(radie)
            x_0 = float(input("Ange ljuskällans x-koordinat: "))
            y_0 = float(input("Ange ljuskällans y-koordinat: "))
            scen = Scen(klot, x_0, y_0)
            vis = TextVisualisering(scen)
            vis.utskrivning()
            while True:
                val = input("Vill du spara klotet som en fil? Ja/Nej: ")
                if val == "Ja":
                    vis.spara_som_text()
                    break
                elif val == "Nej":
                    break
                else:
                    print("Svara 'Ja' eller 'Nej' ")
        if visualiserings_typ == Alternativ.GRAFISKT:
            vis = TkinterVisualisering()


class Alternativ(Enum):
    """Hjälpklass för att underlätta anropet av huvudfunktionen"""
    GRAFISKT = 1
    TEXT = 2

def errormessage():
    """Printar ut det korrekta användingen av programmet i fall anvädaren matar in fel funktion i terminalen"""
    print("Alternativ för visualisering:"   
          "\n\t-t: Textritning"
          "\n\t-g: Grafisk ritning")

app = App()
"""Följande kod fungerar som en meny i terminalen"""
if len(sys.argv) == 1:
    while True:
        print("Alternativ för visualisering:"   
            "\n\t1: Textritning"
            "\n\t2: Grafisk ritning"
            "\n\t3: Avsluta programmet")
        val = input("\t")
        if val == "1":
            app.run(Alternativ.TEXT)
        elif val == "2":
            app.run(Alternativ.GRAFISKT)
        elif val == "3":
            break
        else:
            print("Fel val!")
elif len(sys.argv) == 2:
    if sys.argv[1] == "-t":
        app.run(Alternativ.TEXT)
    elif sys.argv[1] == "-g":
        app.run(Alternativ.GRAFISKT)
    else:
        errormessage() 
else:
    errormessage() 
        