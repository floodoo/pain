# Import
from time import sleep
from painutilities import *
from asciiart import *
import random
from art import *

random_liste = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
faehigkeiten_liste = ['Feuer', 'Frost', 'Unsterblickeits', 'Unsichtbarkeits', 'Flug', 'Teleportations', 'Schrumpf', 'Hochsprung', 'Speed', 'Blitz']

# Funktion Kapitel 5
def exec_chapter5(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Ja ich will das Ritual machen\n')
        sleep(short_delay)
        print('Faeren: Das freut mich zu hören\n')
        sleep(short_delay)
        print('Erzähler: Ein Faeren pfeifte einmal\n')
        sleep(short_delay)
        print('Ein paar Sekunden später kam ein anderer Faeren zu ihm\n')
        sleep(short_delay)
        print('Faeren zu Faeren: Bereitet das Ritual vor\n')
        sleep(short_delay)
        print('Ja Meister\n')
        sleep(short_delay)
        print('Penarrow: Sie sind hier der Meister?\n')
        sleep(short_delay)
        print('Faeren: Ja hier bin ich\n')
        sleep(short_delay)
        print('In eurer Welt würde es wohl Präsident heißen\n')
        sleep(short_delay)
        
        # Enter und Konsole clearen
        nextstep()
        
        print('Penarrow: Wie in eurer Welt?\n')
        sleep(short_delay)
        print('Wir sind doch auf der Erde?!\n')
        sleep(short_delay)
        print('Faeren: Nicht ganz. Ihr Menschen seht nur einen verlassenen Tempel,\n')
        sleep(long_delay)
        print('aber in Wahrheit befinden wir uns in der so genannten Schattenwelt\n')
        sleep(long_delay)
        print('Für die meisten Menschen sind wir unsichtbar,\n')
        sleep(short_delay)
        print('aber ein paar Ausnahmen gibt es\n')
        sleep(short_delay)
        print('Und wie es aussieht, bist du eine Ausnahme\n')
        sleep(short_delay)
        print('Penarrow: Soll ich jetzt darüber froh sein oder nicht?\n')
        sleep(long_delay)
        print('Faeren: Das liegt bei dir, aber wenn die Legende wahr wird\n')
        sleep(short_delay)
        print('werden wir die frohen sein\n')
        sleep(short_delay)
        print('Ich auch, denn wenn die Legende nicht wahr wird\n')
        sleep(short_delay)
        print('werde ich Sterben\n')
        sleep(short_delay)
        print('Faeren: Dann hoffen wir mal, dass du der Auserwählte bist\n')
        
        # Enter und Konsole clearen
        nextstep()
        
        print('Faeren zu Faeren: Das Ritual ist vorbereitet\n')
        sleep(short_delay)
        print('Faeren zu Penarrow: Folge mir, wir gehen zum Ritual\n')
        sleep(short_delay)
        print('Erzähler: Nach ein paar Minuten Laufweg sind sie an einem Tempel angekommen\n')
        sleep(long_delay)
        print('Faeren: Leg dich bitte hier hin und trinke diesen Trank\n')
        sleep(short_delay)
        print('Erzähler: Penarrow legte sich hin und trank den Trank\n')
        sleep(short_delay)
        print('Erst passierte nichts, doch dann wurde er zur Hälfte rot\n')
        sleep(short_delay)
        ritual_schaffen = (random.choice(random_liste))
        
        # Ritual schaffen?
        if ritual_schaffen <= 70:
            
        
            print('und viel viel größer als ein normaler Mensch\n')
            sleep(short_delay)
            print('Faeren: Das ist ja fantastisch du hast überlebt\n')
            sleep(short_delay)
            print('Penarrow: Und was ist jetzt meine Fähigkeit?\n')
            sleep(short_delay)
            
            # Entscheidung: Welche Fähigkeit bekommt Penarrow
            faehigkeit = (random.choice(random_liste))
            
            print('Wie es aussieht hast du die: \n')
            sleep(short_delay)
            print(random.choice(faehigkeiten_liste))
            sleep(long_delay)
            print('Fähigkeit\n')
            sleep(short_delay)
            print('Komm mit wir trainieren dich\n')
            sleep(short_delay)
            print('Erzähler: Sie liefen durch die Stadt bis sie zu einem Trainingsgelände kamen\n')
            sleep(long_delay)
            print('Und als sie liefen hatte jeder Faeren ihn mit großen Erwartungen angeschaut\n')
            sleep(long_delay)
            print('Faeren: Das ist Trainingsmeister Gooldtha\n')
            sleep(short_delay)
            print('Gooltha: Schön dich kennen zu lernen\n')
            sleep(short_delay)
            print('Ich werde dich trainieren, damit du mit deiner Fähigkeit umgehen kannst\n')
            sleep(short_delay)
            print('Penarrow: Ich dachte, ihr kennt euch mit den Fähigkeiten nicht aus, die man beim Ritual bekommt\n')
            sleep(long_delay)
            print('Gooltha: Doch tun wir. Es ist gibt nur so viele Fähigkeiten und es ist zufällig, welche du bekommst\n')
            sleep(long_delay)
            print('Dann fangen wir mal an\n')
            sleep(short_delay)
            
            # Enter und Konsole clearen
            nextstep()
            
            print('Erzähler: Es vergingen Tage, Monate sogar Jahre und er trainierte immer weiter\n')
            sleep(short_delay)
            print('Bis zu einem schrecklichem Tag\n')
            sleep(short_delay)
            print('Faeren: Penarrow! Wir werden angegriffen. Beschütze uns!\n')
            sleep(short_delay)
            print('Penarrow: Wer greift euch an?\n')
            sleep(short_delay)
            print('Faeren: Es sind die Devil''s Warriers\n')
            sleep(short_delay)
            
            # Teufel anzeigen
            show_devil()
            
            print('Da sind sie auch schon. Greif sie an!\n')
            sleep(short_delay)
            # Teufel Drachen anzeigen
            show_devil_pet()
            
            print('Worauf wartest du? Du hast für diesen Moment trainiert\n')
        
        
        else:
            print('Das Ritual ist nicht gut ausgegangen')
            sleep(short_delay)
            Art=text2art('Game   Over')
            print(Art)
            quit()
        
    
    # Englisch
    elif sprache == 2:
        print('Penarrow: Yes I do want to perform the ritual\n')
        sleep(short_delay)
        print('Faeren: I am glad to hear that\n')
        sleep(short_delay)
        print('Narrator: A Faeren blew a whistle\n')
        sleep(short_delay)
        print('Another Faeren joined him shortly\n')
        sleep(short_delay)
        print('Faeren zu Faeren: Prepare the Ritual\n')
        sleep(short_delay)
        print('Yes master\n')
        sleep(short_delay)
        print('Penarrow: You are the master here?\n')
        sleep(short_delay)
        print('Faeren: Yes I am\n')
        sleep(short_delay)
        print('In your world that would probably be named a President\n')
        sleep(short_delay)
        
        # Enter und Konsole clearen
        nextstep()
        
        print('Penarrow: What do you mean with "in your world"?\n')
        sleep(short_delay)
        print('Arent we still on the earth?!\n')
        sleep(short_delay)
        print('Faeren: Not quite. You humans might see nothing but an ancient Temple,\n')
        sleep(long_delay)
        print('but in reality its what we call the shadow realm\n')
        sleep(long_delay)
        print('Which is invisible for most humans,\n')
        sleep(short_delay)
        print('but of course there are a few exceptions\n')
        sleep(short_delay)
        print('and from what it looks like, you are one of those exceptions\n')
        sleep(short_delay)
        print('Penarrow: Should I be glad about that or not?\n')
        sleep(long_delay)
        print('Faeren: Thats up to you, but once the legend has fulfilled\n')
        sleep(short_delay)
        print('we are going to be the ones that are glad\n')
        sleep(short_delay)
        print('Me too because if the legend doesnt fulfill\n')
        sleep(short_delay)
        print('i am going to die.\n')
        sleep(short_delay)
        print('Faeren: Then let us hope that you are the chosen one\n')
        
        # Enter und Konsole clearen
        nextstep()
        
        print('Faeren zu Faeren: The ritual is being prepared\n')
        sleep(short_delay)
        print('Faeren zu Penarrow: Follow me, we are going to the ritual\n')
        sleep(short_delay)
        print('Narrator: A few minutes later they arrive at a temple\n')
        sleep(long_delay)
        print('Faeren: Please lay down here and drink this serum\n')
        sleep(short_delay)
        print('Narrator: Penarrow lies down and drinks the serum\n')
        sleep(short_delay)
        print('Nothing seemed to happen at first but then suddenly he began turning red halfway through his body\n')
        sleep(short_delay)
        ritual_schaffen = (random.choice(random_liste))
        
        # Ritual schaffen
        if ritual_schaffen <= 70:
            print('and grew taller than any normal human\n')
            sleep(short_delay)
            print('Faeren: That is just fantastic, you survived\n')
            sleep(short_delay)
            print('Penarrow: And whats my ability now?\n')
            sleep(short_delay)
            
            # Entscheidung: Welche Fähigkeit bekommt Penarrow
            faehigkeit = (random.choice(random_liste))
            
            # Konsole clearen
            clearscreen()
            
            # Feuerfähigkeit bekommen
            if faehigkeit <= 50:
                
                print('Faeren:  By the looks of it you should be able to spit fire now\n')
            
            # Frostfähigkeit bekommen
            elif faehigkeit >= 55:
                
                print('Faeren: By the looks of it you should be able to freeze things now\n')

            sleep(long_delay)
            print('Follow me to start your training\n')
            sleep(short_delay)
            print('Narrator: They walked through the whole town until they reached a training field\n')
            sleep(long_delay)
            print('and as they walked through the town all the Faerens gazed at him in awe\n')
            sleep(long_delay)
            print('Faeren: This is our trainingsmaster Gooldtha\n')
            sleep(short_delay)
            print('Gooltha: Its nice to meet you\n')
            sleep(short_delay)
            print('I am going to train you, so that you get a grip of your abilities and know how to use them in a combat situation\n')
            sleep(short_delay)
            print('Penarrow: I thought that you dont know anything about the abilities gained from the ritual\n')
            sleep(long_delay)
            print('Gooltha: Yes we do. Its just that there are so many and its random which one you would have become\n')
            sleep(long_delay)
            print('Now let us begin\n')
            sleep(short_delay)
            
            # Enter und Konsole clearen
            nextstep()
            
            print('Narrator: Days, months and even years of training passed\n')
            sleep(short_delay)
            print('until that one unfortunate day\n')
            sleep(short_delay)
            print('Faeren: Penarrow! We are being attacked. Protect us!\n')
            sleep(short_delay)
            print('Penarrow: Who is the attacker?\n')
            sleep(short_delay)
            print('Faeren: Its the Devil Warriors\n')
            sleep(short_delay)
            
            # Teufel anzeigen
            show_devil()
            
            print('There they are. Attack them!\n')
            sleep(short_delay)
            # Teufel Drachen anzeigen
            show_devil_pet()
            
            print('What are you waiting for, you trained for this very moment didnt you\n')
        
        # Game Over
        else:
            print('')
            sleep(short_delay)
            Art=text2art('Game   Over')
            print(Art)
            quit()
        
# Funktion Kapitel 5A
def exec_chapter5A(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Ich werde kämpfen\n')
        sleep(short_delay)
        
        kampf_leben = (random.choice(random_liste))
        if kampf_leben <= 70:
        
            print('Erzähler: Penarrow kämpfte, bis der Feind besiegt war und das dauerte 2 Tage\n')
            sleep(short_delay)
            
            # Troll anzeigen
            show_troll()
            
            print('2 Tage später\n')
            sleep(short_delay)
            print('Nachdem Penarrow alle besiegte hatte, war so erschöpft, dass er danach sofort in den Schlaf viel\n')
            sleep(long_delay)
            print('Penarrow schlief sage und schreibe 3 Monate lang\n')
            sleep(short_delay)
            print('3 Monate später\n')
            
            # Enter und Konsole clearen
            nextstep()
            
            print('Penarrow: * Gähnte * wie lange hab ich geschlafen?\n')
            sleep(short_delay)
            print('Faeren: Hey, gut das du wach bist!\n')
            sleep(short_delay)
            print('Du hast 3 Monate lang geschlafen\n')
            sleep(short_delay)
            print('Penarrow: Echt? So lange\n')
            sleep(short_delay)
            print('Faeren: Ja aber das macht nichts, du hast uns nämlich alle gerettet\n')
            sleep(short_delay)
            print('Und dafür sind wir dir so dankbar\n')
            sleep(short_delay)
            print('Komm erst mal mit! Du musst ja riesigen Hunger haben\n')
            sleep(short_delay)
            print('Oh, ja das habe ich!\n')
            sleep(short_delay)
            print('Nach einem riesigen Festmahl, kam die Frage auf, was er jetzt machen möchte\n')
            sleep(short_delay)
    
        elif kampf_leben >= 71:
            print('Du konntest die Faerens nicht beschützen')
            Art=text2art('Game   Over')
            print(Art)
            quit()
    
    # Englisch
    elif sprache == 2:
        print('Penarrow: I am willing to fight\n')
        sleep(short_delay)
        
        kampf_leben = (random.choice(random_liste))
        if kampf_leben <= 70:
        
            print('Narrator: Penarrow fought until the enemy was defeated, which took 2 days\n')
            sleep(short_delay)
            
            # Troll anzeigen
            show_troll()
            
            print('2 days later\n')
            sleep(short_delay)
            print('After Penarrow had defeated them all he was so exhausted that he just passed out on the spot\n')
            sleep(long_delay)
            print('Penarrow slepts for roughly 3 months\n')
            sleep(short_delay)
            print('3 months later\n')
            
            # Enter und Konsole clearen
            nextstep()
            
            print('Penarrow: * Yawn * how long was I sleeping for?\n')
            sleep(short_delay)
            print('Faeren: So, you are finally awake!\n')
            sleep(short_delay)
            print('You slept for 3 whole months\n')
            sleep(short_delay)
            print('Penarrow: Really? So long\n')
            sleep(short_delay)
            print('Faeren: Yeah but thats nothing, the important thing is that you saved us all\n')
            sleep(short_delay)
            print('and we all thank you for that\n')
            sleep(short_delay)
            print('Come with me, you must be starving\n')
            sleep(short_delay)
            print('Penarrow: Oh, yes I am hungry!\n')
            sleep(short_delay)
            print('Narrator: After a huge feast a question accured, what Penarrow wants to do now\n')
            sleep(short_delay)
    
        elif kampf_leben >= 75:
            print('You were unable to protect the Faerens')
            Art=text2art('Game   Over')
            print(Art)
        
        
        
        
        
# Funktion Kapitel 5B
def exec_chapter5B(sprache, short_delay = 1, long_delay = 2):
    
    # Deutsch
    if sprache == 1:
        
        print('Penarrow: Ich möchte das Ritual nicht machen\n')
        sleep(short_delay)
        print('Faeren: Alles Klar, schade aber wenn du es so willst werde ich das akzeptieren\n')
        sleep(long_delay)
        
    # Englisch
    elif sprache == 2:
        print('Penarrow: No, I do not want to perform the ritual\n')
        sleep(short_delay)
        print('Faeren: Alrighty, if thats your choice ten I will respect it so\n')
        sleep(long_delay)