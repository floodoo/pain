# Import
from time import sleep
from painutilities import *
from asciiart import *

# Funktion Kapitel 2
def exec_chapter2(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Erzähler: Der Sturm hat zum Glück aufgehört\n')
        sleep(short_delay)
        print('Penarrow: Was ist das denn? Wo kommt der riesige Berg auf einmal her?\n')
        sleep(short_delay)
        print('Wo bin ich überhaupt?\n')
        sleep(short_delay)
    
    # Englisch
    elif sprache == 2:
        print('Narrator: Luckily the storm passed\n')
        sleep(short_delay)
        print('Penarrow: Whats this now? Where did that mountain come from?\n')
        sleep(short_delay)
        print('Where even am I?\n')
        sleep(short_delay)

# Funktion Kapitel 2A
def exec_chapter2A(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Ich sollte auf den Berg gehen, um mir eine besser Übersicht von dem ganzen hier zu machen\n')
        sleep(long_delay)
        print('4 Stunden später\n')
        sleep(long_delay)
        print('Endlich oben!\n')
        sleep(short_delay)
        print('Was ist das denn? Mir fehlen die Worte\n')
        sleep(short_delay)
        print('Erzähler: Was Penarrow gerade sieht ist eine antike Stadt, welche wunderschön ist\n')
        sleep(short_delay)
        
        # Stadt zeigen
        show_stadt()
        
        # Enter und Konsole clearen
        nextstep()
        
        print('Wo bin ich denn hier gelandet? Wie ist das denn hier hingekommen?\n')
        sleep(long_delay)
        
        # Entscheidung: Zur antiken Stadt gehen oder nicht
        zur_stadt_gehen = benutzer_zahl_eingabe([1, 2], 'Soll ich zur antiken Stadt hingehen? (1) oder soll ich weggehen? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Zur antiken Stadt hingehen
        if zur_stadt_gehen == 1:
            
            print('Ich sollte mal nachsehen was das hier ist!\n')
            sleep(short_delay)
            print('Es schein mehrere 100 Jahre alt zu sein oder älter\n')
            sleep(short_delay)
            print('AAAAAAAHHHHH\n')
            sleep(short_delay)
            print('Erzähler: Der Boden hatte sich aufgelöst und Penarrow ist in eine tiefe Grube gefallen\n')
            sleep(long_delay)
            print('Penarrow: Oh *piep* wie komme ich hier wieder raus?\n')
            sleep(short_delay)
            print('Hallo?! Hört mich jemand?!\n')
            sleep(short_delay)
             
        # Wieder weg gehen
        elif zur_stadt_gehen == 2:
            
            print('Ich sollte lieber wieder gehen\n')
            sleep(short_delay)
            print('AAAAAAAHHHHH\n')
            sleep(short_delay)
            print('Erzähler: Der Boden hatte sich aufgelöst und Penarrow ist in eine tiefe Grube gefallen\n')
            sleep(long_delay)
            print('Penarrow: Oh mist wie komme ich hier wieder raus?\n')
            sleep(short_delay)
            print('Hallo?! Hört mich jemand?!\n')
            sleep(short_delay)
            
    # Englisch
    elif sprache == 2:
        print('I should get ontop of the mountain for a better view of all this\n')
        sleep(long_delay)
        print('4 hours later\n')
        sleep(long_delay)
        print('Finally at the top!\n')
        sleep(short_delay)
        print('What the....I am in lack of words\n')
        sleep(short_delay)
        print('Narrator: What Penarrow is looking at is a beautiful antique town\n')
        sleep(short_delay)
        
        # Stadt zeigen
        show_stadt()
        
        # Enter und Konsole clearen
        nextstep()
        
        print('What have i stumbled upon? How did this get here?\n')
        sleep(long_delay)
        
        # Entscheidung: Zur antiken Stadt gehen oder nicht
        go_to_town = benutzer_zahl_eingabe([1, 2], 'Should I go towards the town? (1) or should I just walk away? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Zur antiken Stadt hingehen
        if go_to_town == 1:
            
            print('I should probably look after this!\n')
            sleep(short_delay)
            print('It seems to be roughly a hundred years old, maybe even older\n')
            sleep(short_delay)
            print('AAAAAAAAAAAAHH\n')
            sleep(short_delay)
            print('Narrator: The ground had loosen and Penarrow fell into a deep hole\n')
            sleep(long_delay)
            print('Penarrow: Oh crap, how am i going to get out of this now?\n')
            sleep(short_delay)
            print('Hello?! Anybody hear me?!\n')
            sleep(short_delay)
             
        # Wieder weg gehen
        elif go_to_town == 2:
            
            print('I should probably just leave it be\n')
            sleep(short_delay)
            print('AAAAAAAHHHHH\n')
            sleep(short_delay)
            print('Narrator: The ground had loosen and Penarrow fell into a deep hole\n')
            sleep(long_delay)
            print('Penarrow: Oh crap, how am i going to get out of this now?\n')
            sleep(short_delay)
            print('Hello?! Anybody hear me?!\n')
            sleep(short_delay)