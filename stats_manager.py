import game_engine,random

class User:
    def __init__(self,name,attack,kindness,luck,health):
        self.name = name
        self.attack = attack
        self.kindness = kindness
        self.luck = luck
        self.health = health

class Enemy:
    def __init__(self,name,health,attack,kindness,luck,intro_dialogue,
    attack_dialogue,kindness_dialogue,luck_dialogue,winning_dialogue,losing_dialogue):
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
    
    def enemy_introduction(self):
        game_engine.display_line(self.intro_dialogue)

    def enemy_attack(self, user_health):
        attack_modifier = random.randint(1,5)
        total_attack = attack_modifier + self.attack
        user_health -= total_attack
        game_engine.display_line(self.attack_dialogue)
        game_engine.display_line(f"{self.name} hits you for {total_attack} DAMAGE!")
        return user_health

    def enemy_luck(self,luckstat):
        luck_modifier = random.randint(1,100)
        total_luck = luck_modifier + self.luck
        game_engine.display_line(self.luck_dialogue)
        game_engine.display_line(f"{self.name} takes a chance!")
        if total_luck > luckstat:
            game_engine.display_line(f"Oh no!\n{self.name} has manipulated the twisting sands of FATE!")
        else:
            game_engine.display_line(f"What luck!\n{self.name} was unable to beat the odds!")

me = User("Mystagen",10,8,7,300)

ghoul = Enemy("GHOUL",50,7,2,10,"'BoooOooO! I'm gonna succ you!'","'Suck on this!'","'Treats for your pretty??!!'",
"'Brrrrrrr...'", "'HAhahaha....get spooooooOOOOOkeed!'","'AOOWWWAOOAOAHHHH!! NO!!'")

salesperson = Enemy("OVERLY-FRIENDLY VACUUM SALESPERSON",150,15,30,15,"'CAN I INT$RE$T YOU IN OUR WARRANTY PLAN!!'","'CHOP THO$E PRIC$S!!$$!'","'M$$T M$ IN THE MIDDL$ H$R$!!'",
"'LET$ PLAY THE GAM$ OF LIF$$$!!'", "'SIGN H$R$ PL$AS$!!:)))'","'NOO!! MY BOTTOM LIN$$$!!:((('")

enemies = {"GHOUL":ghoul, "OVERLY-FRIENDLY VACUUM SALESPERSON":salesperson}
