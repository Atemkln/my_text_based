import game_engine,random,time

attack_adj = ["HEROIC","GRUESOME","FRIGHTFUL","TIMID","ELEGANT","SMOOTH","BOMBASTIC","RELIGIOUS","IDEOLOGICAL"] #combat adjectives used in user_attack 
victory_adj = ["HOORAH!","YAHOO!","HIYAH!","AGGHH!","SLURP!","WHAM!","POW!","BLAM!","WAP!","SLARG!","WOOSH!"] #successful hit adjectives used in user_attack
kind_adj = ["LOVE!","PEACE!","BALANCE!","UNITY!","DIVERSITY!","DALI LAMA!"] #kindness adjectives used in user_kindness 

#player character attributes and combat functions:
class User: 
    def __init__(self,name,attack,kindness,luck,health,statluck,meanvalue,victory_speech):
        self.name = name
        self.attack = attack
        self.kindness = kindness
        self.luck = luck 
        self.health = health
        self.statluck = statluck #the LUCK value that the enemy must beat (111)
        self.meanvalue = meanvalue #value that the enemy must beat during their KINDNESS check
        self.victory_speech = victory_speech #text when player wins

#player character attacks enemy, and subtracts health from them                                                                                                                            
    def user_attack(self,enemy):
        attribute = random.choice(attack_adj)
        victory = random.choice(victory_adj)
        attack_modifier = random.randint(1,7)
        attack_modifier += self.attack
        enemy.health -= attack_modifier
        game_engine.display_line(f"You ready a {attribute} attack!")
        game_engine.display_line("3...\n2...\n1...", get=2)
        game_engine.display_line(f"{victory}", get=2)
        game_engine.display_line(f"{attack_modifier} DMG!")
        game_engine.display_line(enemy.losing_dialogue)
        if enemy.health > 0: #win condition
            return 0
        else:
            return 1

#player character does a kindness check vs enemy meanvalue
    def user_kindness(self,enemy):
        kind_mod = random.randint(1,3)
        kind_mod += self.kindness 
        kind_choice = random.choice(kind_adj)
        game_engine.display_line("Awww...you have chosen the path of kindness! :P")
        game_engine.display_line("Good KARMA certainly awaits you...")
        game_engine.display_line("3...\n2...\n1...", get=2)
        game_engine.display_line(kind_choice)
        if kind_mod >= enemy.meanvalue:
            enemy.health //= 2
            game_engine.display_line(f"{enemy.name} is hit with the full FORCE of your KINDNESS!")
            game_engine.display_line(f"HP is reduced by half! :P")
        else:
            self.health //= 2
            game_engine.display_line(f"Oh no!\nYour KINDNESS was unable to break through...")
            game_engine.display_line(f"Your HP has been reduced by half :(...")
        return 0

    
    def user_luck(self,enemy):
        luck_mod = random.randint(1,100)
        luck_total = luck_mod + self.luck
        game_engine.display_line(f"You prepare to brave the cruel tides of FATE!")
        game_engine.display_line("3...\n2...\n1...", get=2)
        time.sleep(3)
        if luck_total > enemy.statluck:
            game_engine.display_line(f"FORTUNE smiles upon you this day, {self.name}.") 
            game_engine.display_line(f"{enemy.name} has been subjected to outrageous fortune!", get=2) 
            game_engine.display_line("You have won the encounter!") 
            return 1 
        else:
            game_engine.display_line(f"The GAMBLERS PARADOX is certainly a lofty one...",get=2)  
            game_engine.display_line(f"Lady Luck is not in your corner today, {enemy.name}.")  
            return 0

class Enemy:
    def __init__(self,name,health,attack,kindness,luck,intro_dialogue,
    attack_dialogue,kindness_dialogue,luck_dialogue,winning_dialogue,losing_dialogue,statluck,meanvalue):
        self.name = name
        self.health = health
        self.attack = attack
        self.kindness = kindness
        self.luck = luck
        self.intro_dialogue = intro_dialogue
        self.attack_dialogue = attack_dialogue
        self.kindness_dialogue = kindness_dialogue
        self.luck_dialogue = luck_dialogue
        self.winning_dialogue = winning_dialogue
        self.losing_dialogue = losing_dialogue
        self.statluck = statluck
        self.meanvalue = meanvalue
    
    def enemy_introduction(self):
        game_engine.display_line(self.intro_dialogue)

    def enemy_attack(self):
        attack_modifier = random.randint(1,5)
        attack_modifier += self.attack
        game_engine.display_line(self.attack_dialogue)
        game_engine.display_line(f"{self.name} hits you for {attack_modifier} DAMAGE!")
        me.health -= attack_modifier
        if me.health <= 0:
            game_engine.display_line(f"You have been KILLED, {me.name}...")
            game_engine.display_line(f"You have lost this battle.") 
            return 1
        else:
            game_engine.display_line(f"You have only {me.health} HP remaining!")
            return 0

    def enemy_luck(self):
        luck_modifier = random.randint(1,100)
        total_luck = luck_modifier + self.luck
        game_engine.display_line(self.luck_dialogue)
        game_engine.display_line(f"{self.name} takes a chance!")
        game_engine.display_line("3...\n2...\n1...", get=2)
        time.sleep(3)
        if total_luck > me.statluck:
            game_engine.display_line(f"Oh no!\n{self.name} has manipulated the twisting sands of FATE!")
            game_engine.display_line(f"You have lost this encounter,",get=2)
            game_engine.display_line(f"Perhaps your descendents will fare better...")
            return 1
        else:
            game_engine.display_line(f"What luck!\n{self.name} was unable to beat the odds!")
            return 0

    def enemy_kindness(self):
        kind_mod = random.randint(1,3)
        kind_mod += self.kindness
        kind_choice = random.choice(kind_adj)
        game_engine.display_line(self.kindness_dialogue)
        game_engine.display_line(f"{self.name} is choosing the path of KINDNESS!")
        game_engine.display_line("Good KARMA certainly awaits them...")
        game_engine.display_line("3...\n2...\n1...", get=2)
        game_engine.display_line(kind_choice)
        if kind_mod >= me.meanvalue:
            me.health //= 2
            game_engine.display_line("You are hit with the full FORCE of their KINDNESS!")
            game_engine.display_line("Your HP is reduced by half! :P")
        else:
            self.health //= 2
            game_engine.display_line(f"Nice try!\n{self.name}'s KINDNESS was unable to break through...")
            game_engine.display_line(f"Its HP has been reduced by half :)...")
        return 0

    def enemy_action(self):
        action = random.randint(0,3)
        if action == 0 or action == 1:
            out = self.enemy_attack()
        elif action == 2:
            out = self.enemy_luck()
        else:
            out = self.enemy_kindness()
        return out

me = User("Mystagen",10,1,7,80,90,4,"You have killed it.") 

ghoul = Enemy("GHOUL",50,13,0,10,"'BoooOooO! I'm gonna succ you!'","'Suck on this!'","'Treats for your pretty??!!'",
"'Brrrrrrr...'", "'HAhahaha....get spooooooOOOOOkeed!'","'AOOWWWAOOAOAHHHH!! NO!!'",100,10)

npc = Enemy("NPC",100,6,1,3,"'Hi there! I am decidedly average...'","'I'm a BLUE-BELT, I'll have you know!'",
"'Hey, PAL. We can forsure work this out without resorting to violence...'","'I guess I'll try this? Haha...'"
,"'The only thing worse than a SORE LOSER, is a POOR WINNER. Bring it in, pal...'","'OW! Well...at least I have good COVERAGE...'",100,4)

salesperson = Enemy("OVERLY-FRIENDLY VACUUM SALESPERSON",70,15,4,5,"'CAN I INT$RE$T YOU IN OUR WARRANTY PLAN!!'","'CHOP THO$E PRIC$S!!$$!'","'M$$T M$ IN THE MIDDL$ H$R$!!'",
"'LET$ PLAY THE GAM$ OF LIF$$$!!'", "'SIGN H$R$ PL$AS$!!:)))'","'NOO!! MY BOTTOM LIN$$$!!:((('",100,1000)

enemies = {"GHOUL":ghoul,"OVERLY-FRIENDLY VACUUM SALESPERSON":salesperson,"NPC":npc}
