import time

def t_print(string):
    print(string)
    time.sleep(1)

def p_loop(lst):
    for i in range(len(lst)):
        t_print(lst[i])

def intro():
    lst = ['You have just arrived at your new job!', 'You are in the elevator']
    p_loop(lst)

def fl():
    lst = ['Please enter the number for the floor you would like to visit:', '1. Lobby', '2. Human resources']
    p_loop(lst)
    return str(input('3. Engineering department\n'))
    
def go(floor, name):
    lst = [f'You push the button for the {floor} floor.', f'After a few moments, you find yourself in the {name}.']
    p_loop(lst)



def first_floor(items):
    go('first', 'lobby')
    if 'id' in items:
        t_print('The clerk greets you, but she has already given you your ' 
        'ID card, so there is nothing more to do here now.') 
    else:
        t_print('The clerk greets you and gives you your ID card.')
        items.append('id')

def second_floor(items):
    go('second', 'human resources department')
    if 'handbook' in items:
        lst = ["The HR folks are busy at their desks.",
        "There doesn't seem to be much to do here."]
        p_loop(lst)
    else:
        t_print('The head of HR greets you.')
        if 'id' in items:
            t_print('He looks at your ID card and then gives you a copy of the employee handbook.')
            items.append('handbook')
        else:
            t_print("He has something for you, but says he can't " 
            "give it to you until you go get your ID card.")

def third_floor(items):
    go('third', 'engineering department')
    if 'id' in items:
        lst = ['You use your ID card to open the door.',
        'Your program manager greets you and tells you that you need to have a copy of the',
        'employee handbook in order to start work.']
        p_loop(lst)
    else:
        lst = ["Unfortunately, the door is locked and you can't get in.",
        "It looks like you need some kind of key card to open the door.",
        "You head back to the elevator."]
        p_loop(lst)
    if 'id' in items and 'handbook' in items:
        lst = ["Fortunately, you got that from HR!",
        "Congratulatons! You are ready to start your new job as vice president of engineering!"]
        p_loop(lst)
    if 'id' in items and 'handbook' not in items:
        t_print("They scowl when they see that you don't have it, and send you back to the elevator.")


def enter_floor(items):
    floor = fl()
    if floor == '1':
        first_floor(items)
    elif floor == '2':
        second_floor(items)
    elif floor == '3':
        third_floor(items)
    else:
        enter_floor(items)
    enter_floor(items)

def elevator():
    items = []
    intro()
    enter_floor(items)

elevator()