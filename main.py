# Penarrows Adventure in Nowhere (P.A.I.N.)
# Charakter: Penarrow
# Stadt: Nowhere
# Stadtspezies: Faeren //Wie Dobby's in Harry Potter// 
# Sprache: Nowherianisch

# Import
from time import sleep
from art import *
from painutilities import*
from vorstory import *
from chapter1 import *
from chapter2 import *
from chapter3 import *
from chapter4 import *
from chapter5 import *
from chapter6 import *
from asciiart import *

# Verzögerungen für alles
DELAY_SHORT_S = 3
DELAY_LONG_S = 6

# Sprachauswahl

# Konsole clearen
clearscreen()

# Spieletitel anzeigen
Art=text2art('Welcome   to   P.A.I.N')
print(Art)

# Entscheidung: Deutsch oder Englisch
sprache_wahl = benutzer_zahl_eingabe([1, 2], 'Willst du die Geschichte auf Deutsch? (1) or do you want the Story in English? (2): ')

# Konsole clearen
clearscreen()

# Deutsche Story
if sprache_wahl == 1:
    
    # Konsole clearen
    clearscreen()
    
    # Vorstory überspringen oder nicht
    vorstory_ueberspringen = benutzer_zahl_eingabe([1, 2], 'Willst du zuerst etwas über die Geschichte erfahren (1) oder gleich mit dem Abenteuer anfangen (2): ')
    
    # Konsole clearen
    clearscreen()
    
    # Vorstory überspringen
    if vorstory_ueberspringen == 1:
        
        # Starte Vorstory
        exec_vorstory(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Enter und Konsole clearen
        nextstep()
    
    # Entscheidung: Zur Forschungsstation gehen oder nicht
    sturm_anfang = benutzer_zahl_eingabe([1, 2], 'Möchtest du zu einer nahegelegenden Forschungsstation gehen? (1) oder möchtest du im Schiff bleiben? (2): ')
    
    # Konsole clearen
    clearscreen()
    
    # Zur Forschungsstation gehen
    if sturm_anfang == 1:
        
        # Konsole clearen
        clearscreen()
        
        # Kapitel 1A
        exec_chapter1(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Kapitel 2
        exec_chapter2(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Entscheidung: Auf dem Berg ein Überblick verschaffen oder nicht
        berg_ueberblick = benutzer_zahl_eingabe([1, 2], 'Soll ich auf den Berg gehen um mir einen Überblick zu verschaffen? (1) oder weitergehen? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Auf dem Berg einen Überblick verschaffen
        if berg_ueberblick == 1:
            
            # Kapitel 2A
            exec_chapter2A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Kapitel 3
            exec_chapter3(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Kapitel 4
            exec_chapter4(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Entscheidung: Das Ritual machen oder nicht
            ritual_durchfuehren = benutzer_zahl_eingabe([1, 2], 'Willst du das Ritual machen (1) oder nicht (2): ')
            clearscreen()
            
            # Das Ritual machen
            if ritual_durchfuehren == 1:
                
                # Kapitel 5
                faehigkeit = exec_chapter5(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Entscheidung zu kämpfen oder ab zu hauen
                kaempfen = benutzer_zahl_eingabe([1, 2], 'Willst du kämpfen (1) oder Feige sein und abhauen (2)?: ')
                
                # Konsole clearen
                clearscreen()
                
                # kämpfen
                if kaempfen == 1:
                    
                    # Kapitel 5A
                    exec_chapter5A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Entscheidung: Soll Penarrow nach Hause gehen oder nicht
                    bleiben = benutzer_zahl_eingabe([1, 2], 'Soll Penarrow bei den Faerens bleiben (1) oder nach Hause gehen? (2): ')
                    
                    # Konsole clearen
                    clearscreen()
                    
                    # Bei den Faerens bleiben
                    if bleiben == 1:
                        
                        # Gewonnen
                        print('Penarrow: Ich werde bei euch bleiben und euch weiterhin beschützen\n')
                        sleep(DELAY_SHORT_S)
                        print('Erzähler: Er blieb bis an sein Lebensende bei den Faerens und beschütze sie\n')
                        sleep(DELAY_SHORT_S)
                        
                        # Riesiger Text
                        Art=text2art('Game   gewonnen')
                        print(Art)
                        sleep(DELAY_SHORT_S)
                        show_winner()
                        
                        
                    # Nach Hause gehen
                    elif bleiben == 2:
                        
                        # Kapitel 6
                        exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                        
                        # Entscheidung: Soll Penarrow den Heiltrank nehmen oder nicht
                        faehigkeit_verlieren = benutzer_zahl_eingabe([1, 2], 'Soll ich die Heilmischung trinken (1) und meine Fähigkeit verlieren oder es nicht tun (2): ')
                        
                        # Konsole clearen
                        clearscreen()
                        
                        # Heilmischung trinken
                        if faehigkeit_verlieren == 1:
                            
                            # Kapitel 6A
                            exec_chapter6A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                            
                        #Verlieren
                        elif faehigkeit_verlieren == 2:
                            Art=text2art('Game   Over')
                            print(Art)
                            
                # Nicht kämpfen
                elif kaempfen == 2:
                    print('Du rennst weg und lässt alle im Stich')
                    sleep(DELAY_SHORT_S)
                    
                    # Riesiger Text
                    Art=text2art('Game   Over')
                    print(Art)
            
            # Das Ritual nicht machen
            if ritual_durchfuehren == 2:
                
                # Kapitel 5B
                exec_chapter5B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Kapitel 6
                exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
        # Keinen Überblick verschaffen
        elif berg_ueberblick == 2:
            
            # Konsole clearen
            clearscreen()
            
            print('Du verirrst dich\n')
            sleep(DELAY_SHORT_S)
            
            # Riesiger Text
            Art=text2art('Game   Over')
            print(Art)
            
    # Im Schiff bleiben
    elif sturm_anfang == 2:
        
        # Konsole clearen
        clearscreen()
        
        # Kapitel 1B
        exec_chapter1B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Entscheidung: Holz zum Heizen benutzen oder nicht
        feuerholz_benutzen = benutzer_zahl_eingabe([1, 2], 'Soll ich das Holz zum Heizen benutzen (1) oder nicht? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Holz benutzen
        if feuerholz_benutzen == 1:
            
            # Kapitel 1C
            exec_chapter1C(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Entscheidung: Im Sturm zur Forschungsstation gehen oder nicht
            zur_forschungsstation = benutzer_zahl_eingabe([1, 2], 'Sollen wir im Sturm zur Forschungsstation gehen (1) oder nicht (2): ')
            
            # Konsole clearen
            clearscreen()
            
            # Zur Forschungsstation gehen
            if zur_forschungsstation == 1:
                
                # Kapitel 1D
                exec_chapter1D(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Kapitel 2
                exec_chapter2(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
        
                # Entscheidung: Auf dem Berg ein Überblick verschaffen oder nicht
                berg_ueberblick = benutzer_zahl_eingabe([1, 2], 'Soll ich auf den Berg gehen um mir einen Überblick zu verschaffen? (1) oder weitergehen? (2): ')
                
                # Konsole clearen
                clearscreen()
        
                # Auf dem Berg einen Überblick verschaffen
                if berg_ueberblick == 1:
            
                    # Kapitel 2A
                    exec_chapter2A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Enter und Konsole clearen
                    nextstep()
                    
                    # Kapitel 3
                    exec_chapter3(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Enter und Konsole clearen
                    nextstep()
                    
                    # Kapitel 4
                    exec_chapter4(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Ritual durchführen oder nicht
                    ritual_durchfuehren = benutzer_zahl_eingabe([1, 2], 'Willst du das Ritual machen (1) oder nicht (2): ')
                    
                    # Konsole clearen
                    clearscreen()
                    
                    # Rital durchführen
                    if ritual_durchfuehren == 1:
                        
                        # Kapitel 5
                        exec_chapter5(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                        
                        # Entscheidung zu kämpfen oder ab zu hauen
                        kaempfen = benutzer_zahl_eingabe([1, 2], 'Willst du kämpfen (1) oder Feige sein und abhauen (2)?: ')
                        
                        # Kämpfen
                        if kaempfen == 1:
                    
                            # Kapitel 5A
                            exec_chapter5A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                            
                            # Entscheidung: Soll Penarrow nach Hause gehen oder nicht
                            bleiben = benutzer_zahl_eingabe([1, 2], 'Soll Penarrow bei den Faerens bleiben (1) oder nach Hause gehen? (2): ')
                            
                            # Konsole clearen
                            clearscreen()
                            
                            # Bei den Faerens bleiben
                            if bleiben == 1:
                                
                                print('Penarrow: Ich werde bei euch bleiben und euch weiterhin beschützen\n')
                                sleep(DELAY_SHORT_S)
                                print('Erzähler: Er blieb bis an sein Lebensende bei den Faerens und beschütze sie\n')
                                sleep(DELAY_SHORT_S)
                                
                                # Riesiger Text
                                Art=text2art('Game   gewonnen')
                                print(Art)
                                sleep(DELAY_SHORT_S)
                                show_winner()
                                
                                
                            # Nach Hause gehen
                            elif bleiben == 2:
                                
                                # Kapitel 6
                                exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                                
                                # Entscheidung: Soll Penarrow den Heiltrank nehmen oder nicht
                                faehigkeit_verlieren = benutzer_zahl_eingabe([1, 2], 'Soll ich die Heilmischung trinken (1) und meine Fähigkeit verlieren oder es nicht tun (2): ')
                                
                                # Konsole clearen
                                clearscreen()
                                
                                # Heilmischung trinken
                                if faehigkeit_verlieren == 1:
                                    
                                    # Kapitel 6A
                                    exec_chapter6A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                                    
                                #Verlieren
                                elif faehigkeit_verlieren == 2:
                                    Art=text2art('Game   Over')
                                    print(Art)
                        
                        # Nicht kämpfen
                        elif kaempfen == 2:
                            print('Du rennst weg und lässt alle im Stich')
                            sleep(DELAY_SHORT_S)
                            
                            # Riesiger Text
                            Art=text2art('Game   Over')
                            print(Art)
                        
                    # Ritual nicht durchführen
                    elif ritual_durchfuehren == 2:
                        
                        # Kapitel 5B
                        exec_chapter5B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
                # Keinen Überblick verschaffen
                elif berg_ueberblick == 2:
                    
                    # Konsole clearen
                    clearscreen()
                    
                    print('Du verirrst dich\n')
                    sleep(DELAY_SHORT_S)
                    
                    # Riesiger Text
                    Art=text2art('Game   Over')
                    print(Art)
            
                
            # Nicht zur Forschungsstation gehen
            elif zur_forschungsstation == 2:
                
                print('Ohne Essen geht es nicht\n')
                sleep(DELAY_SHORT_S)
                
                # Riesiger Text
                Art=text2art('Game   Over')
                print(Art)
        
        # Holz nicht benutzen
        elif feuerholz_benutzen == 2:
            
            print('Es ist zu kalt\n')
            sleep(DELAY_SHORT_S)
            
            # Riesiger Text
            Art=text2art('Game   Over')
            print(Art)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if sprache_wahl == 2:
    
    
# Konsole clearen
    clearscreen()
    
    # Vorstory überspringen oder nicht
    vorstory_ueberspringen = benutzer_zahl_eingabe([1, 2], 'Would you like to hear something about the Story (1) or start with the adventure right away (2): ')
    
    # Konsole clearen
    clearscreen()
    
    # Vorstory überspringen
    if vorstory_ueberspringen == 1:
        
        # Starte Vorstory
        exec_vorstory(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Enter und Konsole clearen
        nextstep()
    
    # Entscheidung: Zur Forschungsstation gehen oder nicht
    sturm_anfang = benutzer_zahl_eingabe([1, 2], 'Would you like to go to the next best research station (1) or stay inside the ship (2): ')
    
    # Konsole clearen
    clearscreen()
    
    # Zur Forschungsstation gehen
    if sturm_anfang == 1:
        
        # Konsole clearen
        clearscreen()
        
        # Kapitel 1A
        exec_chapter1(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Kapitel 2
        exec_chapter2(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Entscheidung: Auf dem Berg ein Überblick verschaffen oder nicht
        berg_ueberblick = benutzer_zahl_eingabe([1, 2], 'Should I go ontop of the mountain for a better view (1) or keep going (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Auf dem Berg einen Überblick verschaffen
        if berg_ueberblick == 1:
            
            # Kapitel 2A
            exec_chapter2A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Kapitel 3
            exec_chapter3(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Kapitel 4
            exec_chapter4(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Entscheidung: Das Ritual machen oder nicht
            ritual_durchfuehren = benutzer_zahl_eingabe([1, 2], 'Would you like to perform the ritual (1) or not(2): ')
            
            # Das Ritual machen
            if ritual_durchfuehren == 1:
                
                # Kapitel 5
                faehigkeit = exec_chapter5(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Entscheidung zu kämpfen oder ab zu hauen
                kaempfen = benutzer_zahl_eingabe([1, 2], 'Are you willing to fight (1) or are you going to run away (2)?: ')
                
                # Konsole clearen
                clearscreen()
                
                # kämpfen
                if kaempfen == 1:
                    
                    # Kapitel 5A
                    exec_chapter5A(sprache_wahl, faehigkeit, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Entscheidung: Soll Penarrow nach Hause gehen oder nicht
                    bleiben = benutzer_zahl_eingabe([1, 2], 'Should Penarrow stay with the Faerens (1) or should he go home? (2): ')
                    
                    # Konsole clearen
                    clearscreen()
                    
                    # Bei den Faerens bleiben
                    if bleiben == 1:
                        
                        # Gewonnen
                        print('Penarrow: I decided to stay with you and try to protect you all\n')
                        sleep(DELAY_SHORT_S)
                        print('Narrator: He stayed with the Faerens for the rest of hiw life and protected him\n')
                        sleep(DELAY_SHORT_S)
                        
                        # Riesiger Text
                        Art=text2art('Game   won')
                        print(Art)
                        sleep(DELAY_SHORT_S)
                        show_winner()
                        
                        
                    # Nach Hause gehen
                    elif bleiben == 2:
                        
                        # Kapitel 6
                        exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                        
                        # Entscheidung: Soll Penarrow den Heiltrank nehmen oder nicht
                        faehigkeit_verlieren = benutzer_zahl_eingabe([1, 2], 'Should he take the antidote and lose his abilities (1) or refuse (2): ')
                        
                        # Konsole clearen
                        clearscreen()
                        
                        # Heilmischung trinken
                        if faehigkeit_verlieren == 1:
                            
                            # Kapitel 6A
                            exec_chapter6A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                            
                        #Verlieren
                        elif faehigkeit_verlieren == 2:
                            Art=text2art('Game   Over')
                            print(Art)
                            
                # Nicht kämpfen
                elif kaempfen == 2:
                    print('You run away and leave everyone alone')
                    sleep(DELAY_SHORT_S)
                    
                    # Riesiger Text
                    Art=text2art('Game   Over')
                    print(Art)
            
            # Das Ritual nicht machen
            if ritual_durchfuehren == 2:
                
                # Kapitel 5B
                exec_chapter5B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Kapitel 6
                exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
        # Keinen Überblick verschaffen
        elif berg_ueberblick == 2:
            
            # Konsole clearen
            clearscreen()
            
            print('YOu get lost\n')
            sleep(DELAY_SHORT_S)
            
            # Riesiger Text
            Art=text2art('Game   Over')
            print(Art)
            
    # Im Schiff bleiben
    elif sturm_anfang == 2:
        
        # Konsole clearen
        clearscreen()
        
        # Kapitel 1B
        exec_chapter1B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
        
        # Entscheidung: Holz zum Heizen benutzen oder nicht
        feuerholz_benutzen = benutzer_zahl_eingabe([1, 2], 'Should I use the wood as a heat source (1) or not? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Holz benutzen
        if feuerholz_benutzen == 1:
            
            # Kapitel 1C
            exec_chapter1C(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
            # Entscheidung: Im Sturm zur Forschungsstation gehen oder nicht
            zur_forschungsstation = benutzer_zahl_eingabe([1, 2], 'Should we go to the research station during the storm (1) or not (2): ')
            
            # Konsole clearen
            clearscreen()
            
            # Zur Forschungsstation gehen
            if zur_forschungsstation == 1:
                
                # Kapitel 1D
                exec_chapter1D(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
                # Kapitel 2
                exec_chapter2(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                
        
                # Entscheidung: Auf dem Berg ein Überblick verschaffen oder nicht
                berg_ueberblick = benutzer_zahl_eingabe([1, 2], 'Should I go ontop of the mountain for a better view? (1) or not(2): ')
                
                # Konsole clearen
                clearscreen()
        
                # Auf dem Berg einen Überblick verschaffen
                if berg_ueberblick == 1:
            
                    # Kapitel 2A
                    exec_chapter2A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Enter und Konsole clearen
                    nextstep()
                    
                    # Kapitel 3
                    exec_chapter3(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Enter und Konsole clearen
                    nextstep()
                    
                    # Kapitel 4
                    exec_chapter4(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                    
                    # Ritual durchführen oder nicht
                    ritual_durchfuehren = benutzer_zahl_eingabe([1, 2], 'Would you like to perform the ritual (1) or not (2): ')
                    
                    # Konsole clearen
                    clearscreen()
                    
                    # Rital durchführen
                    if ritual_durchfuehren == 1:
                        
                        # Kapitel 5
                        exec_chapter5(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                        
                        # Entscheidung zu kämpfen oder ab zu hauen
                        kaempfen = benutzer_zahl_eingabe([1, 2], 'Are you willing to fight (1) or do you refuse and run away (2)?: ')
                        
                        # Kämpfen
                        if kaempfen == 1:
                    
                            # Kapitel 5A
                            exec_chapter5A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                            
                            # Entscheidung: Soll Penarrow nach Hause gehen oder nicht
                            bleiben = benutzer_zahl_eingabe([1, 2], 'Should Penarrow stay with the Faerens (1) or should he try to go home? (2): ')
                            
                            # Konsole clearen
                            clearscreen()
                            
                            # Bei den Faerens bleiben
                            if bleiben == 1:
                                
                                print('Penarrow: I decided that I will stay with you to protect you\n')
                                sleep(DELAY_SHORT_S)
                                print('Narrator: He stayed with the Faerens for the rest of his life\n')
                                sleep(DELAY_SHORT_S)
                                
                                # Riesiger Text
                                Art=text2art('Game   won')
                                print(Art)
                                sleep(DELAY_SHORT_S)
                                show_winner()
                                
                                
                            # Nach Hause gehen
                            elif bleiben == 2:
                                
                                # Kapitel 6
                                exec_chapter6(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                                
                                # Entscheidung: Soll Penarrow den Heiltrank nehmen oder nicht
                                faehigkeit_verlieren = benutzer_zahl_eingabe([1, 2], 'Should I drink the antidote and lose my abilities (1) or refuse and keep them (2): ')
                                
                                # Konsole clearen
                                clearscreen()
                                
                                # Heilmischung trinken
                                if faehigkeit_verlieren == 1:
                                    
                                    # Kapitel 6A
                                    exec_chapter6A(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
                        
                                #Verlieren
                                elif faehigkeit_verlieren == 2:
                                    Art=text2art('Game   Over')
                                    print(Art)
                        
                        # Nicht kämpfen
                        elif kaempfen == 2:
                            print('You run away and leave everyone alone')
                            sleep(DELAY_SHORT_S)
                            
                            # Riesiger Text
                            Art=text2art('Game   Over')
                            print(Art)
                        
                    # Ritual nicht durchführen
                    elif ritual_durchfuehren == 2:
                        
                        # Kapitel 5B
                        exec_chapter5B(sprache_wahl, DELAY_SHORT_S, DELAY_LONG_S)
            
                # Keinen Überblick verschaffen
                elif berg_ueberblick == 2:
                    
                    # Konsole clearen
                    clearscreen()
                    
                    print('You get lost\n')
                    sleep(DELAY_SHORT_S)
                    
                    # Riesiger Text
                    Art=text2art('Game   Over')
                    print(Art)
            
                
            # Nicht zur Forschungsstation gehen
            elif zur_forschungsstation == 2:
                
                print('It wont work without food\n')
                sleep(DELAY_SHORT_S)
                
                # Riesiger Text
                Art=text2art('Game   Over')
                print(Art)
        
        # Holz nicht benutzen
        elif feuerholz_benutzen == 2:
            
            print('Its too cold\n')
            sleep(DELAY_SHORT_S)
            
            # Riesiger Text
            Art=text2art('Game   Over')
            print(Art)
