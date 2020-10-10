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

def intro():    
    time_print('You are both still, waiting for the right time to make your move, and then...')


def choose_stats(items = {'key':'thing1', 'player_name':'Brian'}):
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
    if items['key'] == 'thing1':
        opt1['player_name'] = items['player_name']
        stats = opt1
    else:
        opt2['player_name'] = items['player_name']
        stats = opt2
    return stats
     
def fight():
    intro()
    who_attacks(choose_stats())


if __name__ == "__main__":
    fight()
    





    
