import game_engine,random,stats_manager,time

attack_adj = ["HEROIC","GRUESOME","FRIGHTFUL","TIMID","ELEGANT","SMOOTH","BOMBASTIC","RELIGIOUS","IDEOLOGICAL"]
victory_adj = ["HOORAH!","YAHOO!","HIYAH!","AGGHH!","SLURP!","WHAM!","POW!","BLAM!","WAP!","SLARG!","WOOSH!"]

def user_attack(user,monster):
    attribute = random.choice(attack_adj)
    victory = random.choice(victory_adj)
    game_engine.display_line(f"You ready a {attribute} attack!")
    game_engine.display_line("3...\n2...\n1...", get=2)
    game_engine.display_line(f"{victory}")
    game_engine.display_line(monster.losing_dialogue)

def user_luck(user,monster,statluck):
    luck_mod = random.randint(1,100)
    luck_total = luck_mod + user.luck
    game_engine.display_line(f"You prepare to brave the cruel tides of FATE!")
    game_engine.display_line("3...\n2...\n1...", get=2)
    time.sleep(2)
    if luck_total > statluck:
        game_engine.display_line(f"FORTUNE smiles upon you this day, {user.name}.") 
        game_engine.display_line(f"{monster.name} has been subjected to outrageous fortune!", get=2) 
        game_engine.display_line("You have won the encounter!")  
    else:
        game_engine.display_line(f"The GAMBLERS PARADOX is certainly a lofty one...")  
        game_engine.display_line(f"Lady Luck is not in your corner today, {user.name}.")  
        combat_menu(user,monster)

def user_choice(user,monster):
    choice = game_engine.display_line("What will you do?: ", get=1)
    print("")
    if choice == '0':
        user_attack(user,monster)
        attack_value = monster.enemy_attack()
        stats_manager.me.health -= attack_value
        game_engine.display_line(f"You have only {stats_manager.me.health} HP remaining!")
        combat_menu(user,monster)
    elif choice == '1':
        user_luck(user,monster,40) 
    else:
        combat_menu(user,monster)
    
def combat_menu(user,monster):
    game_engine.display_line(f"{user.name} stats --\n\nATK: {user.attack}\nKIND: {user.kindness}\nLUCK: {user.luck}\n\n{user.name}!",get=2)
    user_choice(user,monster)

def combat_encounter(user,monster):
    game_engine.display_line(f"You are challenged by {monster.name}!")
    combat_menu(user,monster)

