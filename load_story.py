import pickle

part1 = {
    1: {
      'Text': [
            "Oh, uh hey.",
            "I just wanted to say sorry about last night...",
            "I usually don't get that drunk and sad, but its been a rough week.",
            "...",
            "Could you ever find it in your heart to forgive me?"
        ],
      'Options': [
          ("Yes of course.", 2),
          ("I'm sorry I dont remember anything. Who are you?", 3)
        ]
    },
    2: {    
        'Text': [
            "Ah, that's good. That's...uh...",
            "...",
            "Anyways...",
            "What should we do about it?",
            "About, y'know, the thing."
        ],
        'Options': [
          ("What thing? What are you talking about?", 4),
          ("We should destroy it.", 5),
          ("We should go get it.", 6)
        ]
    },
    3: {
        'Text': [
            "Ah...shit",
            "Yo!!",
            "The kid is awake but they're acting all dopey and stuff!",
            "...",
            "Hey kid, any idea how to cure a hangover?"
        ],
        'Options': [
          ("How did you get it?", 6),
          ("Nah, no clue.", 5)
        ]
    },
    4: {
      'Text': [
            "The what? The thing? What did I say-",
            "Ohhh...",
            "I meant the @#$%&! thing.",
            "...You know what that is right?"
        ],
      'Options': [
        ("Nah, no clue.", 5),
        ("What do you mean?! All you showed me was a bunch of random characters!", 5)
      ]
    },
    5: {
      'Text': [
            "Yeah, I figured you wouldn't know haha.",
            "But whatever, I'm just messing with you.",
            "In any case, answer me this:",
            "You're in a burning building, and there's an orphanage on the 3rd floor...",
            "And a retirement home on the 1st.",
            "You can only save one person from one of the floors.", 
            "Who are you picking?"
        ],
      'Options': [
        ("I don't get it.", 6),
        ("What does this have to do with where we are now?", 7)
      ]
    },
    6: {
      'Text': [
            "Get it?",
            "What the hell are you talking about?",
            "Friendo...",
            "Do you even know where you are right now?",
        ],
      'Options': [
        ("...", 8),
        ("...",8)
        ]
    },
    7: {
      'Text': [
            "Hm...",
            "Well friendo,",
            "I guess you'll find out as soon as the flames find you.",
        ],
      'Options': [
        ("...", 8),
        ("...",8)
      ]
    },
    8: {
      'Text': [
            "PART 1",
            "BLAZE OF GLORY",
            "I guess you'll find out as soon as the flames find you...",
        ],
      'Options': []
    },
}

with open('part1.ch', 'wb') as chapter:
  pickle.dump(part1, chapter)

part2 = {
  1: {
      'Text': [
            "The leaves blew hurridly across the concrete streets.",
            "Circling overhead was a dark and gloomy sky.",
            "'These are mean streets' is how my partner would have put it.",
            "Mean streets, indeed.",
            "They were shot a few years back,",
            "Didn't fully kill 'em, but they were never the same after that.",
            "I had failed to realize the magnitude of that event at the time.",
            "At that time I'm pretty sure I saw most people like how some would see puzzle pieces,",
            "Trying to understand how each one fit with the other.",
            "...",
            "'I need a coffee.'", 
            "'And a haircut.'",
            "'And a cigarette.'",
            "...",
            "Haaah.",
        ],
      'Options': [
          ("Go to the diner", 2),
          ("Go to the haircut", 3),
          ("Go to the cigarette", 4)
        ]
    },
}

with open('part2.ch', 'wb') as chapter:
  pickle.dump(part2, chapter)