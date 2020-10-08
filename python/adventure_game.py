import time
import random

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

items = {
     'health': 10,
     'rolls': 1,
}

my_hp = items['health']
boss_hp = 10

who_attacks = coin_flip()

if who_attacks == 'heads':
    my_hp -= (die_roll() + die_roll())
    print(f'my hp @ {my_hp}')
elif who_attacks == 'tails':
    boss_hp -= (die_roll() + die_roll())
    print(f'boss hp @ {boss_hp}')

