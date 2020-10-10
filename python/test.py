import time
import random

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def time_print(string):
    print(string)
    time.sleep(1)

def time_print_loop(lst):
    for i in range(len(lst)):
        time_print(lst[i])

def valid_input(promt, option1, option2):
    while True:
        response = input(promt).lower()
        if option1 in response:
            return option1
        if option2 in response:
            return option2
        else:
            time_print("Sorry, I don't understand.")
    return response

def boss_attack(stats):    
    if stats['boss_name'] == 'Big Boi':
        dmg = die_roll() + die_roll() 
    else:
        dmg = die_roll() * 2 
    stats['player_hp'] -= dmg
    lst = [
        f"{stats['boss_name']} unsheaths his sword, darts twards you, and slashes you with a swift blow.",
        f"{stats['boss_name']} hits you for {dmg} damage points.", 
        f"your health is now at {stats['player_hp']}"
        ]
    time_print_loop(lst)
    if stats['player_hp'] > 0:
        answer = valid_input('Continue fighting or flee the battle? Type flee or fight.\n', 'fight', 'flee')
        if answer == "fight":
            time_print(f'''{stats['player_name']} - "I will not back down!"''')
            who_attacks(stats)
        elif answer == "flee":
            lst = [
                f'''{stats['player_name']} - "Im in over my head."''', 
                f"{stats['player_name']} runs from the battle and escape Boss.", 
                "You live to fight another day."
                ]
            time_print_loop(lst)
            town(items)
    else:
        time_print('You have died')
        
def player_attack(stats):
    if stats['boss_name'] == 'Big Boi':
        dmg = die_roll() * 2
    else:
        dmg = die_roll() + die_roll() 
    stats['boss_hp'] -= dmg
    lst = [
        f"{stats['player_name']} bolts toward {stats['boss_name']}, lifting oath breaker above his head, and then stricks {stats['boss_name']} with a heavy blow",
        f"You hit {stats['boss_name']} for {dmg} damage points.",
        f"{stats['boss_name']}'s health is now at {stats['boss_hp']}"
        ]
    time_print_loop(lst)
    if stats['boss_hp'] > 0:
        time_print(f'''{stats['boss_name']} - "Not bad!"''')
        who_attacks(stats)
    else:
        time_print('You have Won!')
        
def who_attacks(stats):    
    result = coin_flip()
    if result == 'heads':
        player_attack(stats)
    elif result == 'tails':
        boss_attack(stats)
    else:
        who_attacks(stats)

def intro_fight():    
    time_print('You are both still, waiting for the right time to make your move, and then...')


def choose_stats(items):
    opt1 = {
        'boss_hp': 10, 
        'player_hp': 10,
        'boss_name': 'Big Boi',
        'player_name':'None'
        }
    opt2 = {
        'boss_hp': 10, 
        'player_hp': 10, 
        'boss_name': 'Small Boi',
        'player_name':'None'
        }
    if items['key'] == '1':
        opt1['player_name'] = items['player_name']
        stats = opt1
    else:
        opt2['player_name'] = items['player_name']
        stats = opt2
    return stats
     
def fight(items):
    intro_fight()
    who_attacks(choose_stats(items))
    play_again()

def play_again():
    time_print("Would you like to play again?")
    replay = valid_input("Type (yes) or (no).", "yes", "no")
    if replay == "yes":
        play()
    elif replay == "no":
        time_print("Ok thanks for playing")
# Story ------------------------------------------------------------>

def get_name(items):
    items['player_name'] = input("To start enter your name\n")
    return items

def intro_story():
    lst = [
        "A brave warrior wonders the world to find great power.",
        "their journey leads them to a small town hidden at the peak of a mountain.",
        "Two great masters reside there. ",
        "One has mastered the forces of nature.",
        "The other is a master of spiritual energy.",
        "An important decision is in front of you...\n"
        ]
    time_print_loop(lst)    

def location(items):
    lst = [
        f"What do you wan't to do {items['player_name']}?",
        "Type (1) to go see the master of nature.",
        ]
    time_print_loop(lst)
    number = input("Type (2) to go see the master of spirit.\n")
    return number

def town(items):
    choice = location(items)
    if choice == '1':
        first(items)
    elif choice == '2':
        second(items)
    else:
        town(items)
    
def first(items):
    time_print("You find yourself in front of a small wooden house surrounded by tall grass and giant oak trees.")
    if items['key'] == '1':
        lst = [
            "Boss isn't home right now.",
            "There doesn't seem to be much to do here.",
            "You head back into town."
            ]
        time_print_loop(lst)
        town(items)
    elif items['key'] == '2':
        lst = [
            "Boss comes out to greet you and notices '2' on you.",
            "She understands why you have come.",
            '''Boss- "I will not be intimidated by one of Boss's thugs."''', 
            "Boss gets into a fighting stace and starts to glow bright green."
            ]
        time_print_loop(lst)
        fight(items)
    else:
        lst = [
            "Boss greets you.",
            "She peers curiously into your eyes and senses your pure heart.",
            "She asks you to be her student and to learn the ways of nature.",
            "Will you accept her offer?"
            ]
        time_print_loop(lst)
        answer = valid_input("Type (yes) or (no).\n", "yes", "no")
        if answer == "yes":
            lst1 = [
                "For the next year you spend every day with boss learning the ways of nature.",
                "You learn that she and the town have been under attack from Boss for many years.",
                "She wants you to end his reign of terror once and for all.",
                "She opens her hands, they glow bright green as she places them over your chest and says...",
                '"This is my most powerful technique name."',
                '"You are ready to face boss."',
                '"Go defeat him!"\n',
                "*You have gain the power of technique!*\n"
                ]
            time_print_loop(lst1)
            items['key'] = '1'
            time_print("With the training from boss and the power of technique, you leave and head into town.")
            town(items)
        elif answer == "no":
            lst2 = [
                '''Boss - "I hope you will reconsider my offer." ''',
                "You leave the small house and return home."
                ]
            time_print_loop(lst2)
            town(items)

def second(items):
    time_print("You find yourself in front of a large stone house surrounded by ancient sculpturs with characters carved into them.")
    if items['key'] == '2':
        lst = [
            "Boss isn't home right now.",
            "There doesn't seem to be much to do here.",
            "You head back into town."
            ]
        time_print_loop(lst)
        town(items)
    elif items['key'] == '1':
        lst = [
            "Boss comes out to greet you and notices '1' on you.",
            "He smiles at you and begins to glow bright red.",
            '''Boss- "I want the power of technique and i will crush you to take it."''', 
            "Boss gets into a fighting stance."
            ]
        time_print_loop(lst)
        fight(items)
    else:
        lst = [
            "Boss greets you.",
            "He sizes you up and senses your desire for power.",
            "He asks you to be his student and to become a spiritual master.",
            "Will you accept his offer?"
            ]
        time_print_loop(lst)
        answer = valid_input("Type (yes) or (no).\n", "yes", "no")
        if answer == "yes":
            lst1 = [
                "For the next year you spend every day with boss learning spiritual techniques .",
                "You learn that he has been trying to take over the town and rule it for years.",
                "He wants you help him by defeating boss, the only peorson truly standing in his way.",
                "He opens his hands, they glow bright red as he places them over your chest and says...",
                '"This is my most powerful technique name."',
                '"You are ready to face boss."',
                '"Go defeat her!"\n',
                "*You have gain the power of technique!*\n"
                ]
            time_print_loop(lst1)
            items['key'] = '2'
            time_print("With the training from boss and the power of technique, you leave and head into town.")
            town(items)
        elif answer == "no":
            lst2 = [
                '''Boss - "I hope you will reconsider my offer." ''',
                "You leave the large stone house and return home."
                ]
            time_print_loop(lst2)
            town(items)

def play():
    items = {
    'key':'', 
    'player_name':''
    }
    get_name(items)
    intro_story()
    town(items)

play()