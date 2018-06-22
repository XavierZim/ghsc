import time
import random
from random import randint
Name = raw_input("What is your name, inconspicuous hero? ")
Magic = 0
maxmagic = 0
Strength = 100
Charisma = 50
Knowledge = 50
Health = 200
maxhealth = 200
sword_buff = 0
tome_buff = 0
stave_buff = 0
str_damage = Strength / 5 + sword_buff 
mgc_damage = Magic / 2 + tome_buff + stave_buff

test_hit_enemy = ("You hit the enemy! The damage you did was: %s")
enemy_hp = ("Enemy health now equals: %s")

drMagic = 25
drStrength = 25
drCharisma = 25
drKnowledge = 25
drHealth = 50

goMagic = 25
goStrength = 100
goCharisma = 25
goKnowledge = 25
goHealth = 100
goAttack = goStrength / 5

slMagic = 40
slStrength = 10
slCharisma = 0
slKnowledge = 0
slHealth = 50
slMaxHealth = 50
slAttack = slMagic / 2

imMagic = 10
imStrength = 100
imCharisma = 0
imKnowledge = 0
imHealth = 50
imMaxHealth = 50
imAttack = imStrength / 5

ogMagic = 20
ogStrength = 50
ogCharisma = 0
ogKnowledge = 0
ogHealth = 200
ogMaxHealth = 200
ogAttack1 = ogStrength / 5
ogAttack2 = ogMagic / 2

script = ("""Name: %s
             Magic: %s
             Strength: %s
             Charisma: %s
             Knowledge: %s
             Health: %s
             Sword Buff: %s
             Tome Buff: %s
             Stave Buff: %s""") 
          
print(script %(Name, maxmagic, Strength, Charisma, Knowledge, maxhealth, sword_buff, tome_buff, stave_buff))

print("Hello, " + Name)
choice1 = raw_input("""Choose one of two options: 
                       Who are you?(1) 
                       Why am I here?(2)""")
if choice1 == ("1"):
    print ("I am a spirit guide, who has been here as long as this dungeon has existed.")
if choice1 == ("2"):
    print("I don't know the answer to that. You just fell from nowhere.")
time.sleep(2)    
print("My name is Manuel, and I have been sent to help you. You are destined to stop evil!")
time.sleep(2)
choice2 = raw_input("""Choose one of two options:
                       Where do we need to go?(1)
                       Why?(2)""")

if choice2 == ("1"):
    print ("follow me, young man, to the endless halls of this dungeon, of that which monsters of many races confide in.")
if choice2 == ("2"):
    print("Why? Because the prophecy states that a person that is 18 and in THIS VERY dungeon will rid the world of evil.")

choice3 = raw_input("""Choose one of two options:
                       What next?(1)
                       But why?(2)""")
if choice3 == ("1"):
    print ("The gods say you must rid this place of the mana produced creatures that roam this dungeon.")
if choice3 == ("2"):
    print("BECAUSE I SAID SO! Now, there are mana-produced creatures that have plagued this dungeon for years. Let's fight your first battles.")
    
print("You have encountered Dungeon Rat!")

Crit = 0

stats = (""" %s stats:
             Health: %s
             Strength: %s
             Crit: %s """)
             
print(stats %(Name, Health, Strength, Crit))

drCrit = 0


drstats = (""" Dungeon Rat stats:
               Health: %s
               Strength: %s
               Crit: %s""")
               
print(drstats %(drHealth, drStrength, drCrit))

print ("""As you may have noticed, this is not your complete stat list.
The reason for this is because you will only be shown what is crucial at the moment.""")
time.sleep(2)

print ("""This is what you see when you engage an enemy. Select 1 for attack""")

while (drHealth > 0):
    battle_1 = raw_input("""What would you like to do?
                            attack(1)
                            check stats(2)
                            inventory(3)""")

    if battle_1 == ("1"):
        drHealth = drHealth - str_damage
        print (test_hit_enemy %(str_damage))
        if (drHealth < 0):
            drHealth = 0  
        print (enemy_hp %(drHealth))
    else:
        print ("cheater")
        drHealth = drHealth - str_damage
        print (test_hit_enemy %(str_damage))
        print (enemy_hp %(drHealth))
 
print("Congratulations, " + Name + "!" 'You have defeated the dungeon rat! There is, however, one more monster left.')
time.sleep(1)
print("A dastardly, DIABOLICAL creation.")
time.sleep(2)
print("A GOBLIN!")
time.sleep(3)
print ("""You were lucky that the dungeon rat did not attack back!
          However, goblins are different!""")
          
stats = (""" %s stats:
             Health: %s
             Strength: %s
             Crit: %s """)
             
print(stats %(Name, Health, Strength, Crit))

goCrit = 0

gostats = (""" Goblin stats:
               Health: %s
               Strength: %s
               Crit: %s""")

print(gostats %(goHealth, goStrength, goCrit))


while (goHealth > 0 or Health > 0):
    battle_2 = raw_input("""What would you like to do?
                            attack(1)
                            check stats(2)
                            inventory(3)""")

    if battle_2 == ("1"):
        goHealth = goHealth - str_damage
        print (test_hit_enemy %(str_damage))
        if (goHealth < 0):
            goHealth = 0  
        print (enemy_hp %(goHealth))
    elif battle_2 == ("2"):
        stats = (""" %s stats:
                     Health: %s
                     Strength: %s
                     Crit: %s """)
        

        print(stats %(Name, Health, Strength, Crit))
    elif battle_2 == ("3"):
        print("You do not have an inventory yet.")
    
    if Health == (0):
        print(Name + "has blacked out. GAME OVER.")
        
    if goHealth == (0):
        break #exits loop
    
    Health = Health - goAttack
    print("Goblin attacks! You lost 20 health!")
    
    if (Health < 0):
        Health = 0 

print("Congratulations, " + Name + "! You have defeated the goblin! you got 100 GP. Here are your stat gains:")

gold = 100
your_gold = ("Your gold: %s")

Strength = Strength + 10
maxhealth = maxhealth + 10

Gains1 = (""" %s has won the battle!:
             Health: %s
             Strength: %s """)
             
print(Gains1 %(Name, maxhealth, Strength))

Health = maxhealth

time.sleep (3)

print ("Young hero, you are on your way to curing the world. Take this sword.")
inventory = [" |sword"]
time.sleep(2)
print ("""Swords give you a certain buff that allows you to do as much more damage as the sword buff is.
          This particular sword gives plus 4 damage.""")
sword_buff = sword_buff + 4


time.sleep (2)

print("Obtained Wooden Sword!")
print("Wooden Sword added to inventory.")
inventorycheck1 = raw_input("Check inventory? (Y/N)")

if inventorycheck1 == ("Y"):
    for inv in inventory:
        print(inv)
elif inventorycheck1 == ("N"):
    print("We will continue our journey henceforth. Onward!")
    
print("You gained 100 GP!")
GP = 100
    
print("Our destination is the town located above the dungeon. There, we can obtain supplies to survive the fights to come.")
print("Location: Flemish Town")

print("Our first stop will be the Magic Shop. It is necessary to go due to the fact that our first hurdle is the Slime Dungeon.")

townactions1 = 6

while (townactions1 > -1):
    actions_remaining = ("You have %s actions remaining.")
    print(actions_remaining %(townactions1))
    actions1 = raw_input("""What will you do?
                            Enter Magic shop(1)
                            Enter Armory(2)
                            Enter Apothecary(3)
                            Go to the Town Hall(4)
                            Listen to a lesson at the Institute(5)
                            Take on an apprenticeship at the School of Magic(6)
                            Venture into a dungeon!(7)""")
                            
    if actions1 == ("1"):
        print("Hello, wandering adventurer! What do you wish to buy?")
        magicshop = raw_input("""Basic Tome: 10 GP(1)
                                 Basic Stave: 10 GP(2)""")
                    
        if magicshop == ("1"):
            inventory.append(" |Basic Tome")
            tome_buff = tome_buff + 10
            if gold < 10:
               print("You do not have enough gold for this item.")
               continue
            magic_display1 = ("""Magic: %s
                                 Tome Buff: %s""")
            print(magic_display1 %(Magic, tome_buff))
            townactions1 = townactions1 - 1
    
        if magicshop == ("2"):
            inventory.append(" |Basic Stave")
            stave_buff = stave_buff + 10
            if gold < 10:
                print("You do not have enough gold for this item.")
                continue
            magic_display2 = ("""Magic: %s
                             Stave Buff: %s""")
            print(magic_display2 %(Magic, stave_buff))
            townactions1 = townactions1 - 1
        
    if actions1 == ("2"):
        print ("Young one, what will you buy?")
        print                (your_gold %(gold))
        armory = raw_input("""Plain Sword 'sb:5' 50 GP(1)
                              Heavy sword'sb:10' 200 GP(2)
                              Enchanted Plain Sword 'sb:20' 300 GP(3)
                              Enchanted Heavy Sword 'sb:40' 600 GP(4)
                              Enchanted Ring 'hp:50' 1000 GP(5)
                              Enchanted Bracelet 'hp:100' 1500 GP(6)
                              Enchanted Necklace 'hp200' 2000 GP(7)""")
        if armory == ("1"):
            if gold < 50:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Plain Sword")
            sword_buff = 5
            print ("sword buff: 5")
            print ("-50 gold")
            gold = gold - 50
            townactions1 = townactions1 - 1
        elif armory == ("2"):
            if gold < 200:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Heavy Sword")
            sword_buff = 10
            print ("Sword Buff: 10")
            print ("-200 gold")
            gold = gold - 200           
            townactions1 = townactions1 - 1
        elif armory == ("3"):
            if gold < 300:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Enchanted Plain Sword")
            sword_buff = 20
            print ("Sword Buff: 20")
            print ("-300 gold")
            gold = gold - 300
            townactions1 = townactions1 - 1
        elif armory == ("4"):
            if gold < 600:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Enchanted Heavy Sword")
            sword_buff = 40
            print ("-600 gold")
            gold = gold - 600
            townactions1 = townactions1 - 1
        elif armory == ("5"):
            if gold < 1000:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Enchanted Ring")
            maxhealth = maxhealth + 50
            Health = maxhealth
            print ("maxhealth: +50 (free full health)")
            print ("-1000 gold")
            gold = gold - 1000
            townactions1 = townactions1 - 1
        elif armory == ("6"):
            if gold < 1500:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Enchanted Bracelet")
            maxhealth = maxhealth + 100
            Health = maxhealth
            print ("maxhealth: +100 (free full health)")
            print ("-1500 gold")
            gold = gold - 1500
            townactions1 = townactions1 - 1
        elif armory == ("7"):
            if gold < 2000:
                print("You do not have enough gold for this item.")
                continue
            inventory.append (" |Enchanted Necklace")
            maxhealth = maxhealth + 200
            Health = maxhealth
            print ("maxhealth: 200 (free full health)")
            print ("-2000 gold")
            gold = gold - 2000
            townactions1 = townactions1 - 1
            
    if actions1 == ("3"):
        print("Welcome to the apothecary! Take your pick of healing herbs and potions below:")
        apothecary = raw_input("""Standard Herb 'heal:50' 10 GP(1)
                                  Mixed Herbs 'heal:200' 50 GP(2)
                                  Strength Potion 'strength +50' 100 GP(3)
                                  Magic Potion 'magic +50' 100 GP(4)""")
        if apothecary == ("1"):
            inventory.append (" |Standard Herb")
            print("Standard Herb added to inventory.")
            townactions1 = townactions1 - 1
        
        if apothecary == ("2"):
            inventory.append(" |Mixed Herbs")
            print("Mixed Herbs added to inventory.")
            townactions1 = townactions1 - 1
            
        if apothecary == ("3"):
            inventory.append(" |Strength Potion")
            print("Strength Potion added to inventory.")
            Strength = Strength + 50
            townactions1 = townactions1 - 1
            
        if apothecary == ("4"):
            inventory.append(" |Magic Potion")
            print("Magic Potion added to inventory.")
            Magic = Magic + 50
            townactions1 = townactions1 - 1

    if actions1 == ("4"):
        if random.randint(0,100) < 50:
            print ("""You attend a public meeting at the town hall.
                  It is really boring, but you learned things.
                  Charisma: +5""")
            Charisma = Charisma + 5
            townactions1 = townactions1 - 1
        else: 
            print("You fell asleep during the meeting.")
            townactions1 = townactions1 - 1
            
    if actions1 == ("5"):
        if random.randint(0,100) < 50:
            print("""You decide to travel to the institute to pursue your thirst for knowledge.
                     You listen intently to the professor.
                     Knowledge +5""")
            Knowledge = Knowledge + 5
            townactions1 = townactions1 - 1
        else:
            print("You dozed off during the professor's lecture.")
            townactions1 = townactions1 - 1
    
    if actions1 == ("6"):
        if random.randint(0,100) < 75:
            print("The school of magic accepts you for today. Magic +10")
            Magic = Magic + 10
            townactions1 = townactions1 - 1
        else: 
            print("The school says no.")
            townactions1 = townactions1 - 1
    
    if actions1 == ("7") or townactions1 == ("0"):
        dungeon_actions = 3
        while (dungeon_actions > 0):
            dungeons_remaining = ("%s dungeons remaining.")
            print (dungeons_remaining %(dungeon_actions))
            whichdungeon = raw_input ("""Which dungeon would you like to go to?
                                        Slime Dungeon(magical)(1)
                                        Imp Dungeon(physical)(2)
                                        Ogre Dungeon(neutral)(3)""")
            
            if whichdungeon == ("1"):
                
                print("Entering Slime Dungeon...") 
                slime_number = 1
                while (slime_number < 10):
                    while (slHealth > 0 or Health > 0):
                        mgc_damage = Magic / 2 + tome_buff + stave_buff
                        slstats = (""" Slime stats:
                                   Health: %s
                                   Strength: %s
                                   Magic: %s""")
                        print(slstats %(slHealth, slStrength, slMagic))
                        sl_battle1 = raw_input("""What would you like to do?
                                                attack(magic)(1)
                                                check stats(2)
                                                inventory(3)""")
            
                        if sl_battle1 == ("1"):
                            slHealth = slHealth - mgc_damage
                            slime_hit = ("You hit Slime! Damage dealt: %s")
                            print(slime_hit %(mgc_damage))
                            if slHealth < 0:
                                slHealth = 0
                                slime_remain_hp = ("Slime has %s health left.")
                                print(slime_remain_hp %(slHealth))
                                
                            if slHealth == 0:
                                print("You have defeated slime!")
                        elif sl_battle1 == ("2"):
                            stats = (""" %s stats:
                                         Health: %s
                                         Magic: %s
                                         Crit: %s """)
                            print(stats %(Name, Health, Magic, Crit))
                        elif sl_battle1 == ("3"):
                            for inv in inventory:
                                print(inv)
                            inventorycheck2 = raw_input("Would you like to use an item in your inventory?(Y/N)")
                            if inventorycheck2 == ("Y"):
                                choose_item = raw_input("Which one?")
                                if choose_item == ("Standard Herb"):
                                    Health = Health + 50
                                    print("50 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                elif choose_item == ("Mixed Herbs"):
                                    Health = Health + 200
                                    print("200 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                else:
                                    continue
                            if inventorycheck2 == ("N"):
                                continue
                            
                        
                        if Health == (0):
                            print(Name + "has blacked out. GAME OVER.")
                            
                        if slHealth == (0):
                            break #exits loop
                        
                        Health = Health - slAttack
                        slime_attacks = ("Slime attacks! Lost %s health.")
                        print (slime_attacks %(slAttack))
                        
                        if (Health < 0):
                            Health = 0 
                                
                        slime_number = slime_number + 1
                    slMagic = slMagic + 10
                    slMaxHealth = slMaxHealth + 10
                    slHealth = slMaxHealth
                    
            if whichdungeon == ("2"):
                
                print("Entering Imp Dungeon...") 
                imp_number = 1
                while (imp_number < 10):
                    while (imHealth > 0 or Health > 0):
                        mgc_damage = Magic / 2 + tome_buff + stave_buff
                        imstats = (""" Imp stats:
                                   Health: %s
                                   Strength: %s
                                   Magic: %s""")
                        print(imstats %(imHealth, imStrength, imMagic))
                        im_battle1 = raw_input("""What would you like to do?
                                                attack(magic)(1)
                                                check stats(2)
                                                inventory(3)""")
            
                        if im_battle1 == ("1"):
                            imHealth = imHealth - mgc_damage
                            imp_hit = ("You hit imp! Damage dealt: %s")
                            print(imp_hit %(str_damage))
                            if imHealth < 0:
                                imHealth = 0
                                imp_remain_hp = ("Imp has %s health left.")
                                print(imp_remain_hp %(imHealth))
                                
                            if imHealth == 0:
                                print("You have defeated imp!")
                        elif im_battle1 == ("2"):
                            stats = (""" %s stats:
                                         Health: %s
                                         Strength: %s
                                         Crit: %s """)
                            print(stats %(Name, Health, Strength, Crit))
                        elif im_battle1 == ("3"):
                            for inv in inventory:
                                print(inv)
                            inventorycheck2 = raw_input("Would you like to use an item in your inventory?(Y/N)")
                            if inventorycheck2 == ("Y"):
                                choose_item = raw_input("Which one?")
                                if choose_item == ("Standard Herb"):
                                    Health = Health + 50
                                    print("50 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                elif choose_item == ("Mixed Herbs"):
                                    Health = Health + 200
                                    print("200 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                else:
                                    continue
                            if inventorycheck2 == ("N"):
                                continue
                            
                        
                        if Health == (0):
                            print(Name + "has blacked out. GAME OVER.")
                            
                        if slHealth == (0):
                            break #exits loop
                        
                        Health = Health - imAttack
                        imp_attacks = ("Imp attacks! Lost %s health.")
                        print (imp_attacks %(imAttack))
                        
                        if (Health < 0):
                            Health = 0 
                                
                        imp_number = imp_number + 1
                    imMagic = imMagic + 10
                    imMaxHealth = imMaxHealth + 10
                    imHealth = imMaxHealth

            if whichdungeon == ("2"):
                
                print("Entering Ogre Dungeon...") 
                og_number = 1
                while (og_number < 5):
                    while (ogHealth > 0 or Health > 0):
                        mgc_damage = Magic / 2 + tome_buff + stave_buff
                        ogstats = (""" Ogre stats:
                                   Health: %s
                                   Strength: %s
                                   Magic: %s""")
                        print(ogstats %(ogHealth, ogStrength, ogMagic))
                        og_battle1 = raw_input("""What would you like to do?
                                                attack(magic)(1)
                                                attack(physical)(2)
                                                check stats(3)
                                                inventory(4)""")
            
                        if og_battle1 == ("1"):
                            ogHealth = ogHealth - mgc_damage
                            ogre_hit = ("You hit imp! Damage dealt: %s")
                            print(ogre_hit %(str_damage))
                            if ogHealth < 0:
                                ogHealth = 0
                                ogre_remain_hp = ("Ogre has %s health left.")
                                print(ogre_remain_hp %(ogHealth))
                                
                            if ogHealth == 0:
                                print("You have defeated ogre!")
                        elif og_battle1 == ("2"):
                            stats = (""" %s stats:
                                         Health: %s
                                         Strength: %s
                                         Crit: %s """)
                            print(stats %(Name, Health, Strength, Crit))
                        elif og_battle1 == ("3"):
                            for inv in inventory:
                                print(inv)
                            inventorycheck2 = raw_input("Would you like to use an item in your inventory?(Y/N)")
                            if inventorycheck2 == ("Y"):
                                choose_item = raw_input("Which one?")
                                if choose_item == ("Standard Herb"):
                                    Health = Health + 50
                                    print("50 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                elif choose_item == ("Mixed Herbs"):
                                    Health = Health + 200
                                    print("200 points healed.")
                                    health = ("Your health is: %s")
                                    print(health %(Health))
                                    if Health > maxhealth:
                                        Health = maxhealth
                                else:
                                    continue
                            if inventorycheck2 == ("N"):
                                continue
                            
                        
                        if Health == (0):
                            print(Name + "has blacked out. GAME OVER.")
                            
                        if ogHealth == (0):
                            break #exits loop
                        
                        Health = Health - ogAttack
                        ogre_attacks = ("Ogre attacks! Lost %s health.")
                        print (ogre_attacks %(ogAttack))
                        
                        if (Health < 0):
                            Health = 0 
                                
                        ogre_number = ogre_number + 1
                    ogMagic = ogMagic + 10
                    ogMaxHealth = ogMaxHealth + 10
                    ogHealth = ogMaxHealth