# Import
import os
from time import sleep

# Funktion zum clearen
def clearscreen():
    
    # Linux ähnliche Systeme
    if os.name == 'posix':                  
        os.environ['TERM'] = 'xterm-color'
        os.system('clear')
        
    # Windows
    elif os.name == 'nt':                   
        os.system('cls')

# Funktion mit Enter und clearen
def nextstep():
    input('Drücke "Enter" zum Fortfahren!\n')
    clearscreen() 

# Funktion um falsche Eingaben abzufangen
def benutzer_zahl_eingabe(eingabe_int_liste, frage_txt = "?: ", fehleingabe_txt = "Nochmal, bitte"):
    if len(eingabe_int_liste) < 2:
        raise ValueError("Parameter eingabe_int_liste muss mindestens zwei Elemente enthalten")
    eingabe_gueltig = False
    rueckgabe = 0

    while not eingabe_gueltig:
        eingabe = input(frage_txt)
        for i in eingabe_int_liste:
            try:
                rueckgabe = int(eingabe)
                if i == rueckgabe:
                    eingabe_gueltig = True
                    break
            except:
                eingabe_gueltig = False
                
        if not eingabe_gueltig:
            print(fehleingabe_txt)
            
    return rueckgabe

    