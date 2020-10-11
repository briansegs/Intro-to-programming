import time
import random

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def time_print(string):
    print(string)
    time.sleep(2)

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

def boss_attack(stats, items):    
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
            who_attacks(stats, items)
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
        
def player_attack(stats, items):
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
        who_attacks(stats, items)
    else:
        time_print('You have Won!')
        
def who_attacks(stats, items):    
    result = coin_flip()
    if result == 'heads':
        player_attack(stats, items)
    elif result == 'tails':
        boss_attack(stats, items)
    else:
        who_attacks(stats, items)

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
    who_attacks(choose_stats(items), items)
    play_again()

def play_again():
    time_print("Would you like to play again?")
    replay = valid_input("Type (yes) or (no).", "yes", "no")
    if replay == "yes":
        play()
    elif replay == "no":
        time_print("Ok thanks for playing!")
# Story ------------------------------------------------------------>

def get_name(items):
    items['player_name'] = input("To start enter your name\n")
    return items

def intro_story():
    lst = [
        "A brave warrior wonders the world in search of great power.",
        "their journey leads them to two sacred mountains divided by a village in a narrow valley.",
        "At the peak of each holy mountain a great master resides.",
        "One has conquered the forces of nature.",
        "The other manipulates spiritual energy.",
        "After a much needed rest in the town's inn, our hero sets out.\n"
        ]
    time_print_loop(lst)    

def location(items):
    lst = [
        f"What do you wan't to do {items['player_name']}?",
        "(1) Traverse the wooded mountain to the east.",
        ]
    time_print_loop(lst)
    number = input("(2) Hike the snow covered mountain to the west.\n")
    return number

def town(items):
    choice = location(items)
    if choice == '1':
        clover(items)
    elif choice == '2':
        Elijah(items)
    else:
        town(items)
    
def clover(items):
    time_print("You find yourself in front of a small wooden house surrounded by tall grass and massive oak trees.")
    if items['key'] == '*Primal Command*':
        lst = [
            "Clover isn't home right now.",
            "There doesn't seem to be much to do here.",
            "You head back into town."
            ]
        time_print_loop(lst)
        town(items)
    elif items['key'] == '2':
        lst = [
            "Clover comes out to greet you and notices '2' on you.",
            "She understands why you have come.",
            '''(Clover) "I will not be intimidated by one of Boss's thugs!"''', 
            "Clover twirls her hands in the air, forming a bright green aura around herself."
            ]
        time_print_loop(lst)
        fight(items)
    else:
        lst = [
            "Clover, brown-haired and slender, with bright, dark eyes, comes out to greet you.",
            "She peers curiously into you and senses your kind heart.",
            f'''(Clover) "{items['player_name']}, I am the master you seek."''',
            '''(Clover) "Train under me and unearth the secrets only I and mother nature know."\n''',
            "Will you accept her offer?"
            ]
        time_print_loop(lst)
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            lst1 = [
                "For the next year you apprentice yourself to Clover, cultivating your skills.",
                "You pickedup that a man named Boss has been trying to steal Clover's power for many years.",
                "You promised Clover that you will bring an end to Boss's reign of terror.",
                "Clover was touched by your commitment.",
                "To conclude your final day of training, Clover requests that you meet her infront of her house.",
                f'''(Clover) "{items['player_name']}, everything that you have endured was to prepare you for this."''',
                '''(Clover) "*Primal Command* is my greatest weapon and now it is yours."''',
                f'''(Clover) "Remember your promise and good luck on your travels {items['player_name']}."\n''',
                "You recieve *Primal Command*\n"
                ]
            time_print_loop(lst1)
            items['key'] = '*Primal Command*'
            time_print("With the training from Clover and the power of *Primal Command*, you leave and head into town.")
            town(items)
        elif answer == "2":
            lst2 = [
                '''(Clover) "I hope you will reconsider my offer." ''',
                "You leave the small house and return to town."
                ]
            time_print_loop(lst2)
            town(items)

def Elijah(items):
    time_print("You find yourself in front of a large log cabin surrounded by ancient stone sculpturs, both covered in snow.")
    if items['key'] == '2':
        lst = [
            "Elijah isn't home right now.",
            "There doesn't seem to be much to do here.",
            "You head back into town."
            ]
        time_print_loop(lst)
        town(items)
    elif items['key'] == '*Primal Command*':
        lst = [
            f"Elijah comes out to greet you and notices you possess {items['key']}.",
            "He smiles at you and begins to glow bright red.",
            '''(Elijah) "I want the power of *Primal Command* and i will crush you to take it!"''', 
            "Elijah gets into a fighting stance."
            ]
        time_print_loop(lst)
        fight(items)
    else:
        lst = [
            "Elijah, tall with powerful shoulders, and fierce blue eyes, comes out to greets you.",
            "He sizes you up, feeling your desire for power.",
            f'''(Elijah) "{items['player_name']}, I am the master you seek."''',
            '''(Elijah) "Take my guidence and uncover limitless potential of the spirit relm."\n''',
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
                "You leave the large stone house and return to town."
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