import sys,time,random,getpass,os,story_data
from typing import Any

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def slow_type(t):
  typing_speed = 120 #wpm
  for l in t:
      flush_input()
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(10.0/typing_speed)
  print("")

def get_input(valid_input: list):
  count = 0
  while True:
    user_entered = getpass.getpass("")
    if user_entered not in valid_input and count == 0:
      slow_type("Hey come on now, get serious!")
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

def display_page_text(lines: list):
  for line in lines:
    slow_type(line)
    get_input([""])

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
      curr_page = None
      break

    display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      break

    curr_page = get_response(page['Options'])
   
if __name__=='__main__':
    story_flow(story_data.part1)
    story_flow(story_data.part2)