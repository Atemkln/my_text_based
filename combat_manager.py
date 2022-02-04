import game_engine

def user_choice(user,monster):
    choice = game_engine.display_line("What will you do?: ", get=1)
    print("")
    if choice == '0':
        checka = user.user_attack(monster)
        if checka != 0:
            game_engine.display_line(user.victory_speech)
        else:
            combat_menu(user,monster)
    elif choice == '1':
        user.user_kindness(monster)
        combat_menu(user,monster)    
    else:
        checkb = user.user_luck(monster)
        if checkb != 0:
            game_engine.display_line(user.victory_speech)
        else:
            combat_menu(user,monster)

def combat_menu(user,monster):
    loss_condition = monster.enemy_action()
    if loss_condition == 0:
        print(f"{user.name} stats --\n\nATK: {user.attack}\nKIND: {user.kindness}\nLUCK: {user.luck}\nHP: {user.health}\n")
        game_engine.display_line(f"0 for ATK\n1 for KIND\n2 for LUCK\n\n{user.name}!",get=2)        
        user_choice(user,monster)
    else:
        pass

def combat_encounter(user,monster):
    game_engine.display_line(f"You are challenged by {monster.name}!")
    game_engine.display_line(monster.intro_dialogue)
    combat_menu(user,monster)

