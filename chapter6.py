# Import
from time import sleep
from painutilities import *
from art import *
from asciiart import *

# Funktion Kapitel 6
def exec_chapter6(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Ich werde heute noch aufbrechen und nach Hause gehen\n')
        sleep(short_delay)
        print('Faeren: Okay ich wünsche dir viel Glück auf deiner Rückreise\n')
        sleep(short_delay)
        print('Wir werden dir einen Rucksack mit Proviant und weiteren nützlichen Dingen mitgeben\n')
        sleep(long_delay)
        print('Penarrow: Ich danke euch\n')
        sleep(short_delay)
        print('Faeren: Ich hoffe wir sehen uns mal wieder\n')
        sleep(short_delay)
        print('Penarrow: Ich hoffe auch\n')
        sleep(short_delay)
        print('Erzähler: Penarrow lief los\n')
        sleep(short_delay)
        print('Nach 2 Stunden kam Penarrow zu einer riesigen Gletscherspalte\n')
        sleep(short_delay)
        print('Penarrow: Oh Mist! Ich muss hier rüber\n')
        sleep(short_delay)
        print('Aber wie soll ich das machen?!\n')
        sleep(short_delay)
        print('Die Faerens haben mir doch ein paar Sachen mitgegeben\n')
        sleep(short_delay)
        print('Ich sollte da mal nachschauen\n')
        sleep(short_delay)
        
        # Entscheiding: Kletterseil und Eispickel benutzen oder nicht
        rucksack = benutzer_zahl_eingabe([1, 2], 'Ich habe hier ein Kletterseil und zwei Eispickel. Soll ich sie benutzen? (1) oder nicht (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Benutzen
        if rucksack == 1:
            
            print('Ich kann das Seil ja mit dem Eispickel verbinden\n')
            sleep(short_delay)
            print('Und das eine Ende befestige ich hier bei mir\n')
            sleep(short_delay)
            print('Und das andere Ende werfe ich wie einen Enterhaken rüber und hoffe, dass er im Eis stecken bleibt\n')
            sleep(long_delay)
            print('Erzähler: Penarrow nahm Anlauf und warf den Eispickel rüber\n')
            sleep(short_delay)
            print('Penarrow: Ich hoffe, dass wird so lange halten, bis ich mit diesem Seil rüber geklettert bin\n')
            sleep(long_delay)
            print('Erzähler: Er fing an rüber zu klettern und als er ungefähr bei der Hälfte war,....\n')
            sleep(short_delay)
            print('löste sich das Seil und Penarrow fiel runter!!!\n')
            sleep(short_delay)
            print('Penarrow: AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH!!!! \n')
            sleep(short_delay)
            print('Erzähler: Penarrow wurde ohnmächtig, weil er sich verletzt hatte\n')
            sleep(short_delay)
            print('Nach einer Weile... \n')
            sleep(long_delay)
            print('Penarrow: Gott sei dank, zum Glück habe ich das überlebt\n')
            sleep(short_delay)
            print('Aber ich habe mir das linke Bein gebrochen und das schmerzt höllisch\n')
            sleep(short_delay)
            print('Zum Glück haben mir die Faerens eine Packung mit ihrer Heilmischung mitgegeben\n')
            sleep(short_delay)
        
        # Nicht benutzen
        elif rucksack == 2:
            
            print('Meine Idee wäre zu riskant\n')
            sleep(short_delay)
            print('Ich sollte schauen, ob ich drum herum laufen kann\n')
            sleep(short_delay)
            print('Erzähler: Er lief 10 Minuten in die eine Richtung, bis ein riesiger Abhang kam\n')
            sleep(short_delay)
            print('Ich muss hier runter klettern, damit ich weiter komme\n')
            sleep(short_delay)
            print('Zum Glück habe ich ja Eispickel und ein Seil dabei\n')
            sleep(short_delay)
            print('Erzähler: Penarrow kletterte runter und er konnte seinen Augen kaum glauben, was er da sah\n')
            sleep(long_delay)
            print('Penarrow: Man habe ich ein Glück, hier ist ja die Forschungsstation\n')
            sleep(short_delay)
            print('Ich sollte schnell dahin laufen. Es ist nämlich sehr kalt\n')
            sleep(short_delay)
            print('Erzähler: Als Penarrow dort ankam, traf er die Crew der Forschungsstation\n')
            sleep(long_delay)
            print('Sie erzählten ihm, dass bald ein Helikopter kommen würde, um ihn abzuholen\n')
            sleep(short_delay)
            print('Penarrow erzählte alles, was geschehen war und auf dieser Grundlage wurde ein Forschungsteam auf den Berg geschickt\n')
            sleep(long_delay)
            print('Er wurde nach einem 2 tägigen Aufenthalt nach Hause geflogen\n')
            
            # Gewonnen
            Art=text2art('Game   gewonnen')
            print(Art)
            sleep(short_delay)
            
            quit()
    
    
    
    
    
    
    
    
    # Englisch
    elif sprache == 2:
        print('Penarrow: I decided to go home today\n')
        sleep(short_delay)
        print('Faeren: Okay I wish you good luck on your way home\n')
        sleep(short_delay)
        print('We are going to hand you a backpack full with food and tools\n')
        sleep(long_delay)
        print('Penarrow: Many thanks\n')
        sleep(short_delay)
        print('Faeren: Hope to see you again soon\n')
        sleep(short_delay)
        print('Penarrow: I hope so too\n')
        sleep(short_delay)
        print('Narrator: Penarrow went out\n')
        sleep(short_delay)
        print('2 hours later Penarrow arrived at a huge cliffside\n')
        sleep(short_delay)
        print('Penarrow: Damnit, i have to get over this\n')
        sleep(short_delay)
        print('but how?!\n')
        sleep(short_delay)
        print('Those Faerens gave me a few things didnt they\n')
        sleep(short_delay)
        print('I should probably check those out\n')
        sleep(short_delay)
        
        # Entscheiding: Kletterseil und Eispickel benutzen oder nicht
        backpack = benutzer_zahl_eingabe([1, 2], 'Should i use this rope and pickaxe (1) or not (2): ')
        
        # Konsole clearen
        clearscreen()
        
        # Benutzen
        if backpack == 1:
            
            print('I could connect the rope to the pickaxe\n')
            sleep(short_delay)
            print('have one loose end tied to me\n')
            sleep(short_delay)
            print('and i throw the other end with the pickaxe, and hopefully it sticks and i get to climb over\n')
            sleep(long_delay)
            print('Narrator: Penarrow walked back a bit and aimed for the top of the cliff and thew the pickaxe\n')
            sleep(short_delay)
            print('Penarrow: Hope this stays there until I climbed over\n')
            sleep(long_delay)
            print('Narrator: He started climbin up and up but once he got halfway through,....\n')
            sleep(short_delay)
            print('the rope snapped and he fell!!!\n')
            sleep(short_delay)
            print('Penarrow: AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHH!!!! \n')
            sleep(short_delay)
            print('Narrator: He passed out upon the fall\n')
            sleep(short_delay)
            print('after a while... \n')
            sleep(long_delay)
            print('Penarrow: Oh God I am alive\n')
            sleep(short_delay)
            print('but I broke my right leg and it hurts like hell\n')
            sleep(short_delay)
            print('Luckily those Faerens packed me one of their serums\n')
            sleep(short_delay)
        
        # Nicht benutzen
        elif backpack == 2:
            
            print('That would be too risky\n')
            sleep(short_delay)
            print('There should be another way round\n')
            sleep(short_delay)
            print('Narrator: He walked for 10 minutes until reaching a dead end with a cliff\n')
            sleep(short_delay)
            print('I could climb down and go further\n')
            sleep(short_delay)
            print('Luckily i have this rope and pickaxe\n')
            sleep(short_delay)
            print('Narrator: Penarrow climbed down and couldnt believe what he saw\n')
            sleep(long_delay)
            print('Penarrow: It must be my lucky day, thats the research station!\n')
            sleep(short_delay)
            print('I should climb down quickly cuz its getting really cold\n')
            sleep(short_delay)
            print('Narrator: Once he arrived, he met his fellow crew members at the station\n')
            sleep(long_delay)
            print('They told him that a helicopter would arrive shortly to pick them up\n')
            sleep(short_delay)
            print('Penarrow told everyone of what he saw and what happened and a research team was sent to the mountain\n')
            sleep(long_delay)
            print('He got sent home after 2 days of research\n')
            
            # Gewonnen
            Art=text2art('Game   won')
            print(Art)
            sleep(short_delay)
        
            quit()
        
        
        
        
        
        
# Funktion Kapitel 6A
def exec_chapter6A(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Ich sollte es in Kauf nehmen, denn ich will ja hier wieder lebend raus kommen\n')
        sleep(short_delay)
        print('Erzähler: Er trank den Trank und nach ungefähr einer Stunde war sein Bein wieder komplett verheilt\n')
        sleep(long_delay)
        print('Als sein Bein geheilt war, musste er einen Weg aus der Gletscherspalte finden\n')
        sleep(short_delay)
        print('Penarrow: Okay wie komme ich jetzt hier nur wieder raus?\n')
        sleep(short_delay)
        print('Da vorne ist es mega hell. Ich sollte mal nach schauen, was das ist\n')
        sleep(short_delay)
        print('Erzähler: Penarrow lief ungefähr 10 min in die Richtung woher das helle Licht kam\n')
        sleep(short_delay)
        print('Als er ankam, staunte er nicht schlecht\n')
        sleep(short_delay)
        print('Penarrow: Man habe ich ein Glück, hier ist ja die Forschungsstation\n')
        sleep(short_delay)
        
        # Forschungsstation zeigen
        show_mountain_camp()
        
        sleep(short_delay)
        print('Ich sollte schnell dahin laufen, es ist nämlich sehr kalt\n')
        sleep(short_delay)
        print('Erzähler: Als Penarrow dort ankam, traf er die Crew der Forschungsstation\n')
        sleep(long_delay)
        print('Sie erzählten ihm, dass bald ein Helikopter kommen würde, um ihn abzuholen\n')
        sleep(short_delay)
        print('Penarrow erzählte alles, was geschehen war und auf dieser Grundlage wurde ein Forschungsteam auf den Berg geschickt\n')
        leep(long_delay)
        print('Er wurde nach einem 2 tägigen Aufenthalt nach Hause geflogen\n')
        
        # Gewonnen
        Art=text2art('Game   gewonnen')
        print(Art)
        sleep(short_delay)
        show_winner()
        
    # Englisch
    elif sprache == 2:
        print('I should probably take my life for granted\n')
        sleep(short_delay)
        print('Narrator: He drank the serum and after an hour or so his leg was fully healed\n')
        sleep(long_delay)
        print('After his leg was healed he got up to look for a way home\n')
        sleep(short_delay)
        print('Penarrow: Alright how do i get out of here now?\n')
        sleep(short_delay)
        print('There seems to be an opening over there, I should check that out\n')
        sleep(short_delay)
        print('Narrator: Penarrow walked towards the opening, the light from what seemed to be outside getting brighter and brighter\n')
        sleep(short_delay)
        print('Once he arrived he gazed in awe\n')
        sleep(short_delay)
        print('Penarrow: Would you look at that, its the research station!\n')
        sleep(short_delay)
        
        # Forschungsstation zeigen
        show_mountain_camp()
        
        sleep(short_delay)
        print('I should hurry because its getting really cold\n')
        sleep(short_delay)
        print('Narrator: Once he arrived he met his fellow crewmates\n')
        sleep(long_delay)
        print('They told him that a helicopter was going to arrive soon to pick them up\n')
        sleep(short_delay)
        print('Penarrow told everyone of what he had seen and shortly after a research team was sent to the mountain\n')
        leep(long_delay)
        print('He got sent home after just 2 days of research\n')
        
        # Gewonnen
        Art=text2art('Game   won')
        print(Art)
        sleep(short_delay)
        show_winner()