# Import
from time import sleep
from painutilities import *
import random

random_liste = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Funktion Kapitel 1
def exec_chapter1(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        print('Penarrow: Wir müssen uns beeilen! Wir gehen zu der nächsten Forschungsstation!\n')
        sleep(long_delay)
        print('Erzähler: Ob das die richtige Entscheidung war?\n')
        sleep(short_delay)
        print('Penarrow: LOS LOS LOS! BEEILUNG DER SCHNEESTURM KOMMT IMMER NÄHER!\n')
        sleep(short_delay)
        print('Erzähler: Sie liefen los, aber ausgerechnet jetzt war es so stürmisch, dass man nicht mal seine Hand vor Augen sehen konnte\n')
        sleep(long_delay)
        print('Penarrow: Hallo?! Wo seid ihr alle?! Oh verdammt\n')
        sleep(short_delay)
        
        # Entscheidung: Crew suchen oder nicht
        crew_suchen = benutzer_zahl_eingabe([1, 2], 'Soll ich die Crew suchen gehen? (1) oder suche ich sie nicht? (2): ')
        
        if crew_suchen == 1:
            
            # Konsole clearen
            clearscreen()
            
            print('Oh Mann! Ich muss sie suchen gehen\n')
            sleep(short_delay)
            print('Hallo? Wo seid ihr? HAAALLLOO?!\n')
            sleep(short_delay)
            print('Oh Mann! Ich hoffe es geht ihnen gut\n')
            sleep(short_delay)
            print('2 Stunden später\n')
            sleep(short_delay)
            
        # Die Crew nicht suchen
        elif crew_suchen == 2:
            
            # Konsole clearen
            clearscreen()
            
            print('Ich muss mich in Sicherheit begeben!\n')
            sleep(short_delay)
            print('Dumm nur, dass ich nicht weiß, wo ich bin\n')
            sleep(short_delay)
            
    # Englisch
    elif sprache == 2:
        print('Penarrow: We have to hurry! Let us go to the next research station!\n')
        sleep(long_delay)
        print('Narrator: Was that the right decision?\n')
        sleep(short_delay)
        print('Penarrow: GO GO GO! THE SNOW STORM IS GETTING CLOSER!\n')
        sleep(short_delay)
        print('Narrator: They started running but the Storm got worse and worse, to the point where they were not even able to see what was infront of them\n')
        sleep(long_delay)
        print('Penarrow: Hello?! Where is everybody?! God damnit.\n')
        sleep(short_delay)
        
        # Entscheidung: Crew suchen oder nicht
        search_crew = benutzer_zahl_eingabe([1, 2], 'Should I go look for the crew? (1) or not? (2): ')
        
        if search_crew == 1:
            
            # Konsole clearen
            clearscreen()
            
            print('Oh Man! I have to look for them\n')
            sleep(short_delay)
            print('Hello? Where are you? HEELLLOO?!\n')
            sleep(short_delay)
            print('Oh Man! I just hope that they are alright\n')
            sleep(short_delay)
            print('2 hours later\n')
            sleep(short_delay)
            
        # Die Crew nicht suchen
        elif search_crew == 2:
            
            # Konsole clearen
            clearscreen()
            
            print('I have to get into safety!\n')
            sleep(short_delay)
            print('But i have no clue where i am.\n')
            sleep(short_delay)
        
# Funktion Kapitel 1B
def exec_chapter1B(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Wir bleiben hier und warten den Sturm ab!\n')
        sleep(short_delay)
        print('Crew: Penarrow wir haben aber fast nichts mehr zu essen und wer weiss wie lange der Sturm geht\n')
        sleep(long_delay)
        print('Penarrow: Wir riskieren es!\n')
        sleep(short_delay)
        print('Schliesst alle Fenster und Türen und macht die Heizung an\n')
        sleep(short_delay)
        print('Crew: Sir wir haben kein Heizöl mehr, aber wir können noch den rest Feuerholz reinlegen\n')
        sleep(short_delay)
        
    # Englisch
    elif sprache == 2:
        print('Penarrow: Let us wait here til the storm passes!\n')
        sleep(short_delay)
        print('Crew: But Penarrow we are short on food and who knows how long the storm will last\n')
        sleep(long_delay)
        print('Penarrow: We shall risk it!\n')
        sleep(short_delay)
        print('Close all the doors and windows and light up the heater\n')
        sleep(short_delay)
        print('Crew: Sir we dont have any wood left but we could use the rest of our firewood\n')
        sleep(short_delay)

# Funktion Kapitel 1C
def exec_chapter1C(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Benutzt das letzte Feuerholz!\n')
        sleep(short_delay)
        print('Crew: Ja Sir\n')
        sleep(short_delay)
        print('Penarrow: Dann hoffen wir mal, dass es gut geht\n')
        sleep(short_delay)
        print('3 Tage später\n')
        sleep(long_delay)
        print('Crew: Sir wir haben kein Essen mehr und der Sturm scheint kein Ende zu haben was sollen wir tun?\n')
        sleep(short_delay)
        
    # Englisch
    elif sprache == 2:
        print('Penarrow: Use the last firewood!\n')
        sleep(short_delay)
        print('Crew: Yes Sir\n')
        sleep(short_delay)
        print('Penarrow: Then let us hope for the best.\n')
        sleep(short_delay)
        print('3 days later\n')
        sleep(long_delay)
        print('Crew: Sir we are out of food and the storm is still going, what do we do?\n')
        sleep(short_delay)
        
# Funktion Kapitel 1D
def exec_chapter1D(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: LOS LOS LOS Wir müssen zur Forschungsstation sonst verhungern wir!\n')
        sleep(short_delay)
        print('Crew: Sir die Tür klemmt, wir bekommen sie nicht auf\n')
        sleep(short_delay)
        print('Aus dem Weg ich mach das!\n')
        sleep(short_delay)
        print('Crew: Sir ich habe hier einen Bunsenbrenner gefunden\n')
        sleep(short_delay)
                
        print('Penarrow: Geil\n')
        sleep(short_delay)
        
        raus_kommen = (random.choice(random_liste))
        
        # Bunzenbrenner
            
        if raus_kommen <= 25:
            print('Gib den Bunsenbrenner her\n')
            sleep(short_delay)
            print('Oh Mist! Da ist ja kein Gas mehr drinne\n')
            sleep(short_delay)
            Art=text2art('Game   Over')
            print(Art)
        
        if raus_kommen >= 25:
            print('Gib den Bunsenbrenner her')
          
            sleep(short_delay)
            print('Crew: Hier, ich hoffe damit kommen wir aus diesem Schiff raus!\n')
            sleep(short_delay)
            print('Penarrow: Geschafft endlich Frei\n')
            sleep(short_delay)
            print('Brrrrr ist aber kalt hier\n')
            sleep(short_delay)
            print('Crew: Laut der Anzeige hier sind es -55 Grad hier\n')
            sleep(short_delay)
            print('Penarrow: Wir sollten uns beeilen bevor wir hier erfrieren!\n')
            sleep(long_delay)
            print('Erzähler: Sie liefen im Sturm los und versuchten die Forschungsstation zu finden.\n')
            sleep(long_delay)
            print('2 Stunden später\n')
            sleep(long_delay)
            print('Penarrow: Hallo?! HAALLOO?! Oh man\n')
            sleep(short_delay)
            print('Ich kann nichtmal meine Hand sehen was ist das für ein *piep*\n')
            sleep(short_delay)
            print('Ich habe meine Crew in diesem verdammten Sturm verloren\n')
            sleep(short_delay)
            
            # Entscheidung: Crew suchen oder nicht
            crew_suchen = int(input('Soll ich die Crew Suchen? (1) oder zur Forschungsstation gehen? (2): '))
            
            # Crew suchen
            if crew_suchen == 1:
                
                # Konsole clearen
                clearscreen()
                
                print('Oh Mann! Ich muss sie Suchen gehen\n')
                sleep(short_delay)
                print('Hallo? Wo seid ihr? HAAALLLOO\n')
                sleep(short_delay)
                print('Oh Mann! Ich hoffe es geht ihnen gut\n')
                sleep(short_delay)
                print('2 Stunden Später\n')
                sleep(short_delay)
                
            # Crew nicht suchen
            elif crew_suchen == 2:
                
                # Konsole clearen
                clearscreen()
                
                print('Ich muss mich in Sicherheit begeben!\n')
                sleep(short_delay)
                print('Dumm nur, dass ich nicht weiss wo ich bin\n')
                sleep(short_delay)
        
    # Englisch
    elif sprache == 2:
        print('Penarrow: Hurry to the research station or else we might starve!\n')
        sleep(short_delay)
        print('Crew: Sir the door is jammed, we are unable to get it open\n')
        sleep(short_delay)
        print('Out of my way, let me handle this!\n')
        sleep(short_delay)
        print('Crew: Sir I found a burner that might help us\n')
        sleep(short_delay)
        print('Penarrow: Awesome\n')
        sleep(short_delay)
        
        if raus_kommen <= 25:
            print('Give me the burner\n')
            sleep(short_delay)
            print('What the...there is no gas in this thing\n')
            sleep(short_delay)
            Art=text2art('Game   Over')
            print(Art)
        
        if raus_kommen >= 25:
            print('Hand me the burner\n')
        
        
            
            sleep(short_delay)
            print('Crew: Here, I hope this helps us get out of the ship!\n')
            sleep(short_delay)
            print('Penarrow: Finally! We are free!\n')
            sleep(short_delay)
            print('Brrrrr but its cold here\n')
            sleep(short_delay)
            print('Crew: The display shows -55 degrees right now\n')
            sleep(short_delay)
            print('Penarrow: We should hurry before we freeze to death!\n')
            sleep(long_delay)
            print('Narrator: They ran out into the storm to search for the research station.\n')
            sleep(long_delay)
            print('2 hours later\n')
            sleep(long_delay)
            print('Penarrow: Hello?! HEELLOO?! Oh man\n')
            sleep(short_delay)
            print('I cant even see my hand infront of my eyes what the [censored]\n')
            sleep(short_delay)
            print('I lost my crew in this damn storm\n')
            sleep(short_delay)
            
            # Entscheidung: Crew suchen oder nicht
            search_crew = benutzer_zahl_eingabe([1, 2], 'Should i look for the crew? (1) or go to the research station? (2): ')
            
            # Crew suchen
            if search_crew == 1:
                
                # Konsole clearen
                clearscreen()
                
                print('Oh Man! I have to look for them\n')
                sleep(short_delay)
                print('Hello? Where are you? HEELLLOO\n')
                sleep(short_delay)
                print('Oh Man! I hope that they are doing fine\n')
                sleep(short_delay)
                print('2 hours later\n')
                sleep(short_delay)
                
            # Crew nicht suchen
            elif search_crew == 2:
                
                # Konsole clearen
                clearscreen()
                
                print('I have to get into safety!\n')
                sleep(short_delay)
                print('But i have no clue where i am\n')
                sleep(short_delay)
