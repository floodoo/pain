# Import
from time import sleep
from painutilities import *
from asciiart import *
 
# Funktion Kapitel Vorstory
def exec_vorstory(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        # Konsole clearen
        clearscreen()
        
        sleep(short_delay)
        print('Erzähler: In einem fernen und unentdeckten Teil der Welt gibt es eine Stadt, von der nicht viele Bescheid wissen.\n')
        sleep(long_delay)
        print('Die wenigen, die die Stadt zu Gesicht bekommen hatten und überlebt hatten, beschrieben sie als eine Geisterstadt,\n')
        sleep(long_delay)
        print('wo anscheinend keine Art von Leben existierte. Jedoch es existierte Leben. Sie nannten sich die Faerens.\n')
        sleep(long_delay)
        print('Die Faerens sind eine Menschen ähnliche Rasse, die sehr zurückhalten lebt.\n')
        sleep(short_delay)
        print('Sobald jemand in ihre Nähe kommt verstecken sie sich oder wenn sie sich angegriffen fühlen töten sie dich\n')
        
        # Enter und Konsole clearen
        nextstep()
        
        print('In dieser mysteriösen Epoche hatte das Team des Forschungsschiffes USS International den Auftrag, in der Antarktis nach einer Höhle zu suchen, die durch die Erderwärmung freigelegt wurde\n')
        sleep(long_delay)
        
        # Boot zeigen
        show_boat()
        sleep(short_delay)
        print('Als die USS International und ihre Crew in die Nähe von der Antarktis kamen, begann ein Schneesturm aufzuziehen und ausgerechnet jetzt strandete die USS auf einer riesigen Eisscholle\n')
        sleep(long_delay)
    
    # Englisch
    elif sprache == 2:
        
        clearscreen()
        
        sleep(short_delay)
        print('Narrator: In a far and distant land exists a town that not many know about.\n')
        sleep(long_delay)
        print('The few that were lucky enough to see the town described it mostly as a ghost town\n')
        sleep(long_delay)
        print('where apparently no sight of life has been discovered. But there was life indeed, beings named the Faerens.\n')
        sleep(long_delay)
        print('The Faerens are nothing like Humans and are isolated from the outside world.\n')
        sleep(short_delay)
        print('As soon as someone comes close to them they start hiding or even attacking the intruder\n')
        
        # Enter und Konsole clearen
        nextstep()
        
        print('A team of the research ship USS International had the task to perform an expedition in a cave that had been opened thanks to global warming\n')
        sleep(long_delay)
        
        # Boot zeigen
        show_boat()
        sleep(short_delay)
        print('As soon as the USS International and its crew had come close to the coast a massive snow storm had started to appear which caused the ship to get stranded on the coast\n')
        sleep(long_delay)
    