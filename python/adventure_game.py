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

def get_name():
    name = input("To start enter your name\n")
    items = {
        'key':'', 
        'player_name':''
        }
    return name

def intro(name):
    lst = [
        "A brave warrior wonders the world to find great power.",
        "their journey leads them to a small town hidden at the peak of a mountain.",
        "Two great masters reside there. ",
        "One has mastered the forces of nature.",
        "The other is a master of spiritual energy.",
        "An important decision is in front of you...\n"
        ]
    time_print_loop(lst)    

def location():
    lst = [
        "What do you wan't to do?",
        "1. Go see the master of nature",
        ]
    time_print_loop(lst)
    choice = int(valid_input("2. Go see the master of spirit\n", "1", "2"))
    return choice

def play():
    intro(get_name())
    location()

play()