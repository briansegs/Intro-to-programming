import time

def get_order(option1, option2):
    response = valid_input(f'Please place your order. Would you like {option1} or {option2}?\n', option1, option2)
    
    if option1 in response:
        print_pause(f"{option1} it is")
    elif option2 in response:
        print_pause(f"{option2} it is")
    
def intro():
    lst = [
        'Hello! I am Bob, the Breakfast Bot.',  
        'Today we have two breakfasts available.', 
        'The first is waffles with strawberries and whipped cream.', 
        'The second is sweet potato pancakes with butter and syrup.'
    ]
    for index in range(len(lst)):
        print_pause(lst[index])
    
def order_again(option1, option2):
    response = valid_input(f"Would you like to place another order? Please say {option1} or {option2}.\n", option1, option2)
    if option1 in response:
        print_pause('OK, goodbye!')
        return False
    elif option2 in response:
        print_pause("Very good, I'm happy to take another order.")
        return True
    
def print_pause(message):
    print(message)
    time.sleep(1)

def valid_input(promt, option1, option2):
    while True:
        response = input(promt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response
                
def order_breakfast():
    intro()
    again = True
    while again == True:
        get_order('waffles', 'pancakes')
        again = order_again('no', 'yes')

    
order_breakfast()