# Import
from time import sleep
from painutilities import *

# Funktion Kapitel 3
def exec_chapter3(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        # Entscheidung: Aus der Falle raus klettern oder nicht
        in_der_falle = benutzer_zahl_eingabe([1, 2], 'Soll ich versuchen raus zu klettern? (1) oder soll ich es lassen? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Aus der Falle raus klettern
        if in_der_falle == 1:
            
            print('Ich sollte versuchen hier raus zu kommen\n')
            sleep(short_delay)
            print('Ich hab es fast geschafft\n')
            sleep(short_delay)
            print('AAAAAAAHHHHH ich bin runtergefallen\n')
            sleep(short_delay)
            print('Ich habe mich verletzt\n')
            sleep(short_delay)
            print('Ich komme hier wohl nie wieder raus :(\n')
            sleep(short_delay)
            print('Erzähler: 4 Stunden Später \n')
            sleep(long_delay)
            print('Erzähler: Penarrow war ohnmächtig und wurde von einer unbekannten Spezies gerettet\n')
            sleep(long_delay)
            print('Penarrow: Wo bin ich? Wer seit ihr?\n')
            sleep(short_delay)
            print('Erzähler: Was Penarrow gerade sieht: Gestalten kamen auf ihn zu die ganz und gar nicht nach Menschen aussahen\n')
            sleep(long_delay)
            print('Sie hatten riesige blaue Augen und spitze Ohren\n')
            sleep(short_delay)
            print('Außerdem hatten sie kurze Hosen an und einen viel zu großen Hoodie drüber\n')
            sleep(long_delay)
            print('Fearens: Wir sind Faerens. Wir haben dich gerettet. Du bist in einer unserer Fallen getreten\n')
            sleep(long_delay)
            print('Wir haben dir ein Gemisch aus Kräutern gegeben damit deine Wunden schneller heilen\n')
            sleep(long_delay)
            print('Penarrow: Und wieso sind meine Hände blau?!?\n')
            
            # Enter und Konsole clearen
            nextstep()
            
            print('Wir haben ein Ritual durchgeführt und dadurch wissen wir alles was du weißt. Sonst könnten wir deine Sprache nicht\n')
            sleep(long_delay)
            print('Und das mit den blauen Händen ist nur ein kleiner Nebeneffekt der aber sehr schnell wieder verschwindet\n')
            sleep(long_delay)
            print('Penarrow: Wie könnt ihr hier nur überleben in kurzen Hosen?!\n')
            sleep(short_delay)
            print('Es sind doch -55 Grad\n')
            sleep(short_delay)
            print('Faerens: Wir sind Faerens. Wir kennen keine Kälte oder wie ihr die Abwesenheit von Wärme nennt\n')
            sleep(short_delay)
        
        # Aus der Falle nicht raus klettern
        elif in_der_falle == 2:
            
            print('Erzähler: 4 Stunden später\n')
            sleep(long_delay)
            print('Es kam eine seltsame Gestalt zu der Falle und sah Penarrow\n')
            sleep(short_delay)
            print('Die Gestalt hatte ungewöhnlich große blaue Augen und spitze Ohren\n')
            sleep(short_delay)
            print('Außerdem hatten sie nur eine kurze Hose an mit einem viel zu großem Hoodie drüber\n')
            sleep(short_delay)
            print('Plötzlich holte sie eine Art Pfeife raus und aktivierte sie\n')
            sleep(short_delay)
            print('Erzähler: Durch den ziemlich schrillen Ton war Penarrow ohnmächtig geworden\n')
            sleep(short_delay)
            print('Penarrow: Wo bin ich? Wer seit ihr?\n')
            sleep(short_delay)
            print('Fearens: Wir sind Faerens. Wir haben dich gerettet. Du bist in einer unserer Fallen getreten\n')
            sleep(long_delay)
            print('Penarrow: Und wieso sind meine Hände blau?!?\n')
            sleep(short_delay)
            print('Wir haben ein Ritual durchgeführt und dadurch wissen wir alles was du weißt. Sonst könnten wir deine Sprache nicht\n')
            sleep(long_delay)
            print('Und das mit den blauen Händen ist nur ein kleiner Nebeneffekt der aber sehr schnell wieder verschwindet\n')
            sleep(long_delay)
            print('Penarrow: Wie könnt ihr hier nur überleben in kurzen Hosen?!\n')
            sleep(short_delay)
            print('Es sind doch -55 Grad\n')
            sleep(short_delay)
            print('Faerens: Wir sind Faerens. Wir kennen keine Kälte oder wie ihr die Abwesenheit von Wärme nennt\n')
            sleep(short_delay)
            
            # Enter und Konsole clearen
            nextstep()
        
    # Englisch
    elif sprache == 2:
        # Entscheidung: Aus der Falle raus klettern oder nicht
        in_the_trap = benutzer_zahl_eingabe([1, 2], 'Should I try to climb out? (1) or should I just wait here? (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Aus der Falle raus klettern
        if in_the_trap == 1:
            
            print('I should atleast try getting out of here\n')
            sleep(short_delay)
            print('Almost made it\n')
            sleep(short_delay)
            print('AAAAAAAHHHHH i fell\n')
            sleep(short_delay)
            print('Damnit I got hurt\n')
            sleep(short_delay)
            print('Seems like i wont be getting out of here any time soon:(\n')
            sleep(short_delay)
            print('Narrator: 4 hours later \n')
            sleep(long_delay)
            print('Narrator: Penarrow got unconscious and was carried away by an unknown species\n')
            sleep(long_delay)
            print('Penarrow: Where am I? Who are you?\n')
            sleep(short_delay)
            print('Narrator: From Penarrows point of view there were some creatures around him that didnt look like humans in the slightest\n')
            sleep(long_delay)
            print('They had giant blue eyes and pointy ears\n')
            sleep(short_delay)
            print('Their clothing was manly made out of some shorts and a clearly oversized hoodie\n')
            sleep(long_delay)
            print('Fearens: We are Faerens. We saved you. You walked into our trap\n')
            sleep(long_delay)
            print('We gave you a mixture of our plants to heal your wounds faster\n')
            sleep(long_delay)
            print('Penarrow: Thank you but...why are my hands blue?!?\n')
            
            # Enter und Konsole clearen
            nextstep()
            
            print('We went throught a ritual so that we know what you know. Otherwise we would not know your language\n')
            sleep(long_delay)
            print('Those blue hands are just a minor side effect but it should pass after a while\n')
            sleep(long_delay)
            print('Penarrow: How are you able to survive in this cold just wearing those shorts?!\n')
            sleep(short_delay)
            print('Its like -55 degrees out there\n')
            sleep(short_delay)
            print('Faerens: We are Faerens. We do not know the cold or even the warmth that you seem to prefer\n')
            sleep(short_delay)
        
        # Aus der Falle nicht raus klettern
        elif in_the_trap == 2:
            
            print('Narrator: 4 hours later\n')
            sleep(long_delay)
            print('A strange creature came closer to Penarrow and noticed the trap\n')
            sleep(short_delay)
            print('The creature had big blue eyes and pointy ears\n')
            sleep(short_delay)
            print('It was also wearing nothing but shorts and a oversized hoodie\n')
            sleep(short_delay)
            print('It suddenly pulled out some type of whistle and blew into it\n')
            sleep(short_delay)
            print('Narrator: The sound of the whistle made Penarrow pass out\n')
            sleep(short_delay)
            print('Penarrow: Where am I? Who are you?\n')
            sleep(short_delay)
            print('Fearens: We are the Faerens. We saved you. You stepped into our trap.\n')
            sleep(long_delay)
            print('Penarrow: And why in the world are my hands blue?!?\n')
            sleep(short_delay)
            print('We have gone through a ritual to know what you know. Otherwise we would not know your language\n')
            sleep(long_delay)
            print('And the blue hands are just a minor side effect but it should be gone after a while\n')
            sleep(long_delay)
            print('Penarrow: How are you able to survive in those shorts?!\n')
            sleep(short_delay)
            print('Isnt it like -55 degrees\n')
            sleep(short_delay)
            print('Faerens: We are Faerens. We do not know what the cold is or that warmth which you seem to prefer\n')
            sleep(short_delay)
            
            # Enter und Konsole clearen
            nextstep()