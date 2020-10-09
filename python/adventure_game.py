import time
import random

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def t_print(string):
    print(string)
    time.sleep(1)

def t_print_loop(lst):
    for i in range(len(lst)):
        t_print(lst[i])

def valid_input(promt, option1, option2):
    while True:
        response = input(promt).lower()
        if option1 in response:
            return option1
        if option2 in response:
            return option2
        else:
            t_print("Sorry, I don't understand.")
    return response

def player_attack(hp):    
    dmg = (die_roll() + die_roll())
    hp['player'] -= dmg
    lst = ['The Boss unsheaths his sword, darts twards you, and slashes you with a swift blow.',
    f'Boss hits you for {dmg} damage points.', 
    f'your health is now at {hp["player"]}'
    ]
    t_print_loop(lst)
    if hp['player'] > 0:
        answer = valid_input('Continue fighting or flee the battle? Type flee or fight.', 'fight', 'flee')
        if answer == "fight":
            t_print('Player- "I will not back down!"')
            who_attacks(hp)
        elif answer == "flee":
            lst = ['Player- "Im in over my head."', 
            'You run from the battle and escape Boss.', 
            'You live to fight another day.'
            ]
            
            
    else:
        t_print('You have died')
        


def boss_attack(hp):
    dmg = (die_roll() * 2)
    hp['boss'] -= dmg
    t_print('You bolt toward Boss, lifting oath breaker above your head, and then strick Boss with a heavy blow')
    t_print(f'You hit Boss for {dmg} damage points.')
    t_print(f"Boss's health is now at {hp['boss']}")
    if hp['boss'] > 0:
        t_print('Boss- "Not bad!"')
        who_attacks(hp)
    else:
        t_print('You have Won!')
        

def who_attacks(hp):    
    result = coin_flip()
    if result == 'heads':
        player_attack(hp)
    elif result == 'tails':
        boss_attack(hp)
    else:
        who_attacks(hp)

def intro():    
    t_print('You are both still, waiting for the right time to make your move, and then...')

def fight():
    hp = {'boss': 10, 'player': 10}
    intro()
    who_attacks(hp)


fight()
    
