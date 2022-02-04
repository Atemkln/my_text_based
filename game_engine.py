import sys,time,getpass,story_data,combat_manager,stats_manager
from typing import Any

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def slow_type(t, space=True):
  typing_speed = 12000 #wpm
  for l in t:
      flush_input()
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(10.0/typing_speed)
  if space:
   print("")

def get_input(valid_input: list):
  count = 0
  while True:
    user_entered = getpass.getpass("")
    if user_entered not in valid_input and count == 0:
      slow_type("Hey inputs need to be VALID!!!")
      count += 1
      user_entered = None
    elif user_entered not in valid_input and count == 1:
      slow_type("Seriously...you need to focus...")
      count += 1
      user_entered = None
    elif user_entered not in valid_input and count == 2:
      slow_type("Hahaha...you're hopeless.")
      user_entered = None    
    else:
      return user_entered

def display_line(line, get=0):
    if get == 0:
      slow_type(line)
      choice0 = get_input([""])
      return choice0
    elif get == 1:
      slow_type(line,space=False)
      choice1 = get_input(["0","1","2"])
      return choice1
    elif get == 2:
      slow_type(line)
      print("")

def get_response(options: list):
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
  
  valid_inputs = [str(num) for num in range(len(options))]

  option_index = int(get_input(valid_inputs))

  return options[option_index][1]

def story_flow(story: dict):
  curr_page = 1

  while curr_page != None:
    page = story.get(curr_page, Any)
    
    if page == None:
      break

    for line in page['Text']:
      if line[0] != '|':
        display_line(line)
      else:
        combat_manager.combat_encounter(stats_manager.me,stats_manager.enemies[line[1:]])

    if len(page['Options']) == 0:
      curr_page = None
      break

    curr_page = get_response(page['Options'])
  
if __name__=='__main__':
    story_flow(story_data.part1)
    story_flow(story_data.part2)