import game_engine,random,stats_manager

def user_choice():
    game_engine.display_line("What will you do?: ", get=1)

attack_adj = ["HEROIC", "GRUESOME", "FRIGHTFUL", "TIMID", "ELEGANT", "SMOOTH", "BOMBASTIC", "RELIGIOUS", "IDEOLOGICAL"]
def combat_menu(user,monster):
    game_engine.display_line(f"{user.name} stats --\n\nATK: {user.attack}\nKIND: {user.kindness}\nLUCK: {user.luck}\n\n{user.name}!")
    choice = user_choice()
    if choice == 0:
        user_attack(stats_manager.me)

def combat_encounter(user,monster):
    game_engine.display_line(f"You are challenged by {monster.name}!")
    combat_menu(user,monster)

def user_attack(user):
    attribute = random.choice(attack_adj)
    game_engine.display_line(f"You ready a {attribute} attack!")
    game_engine.display_line("3...\n2...\n1...", get=2)
    game_engine.display_line("WOWIE!")


