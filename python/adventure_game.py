import time
import random

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def t_print(string):
    print(string)
    time.sleep(1)

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

items = {
     'health': 10,
     'rolls': 1,
}

my_hp = items['health']
boss_hp = 10

t_print('You are both still, waiting for the right time to make your move, and then...')
who_attacks = coin_flip()
while my_hp > 0 and boss_hp > 0:
    if who_attacks == 'heads':
        dmg = (die_roll() + die_roll())
        my_hp -= dmg
        t_print('The Boss unsheaths his sword, darts twards you, and slashes you with a swift blow.')
        t_print(f'Boss hits you for {dmg} damage points.\n' 
        f'your health is now at {my_hp}')
        if my_hp > 0:
            answer = valid_input('Continue fighting or flee the battle? Type flee or fight.', 'fight', 'flee')
            if answer == "fight":
                t_print('Player- "I will not back down!"')
                who_attacks = coin_flip()
            elif answer == "flee":
                t_print('Player- "Im in over my head."')
                t_print('You run from the battle and escape Boss.')
                t_print('You live to fight another day.')
                break
        else:
            t_print('You have died')

             

    elif who_attacks == 'tails':
        dmg = (die_roll() * 2)
        boss_hp -= dmg
        t_print('You bolt toward Boss, lifting oath breaker above your head, and then strick Boss with a heavy blow')
        t_print(f'You hit Boss for {dmg} damage points.\n'
        f"Boss's health is now at {boss_hp}")
        if boss_hp > 0:
            t_print('Boss- "Not bad!"')
            who_attacks = coin_flip()
        else:
            t_print('You have Won!')

