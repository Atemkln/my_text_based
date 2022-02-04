import game_engine,random,stats_manager,time

attack_adj = ["HEROIC","GRUESOME","FRIGHTFUL","TIMID","ELEGANT","SMOOTH","BOMBASTIC","RELIGIOUS","IDEOLOGICAL"]
victory_adj = ["HOORAH!","YAHOO!","HIYAH!","AGGHH!","SLURP!","WHAM!","POW!","BLAM!","WAP!","SLARG!","WOOSH!"]

def user_attack(user,monster):
    attribute = random.choice(attack_adj)
    victory = random.choice(victory_adj)
    attack_modifier = random.randint(1,7)
    attack_modifier += user.attack
    monster.health -= attack_modifier
    game_engine.display_line(f"You ready a {attribute} attack!")
    game_engine.display_line("3...\n2...\n1...", get=2)
    game_engine.display_line(f"{victory}", get=2)
    game_engine.display_line(f"{attack_modifier} DMG!")
    game_engine.display_line(monster.losing_dialogue)
    if monster.health > 0:
        combat_menu(user,monster)
    else:
        game_engine.display_line("You have killed it.")     

def user_luck(user,monster,statluck):
    luck_mod = random.randint(1,100)
    luck_total = luck_mod + user.luck
    game_engine.display_line(f"You prepare to brave the cruel tides of FATE!")
    game_engine.display_line("3...\n2...\n1...", get=2)
    time.sleep(3)
    if luck_total > statluck:
        game_engine.display_line(f"FORTUNE smiles upon you this day, {user.name}.") 
        game_engine.display_line(f"{monster.name} has been subjected to outrageous fortune!", get=2) 
        game_engine.display_line("You have won the encounter!")  
    else:
        game_engine.display_line(f"The GAMBLERS PARADOX is certainly a lofty one...",get=2)  
        game_engine.display_line(f"Lady Luck is not in your corner today, {user.name}.")  
        combat_menu(user,monster)

def user_choice(user,monster):
    choice = game_engine.display_line("What will you do?: ", get=1)
    print("")
    if choice == '0':
        user_attack(user,monster)
    elif choice == '1':
        user_luck(user,monster,100)          

def combat_menu(user,monster):
    loss_condition = monster.enemy_action()
    if loss_condition == 0:
        game_engine.display_line(f"{user.name} stats --\n\nATK: {user.attack}\nKIND: {user.kindness}\nLUCK: {user.luck}\n\n{user.name}!",get=2)
        user_choice(user,monster)
    else:
        pass

def combat_encounter(user,monster):
    game_engine.display_line(f"You are challenged by {monster.name}!")
    combat_menu(user,monster)

