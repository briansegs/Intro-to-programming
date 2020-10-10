import time
import random
import fight

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
        first(items)
    elif choice == '2':
        print('second')
    else:
        enter(items)
    enter(items)

def first(items):
    if items['key'] == '1':
        lst = [
            "Boss doesn't seem to be home.",
            "There doesn't seem to be much to do here."
            "You head back into town."
            ]
        time_print_loop(lst)
    else:
        lst = [
            "Boss greets you.",
            "She peers curiously into your eyes and senses your pure heart.",
            "She asks you to be her student and to learn the ways of nature."
            ]
        time_print_loop(lst)
        answer = valid_input("Will you accept her offer? Type (yes) or (no).", "yes", "no")
        if answer == "yes":
            lst1 = [
                "For the next year you spend every day with boss learning the ways of nature.",
                "You learn that she and the town have been under attack from Boss for many years.",
                "She wants you to end his reign of terror once and for all.",
                "She opens her hands, they glow bright green as she places them over your chest and says...",
                '"This is my most powerful technique name."',
                '"You are ready to face boss."',
                '"Go defeat him!"\n',
                "You have gain the power of technique!\n"
                ]
            time_print_loop(lst1)
            items['key'] = '1'
            time_print("With the training from boss and the power of technique, you leave and head into town.")


def play():
    items = {
    'key':'', 
    'player_name':''
    }
    get_name(items)
    intro()
    enter(items)

play()