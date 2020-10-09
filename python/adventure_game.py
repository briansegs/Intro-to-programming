import time
import random

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

def get_name(items):
    items['player_name'] = input("To start enter your name\n")
    return items

def intro():
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
        "Type 1 to go see the master of nature.",
        ]
    time_print_loop(lst)
    number = input("Type 2 to go see the master of spirit.\n")
    return number

def enter(items):
    choice = location(items)
    if choice == '1':
        print('first')
    elif choice == '2':
        print('second')
    else:
        enter(items)
    enter(items)

def go(floor, name):
    lst = [
        f'You push the button for the {floor} floor.', 
        f'After a few moments, you find yourself in the {name}.'
        ]
    p_loop(lst)

def play():
    items = {
    'key':'', 
    'player_name':''
    }
    get_name(items)
    intro()
    enter(items)

play()