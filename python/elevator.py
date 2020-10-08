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
    lst = [f'You push the button for the {floor} floor.', f'After a few moments, you find yourself in the {name}.', 'Where would you like to go next?']
    p_loop(lst)

def enter_floor():
    floor = fl()
    if floor == '1':
        go('first', 'lobby')
    elif floor == '2':
        go('second', 'human resources department')
    elif floor == '3':
        go('third', 'engineering department')
    else:
        enter_floor()
    enter_floor()

def items():
    bag = [] 

def elevator():
    intro()
    enter_floor()

elevator()