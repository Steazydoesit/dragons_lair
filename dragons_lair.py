character_classes = ('Mage','Rogue','Hunter','Warrior')
health = {'Mage':200,'Rogue':225,'Hunter':250,'Warrior':300}
dmg_range = {'Mage':75,'Rogue':60,'Hunter':55,'Warrior':50}
boss = ('Dragon')
boss_health = {'Dragon':500}
boss_dmg_range = {'Dragon':40}

mage_attacks = [['Fireball',100,40],['Arcane Blast',70,60],['Pyroblast',50,90]]
rogue_attacks = [['Shiv',100,40],['Ambush',80,50],['Mutilate',60,80]]
hunter_attacks = [['Serpent Shot',100,35],['Explosive Shot',80,50],['Aimed Shot',70,65]]
warrior_attacks = [['Slam',100,35],['Mortal Strike',80,50],['Execute',30,100]]
dragon_attacks = [['Flame Breath',90,20],['Claw',60,40],['Death and Destruction',20,100]]

import random
import time

class Character:
    
    def __init__(self):
        
        character_class = input('Hello.  Please choose a class: Mage, Rogue, Hunter, Warrior ')
        class_chosen = False
        while class_chosen == False:
        
            if character_class[0].lower() == 'm':
                character_class = 'Mage'
                class_chosen = True
            elif character_class[0].lower() == 'r':
                character_class = 'Rogue'
                class_chosen = True
            elif character_class[0].lower() == 'h':
                character_class = 'Hunter'
                class_chosen = True
            elif character_class[0].lower() == 'w':
                character_class = 'Warrior'
                class_chosen = True
            else:
                character_class = input('Sorry, I dont understand.  Please choose a class: Mage, Rogue, Hunter, Warrior ')
        
        self.health = health[character_class]
        self.dmg_range = dmg_range[character_class]
        self.character_class = character_class

def char_attacks():

    if new_char.character_class.lower()[0] == 'm':
        for i in mage_attacks:
            print(str(i[0]) + ' does ' + str(i[2]) + ' damage with a hit chance of ' + str(i[1]) + ' %.')

    if new_char.character_class.lower()[0] == 'r':
        for i in rogue_attacks:
            print(str(i[0]) + ' does ' + str(i[2]) + ' damage with a hit chance of ' + str(i[1]) + ' %.')

    if new_char.character_class.lower()[0] == 'h':
        for i in hunter_attacks:
            print(str(i[0]) + ' does ' + str(i[2]) + ' damage with a hit chance of ' + str(i[1]) + ' %.')

    if new_char.character_class.lower()[0] == 'w':
        for i in warrior_attacks:
            print(str(i[0]) + ' does ' + str(i[2]) + ' damage with a hit chance of ' + str(i[1]) + ' %.')

class Boss:
    
    def __init__(self):
        
        self.boss = boss
        self.boss_health = boss_health['Dragon']
        self.boss_dmg_range = boss_dmg_range['Dragon']

def boss_attacks():

    for i in dragon_attacks:
        print(str(i[0]) + ' does ' + str(i[2]) + ' damage with a hit chance of ' + str(i[1]) + ' %.')

def choose_attack():
    
    
    char_attacks()
    attack_choice = input('Choose your attack: ')
    
    if new_char.character_class.lower()[0] == 'm':
        if attack_choice.lower()[0] == 'f':
            new_boss.boss_health = new_boss.boss_health - 40
            print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
        elif attack_choice.lower()[0] == 'a':
            if random.randint(0,100) <= 70:
                new_boss.boss_health = new_boss.boss_health - 60
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
        elif attack_choice.lower()[0] == 'p':
            if random.randint(0,100) <= 50:
                new_boss.boss_health = new_boss.boss_health - 90
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
                
    elif new_char.character_class.lower()[0] == 'r':
        if attack_choice.lower()[0] == 's':
            new_boss.boss_health = new_boss.boss_health - 40
            print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
        elif attack_choice.lower()[0] == 'a':
            if random.randint(0,100) <= 80:
                new_boss.boss_health = new_boss.boss_health - 50
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
        elif attack_choice.lower()[0] == 'm':
            if random.randint(0,100) <= 60:
                new_boss.boss_health = new_boss.boss_health - 80
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')

    elif new_char.character_class.lower()[0] == 'h':
        if attack_choice.lower()[0] == 's':
            new_boss.boss_health = new_boss.boss_health - 35
            print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
        elif attack_choice.lower()[0] == 'e':
            if random.randint(0,100) <= 80:
                new_boss.boss_health = new_boss.boss_health - 50
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
        elif attack_choice.lower()[0] == 'a':
            if random.randint(0,100) <= 70:
                new_boss.boss_health = new_boss.boss_health - 65
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
                
    elif new_char.character_class.lower()[0] == 'w':
        if attack_choice.lower()[0] == 's':
            new_boss.boss_health = new_boss.boss_health - 35
            print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
        elif attack_choice.lower()[0] == 'm':
            if random.randint(0,100) <= 80:
                new_boss.boss_health = new_boss.boss_health - 50
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')
        elif attack_choice.lower()[0] == 'e':
            if random.randint(0,100) <= 30:
                new_boss.boss_health = new_boss.boss_health - 100
                print('Good hit! The boss now has {} health remaining'.format(new_boss.boss_health))
            else:
                print('Attack missed.')

def boss_attack():
    
    num = random.randint(0,100)
    print(num)
    
    if num in range(0,40):
        print('The dragon used {}!'.format(dragon_attacks[0][0]))
        if random.randint(0,100) <= 90:
            print('It hit you!')
            new_char.health = new_char.health - 20
            print('You have {} health remaining'.format(new_char.health))
        else:
            print("The dragon's attack missed.")
    elif num in range(41,70):
        print('The dragon used {}!'.format(dragon_attacks[1][0]))
        if random.randint(0,100) <= 60:
            print('It hit you!')
            new_char.health = new_char.health - 40
            print('You have {} health remaining'.format(new_char.health))
        else:
            print("The dragon's attack missed.")
    elif num in range(71,100):
        print('The dragon used {}!'.format(dragon_attacks[2][0]))
        if random.randint(0,100) <= 20:
            print('It hit you!')
            new_char.health = new_char.health - 100
            print('You have {} health remaining'.format(new_char.health))
        else:
            print("The dragon's attack missed.")
    

while True:
    
    instructions = input("Welcome to The Dragon's Lair.  Do you need game instructions? Please enter Yes or No")
    if instructions.lower()[0] == 'y':
        print('You can choose from 4 classes: Mage, Rogue, Hunter, or Warrior. \n Each class has 3 abilities, with higher damage abilities having a higher chance to miss. \n You must defeat the dragon before your health reaches zero!')
    else:
        pass
    
    #Character Selection:
    new_char = Character()
    
    print('You have selected to play as a {}'.format(new_char.character_class))
    print('Here are your abilities: ')
    char_attacks()
    
    print('You are beginning with {} health.'.format(new_char.health))
    
    new_boss = Boss()
    waiting = True
    while waiting:
        
        play_game = input('Are you ready to enter the dragons Lair? Y/N')
        if play_game.lower()[0] == 'y':
            print('You enter into the mouth of the cave, which strangely looks like an actual dragon jaw...')
            waiting = False
        else:
            print("Good idea.  Only enter the cave once you've properly prepared")
            waiting = True
            time.sleep(5)
    time.sleep(7)
    
    print('You feel the ground shake, when suddenly "Dendragosa, The World-Ender" lands before you!')
#    combat = True
    player_turn = True
    dragon_turn = False
    while new_boss.boss_health >0 and new_char.health >0:
        
        '''
        if new_boss.boss_health <= 0:
            print('The dragon has been defeated! Victory is yours.')
            combat = False
            break
            
        elif new_char.health <= 0:
            print('You have been slain by the dragon.  May your soul rest in Valhalla.')
            combat = False
            break
        '''    

        if player_turn == True:
            
            time.sleep(3)
            choose_attack()
            time.sleep(3)
            if new_boss.boss_health >0 and new_char.health >0:
                player_turn = False
                dragon_turn = True
           # elif new_boss.boss_health <= 0:
               # combat = False
                
            
        elif dragon_turn == True:
            
            time.sleep(3)
            boss_attack()
            time.sleep(3)
            if new_char.health > 0 and new_boss.boss_health > 0:
                dragon_turn = False
                player_turn = True
           # elif new_char.health <= 0:
             #   combat = False

    if new_boss.boss_health <= 0:
        print('You have defeated the dragon.  Victory is yours!')
        
    elif new_char.health <= 0:
        print('You have been slain by the dragon.  May your soul rest in Valhalla.')
        
        
    
    
    
    new_game = input('Would you like to play again? y/n')
        
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break
    