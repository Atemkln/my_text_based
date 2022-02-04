import game_engine,random,time

class User:
    def __init__(self,name,attack,kindness,luck,health,statluck):
        self.name = name
        self.attack = attack
        self.kindness = kindness
        self.luck = luck
        self.health = health
        self.statluck = statluck

class Enemy:
    def __init__(self,name,health,attack,kindness,luck,intro_dialogue,
    attack_dialogue,kindness_dialogue,luck_dialogue,winning_dialogue,losing_dialogue,luckstat):
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
        self.luckstat = luckstat
    
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
        if total_luck > self.luckstat:
            game_engine.display_line(f"Oh no!\n{self.name} has manipulated the twisting sands of FATE!")
            game_engine.display_line(f"You have lost this encounter,",get=2)
            game_engine.display_line(f"Perhaps your descendents will fare better...")
            return 1
        else:
            game_engine.display_line(f"What luck!\n{self.name} was unable to beat the odds!")
            return 0

    def enemy_action(self):
        action = random.randint(0,1)
        if action == 0:
            out = self.enemy_attack()
        elif action == 1:
            out = self.enemy_luck()
        return out

me = User("Mystagen",10,8,7,80,90)

ghoul = Enemy("GHOUL",50,13,2,10,"'BoooOooO! I'm gonna succ you!'","'Suck on this!'","'Treats for your pretty??!!'",
"'Brrrrrrr...'", "'HAhahaha....get spooooooOOOOOkeed!'","'AOOWWWAOOAOAHHHH!! NO!!'",100)

salesperson = Enemy("OVERLY-FRIENDLY VACUUM SALESPERSON",70,15,30,5,"'CAN I INT$RE$T YOU IN OUR WARRANTY PLAN!!'","'CHOP THO$E PRIC$S!!$$!'","'M$$T M$ IN THE MIDDL$ H$R$!!'",
"'LET$ PLAY THE GAM$ OF LIF$$$!!'", "'SIGN H$R$ PL$AS$!!:)))'","'NOO!! MY BOTTOM LIN$$$!!:((('",100)

enemies = {"GHOUL":ghoul,"OVERLY-FRIENDLY VACUUM SALESPERSON":salesperson}
