import time
import random

#<------------------------------------------------------------ Basic Functions ------------------------------------------------------------>    

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def time_print(string):
    print(string)
    time.sleep(2)

def time_print_loop(lst):
    for i in range(len(lst)):
        time_print(lst[i])

def time_print_img(lst):
    for i in range(len(lst)):
        print(lst[i])
        time.sleep(.5)

def valid_input(promt, option1, option2):
    while True:
        response = input(promt).lower()
        if option1 in response:
            return option1
        if option2 in response:
            return option2
        else:
            time_print("I don't understand.")
    return response

def contine_reading():
    while True:
        response = input("Enter (1) to continue.\n").lower()
        if "1" in response:
            break
        else:
            time_print("I don't understand.")

#<------------------------------------------------------------ Fight System ------------------------------------------------------------>    

def boss_attack(items):    
    if items['boss_name'] == 'Clover':
        dmg = die_roll() + die_roll() 
        items['player_hp'] -= dmg
        lst = [
            f"{items['boss_name']} thrust her hands out tward you, shouting *Primal Command*!, as a torrent of all 5 elements crash into you.",
            f"{items['boss_name']} hits you for {dmg} damage.", 
            f"your health is now at {items['player_hp']}"
            ]
        time_print_loop(lst)
    else:
        dmg = die_roll() * 2 
        items['player_hp'] -= dmg
        lst = [
            f"{items['boss_name']} shouts *Banishing Light*! as a massive beam of light stricks you from the sky.",
            f"{items['boss_name']} hits you for {dmg} damage.", 
            f"your health is now at {items['player_hp']}\n"
            ]
        time_print_loop(lst)
    if items['player_hp'] > 0:
        answer = valid_input('Continue fighting or flee the battle?\n(1) Fight\n(2) Run\n', '1', '2')
        if answer == "1":
            time_print(f'''({items['player_name']}) "I will not give up!"''')
            who_attacks(items)
        elif answer == "2":
            lst = [
                f'''({items['player_name']}) "Im in over my head."''', 
                f"{items['player_name']} runs from the battle and escapes {items['boss_name']}.", 
                "You live to fight another day and return to town."
                ]
            time_print_loop(lst)
            town(items)
    else:
        time_print('You have died!')
        play_again()
        
def player_attack(items):
    if items['boss_name'] == 'Clover':
        dmg = die_roll() * 2
    else:
        dmg = die_roll() + die_roll() 
    items['boss_hp'] -= dmg
    lst = [
        f"{items['player_name']} bolts toward {items['boss_name']}, shouting {items['key']}!, as he blast {items['boss_name']} with a punishing strike.",
        f"You hit {items['boss_name']} for {dmg} damage points.",
        f"{items['boss_name']}'s health is now at {items['boss_hp']}\n"
        ]
    time_print_loop(lst)
    if items['boss_hp'] > 0:
        time_print(f'''{items['boss_name']} - "Not bad!"''')
        who_attacks(items)
    else:
        time_print('You have Won!')
        play_again()
        
def who_attacks(items):    
    result = coin_flip()
    if result == 'heads':
        player_attack(items)
    elif result == 'tails':
        boss_attack(items)
    else:
        who_attacks(items)

def intro_fight():    
    time_print('You are both still, waiting for the right time to make your move, and then...')


def choose_stats(items):
    opt1 = {
        'boss_hp': 10, 
        'player_hp': 10,
        'boss_name': 'Elijah'
        }
    opt2 = {
        'boss_hp': 10, 
        'player_hp': 10, 
        'boss_name': 'Clover',
        }
    if items['key'] == '*Primal Command*':
        items.update(opt1)
    else:
        items.update(opt2)
    return items
     
def play_again():
    time_print("Would you like to play again?")
    replay = valid_input("(1) Yes\n(2) No\n", "1", "2")
    if replay == "1":
        play()
    elif replay == "2":
        time_print("Ok thanks for playing!")

def fight(items):
    intro_fight()
    who_attacks(choose_stats(items))

#<------------------------------------------------------------ Story ------------------------------------------------------------>

def title():
    lst = [
        "         ,--.",                                                                                                                           
        "       ,--.'|                                                                                       ,--,    ,--,",                        
        "   ,--,:  : |                                                                    ,---.            ,--.'|  ,--.'|",                        
        ",`--.'`|  ' :             __  ,-.  __  ,-.   ,---.           .---.              /__./|            |  | :  |  | :",                        
        "|   :  :  | |           ,' ,'/ /|,' ,'/ /|  '   ,'\         /. ./|         ,---.;  ; |            :  : '  :  : '",                        
        ":   |   \ | :  ,--.--.  '  | |' |'  | |' | /   /   |     .-'-. ' |        /___/ \  | |   ,--.--.  |  ' |  |  ' |      ,---.       .--,",  
        "|   : '  '; | /       \ |  |   ,'|  |   ,'.   ; ,. :    /___/ \: |        \   ;  \ ' |  /       \ '  | |  '  | |     /     \    /_ ./|",  
        "'   ' ;.    ;.--.  .-. |'  :  /  '  :  /  '   | |: : .-'.. '   ' .         \   \  \: | .--.  .-. ||  | :  |  | :    /    /  |, ' , ' :",  
        "|   | | \   | \__\/: . .|  | '   |  | '   '   | .; :/___/ \:     '          ;   \  ' .  \__\/: . .'  : |__'  : |__ .    ' / /___/ \: |",  
        "'   : |  ; .' ,' .--.; |;  : |   ;  : |   |   :    |.   \  ' .\  |           \   \   '  ,' .--.; ||  | '.'|  | '.'|'   ;   /|.  \  ' |",  
        "|   | '`--'  /  /  ,.  ||  , ;   |  , ;    \   \  /  \   \   ' \ |            \   `  ; /  /  ,.  |;  :    ;  :    ;'   |  / | \  ;   :",  
        "'   : |     ;  :   .'   \---'     ---'      `----'    \   \  |--'              :   \ |;  :   .'   \  ,   /|  ,   / |   :    |  \  \  ;",  
        ";   |.'     |  ,     .-./                              \   \ |                  '---' |  ,     .-./---`-'  ---`-'   \   \  /    :  \  \ ", 
        "'---'        `--`---'                                   '---'                          `--`---'                      `----'      \  ' ;", 
        "                                                                                                                                  `--`", 
                                                                                                                                    
        ]
    time_print_img(lst)

def get_name(items):
    items['player_name'] = input("To start enter your name\n")
    return items

def intro_story():
    lst = [
        "A brave warrior wonders the world in search of great power.",
        "their journey leads them to two sacred mountains divided by a village in a narrow valley.",
        ]
    time_print_loop(lst)
    lst = [
        "        __   .  /\   .           .",
        "    *  /  \ *  /  \_         *     /\ __        *",
        "      /    \  /\ '  \*           _/  /  \  *'.",
        " .   /\/\  /\/ :' __ \_      _ /   ^/_   `--.",
        "    /    \/  \  _/  \-'\    /   ^ _   \_ ^ .'\  *",
        "  /\  .-   `. \/     \ /''' `.  _/ \  ^ `_/   \.",
        " /  `-.__ `   / .-'.--\ ''' / ^  `--./ .-'  `- ^",
        "/        `.  / /       `.''' .-' ^    '-._ `._  `-",
        "                          ''' "
        ]
    time_print_img(lst)        
    lst = ["At the peak of each holy mountain a great master resides.",
        "One has conquered the forces of nature.",
        "The other manipulates spiritual energy.\n"
        ]
    time_print_loop(lst)
    contine_reading()
    lst = [
        "           )            _     / \ ",
        "   /\    ( _   _._     / \   /^  \ ",
        "\ /  \    |_|-'_~_`-._/ ^ \ /  ^^ \ ",
        " \ /\/\_.-'-_~_-~_-~-_`-._^/  ^    \ ",
        "   _.-'_~-_~-_-~-_~_~-_~-_`-._   ^ ",
        "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "    |  [ ]   [ ]  [ ]   [ ] |",
        "    |   ___     __    ___   |   ",
        "    |  [___]   | .|  [___]  |  <inn>",
        "    |________  |__|  _______|    |",
        "^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^|^^ ",
        "          ^^^^^ === ^^^^^^      ^^^   "
        ]
    time_print_img(lst)
    time_print("After a much needed rest at the village inn, our hero sets out.\n")
        
def get_location(items):
    lst = [
        f"What do you wan't to do {items['player_name']}?",
        "(1) Traverse the wooded mountain to the east.",
        ]
    time_print_loop(lst)
    number = input("(2) Hike the snow covered mountain to the west.\n")
    return number

#<----- Story Flow ----->

def town(items):
    choice = get_location(items)
    if choice == '1':
        clover(items)
    elif choice == '2':
        elijah(items)
    else:
        town(items)

#<-------------------------------- Clover Functions -------------------------------->
def print_clover_house(items):
    lst = [
            "                                   /  \   .      ~         /\         `", 
            "  ~      /\      .            /\  /    \                  /`-\ ",
            "        /  \       `   /\    /^ \/  ^   \      /\  *     /  ^ \  .",
            "   .   / ^  \         / ^\  /  ^/  ^  )  \    /^ \      /  ^ ^ \ ",
            "      /`     \     ` /  ^ \/^ ^/^   (     \  /  ^ \    /      ^ \ ",
            "     /    ^   \~    / ^   /  ^/ ^ ^ ) ) ^  \/  ^^  \  / ^      `_\ ",
            "    /^  ^   `  \   / ^ ^   ^ / ^  (  ( ^   / ^   ^  \/`   ^       \ ",     
            "   /     ^ ^    \ /  ^ ^ ^^ / ^  (____) ^ /       ^ /     ^ ^   ^  \ ",
            "  /`   ^ ^  ^    \    ^  ^  ______|__|_____^ ^     / ^-    ^      ^ \ ",
            " / `'     ^     `-\     ^  /_______________\ ^ ^  / ^    ``     `-   \ ",
            "/     ^  ^^   ^   ^\^     /_________________\  ^ /  ^  ^^     ^       \ ", 
            "  -^ ^  ^ ^^-     ^ \^  ^  ||||||   |||__|||    /`-  ^  ^ ^^^   ^^-    \ ",       
            "        | |                ||||||I  |||__|||              | |    ",
            "||||||| [ ] |||||||||||||| ||||||___|||||||| |||||||||||| [ ] |||||||||| ", 
            '""""""""""""""""""""""""""""""""===="""""""""""""""""""""""""""""""""""""" ',
            "    |||||||||||||||||||||||||||=====|||||||||||||||||||||||||||||||| "   
            ]
    time_print_img(lst)
    
def clover_offer(items):
    print_clover_house(items)
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out to greet you.",
        "She peers curiously into you, sensing your kind heart...",
        f'''(Clover) "{items['player_name']}, I am the master you seek."''',
        '''(Clover) "Train under me and unearth the secrets only I and Mother Nature know."\n''',
        "Will you accept her offer?"
        ]
    time_print_loop(lst)

def clover_not_home(items):
    lst = [
        "Clover isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.\n"
        ]
    time_print_loop(lst)
    town(items)

def clover_fight(items):
    print_clover_house()
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out to greet you.",
        f"She notices {items['key']} in your possession and understands why you have come.",
        '''(Clover) "I will not be intimidated by one of Elijah's thugs!"''', 
        "Clover twirls her hands in the air, forming a bright green aura around herself.\n"
        ]
    time_print_loop(lst)
    contine_reading()
    fight(items)

def clover_training(items):
    lst = [
        "For the next year you apprentice yourself to Clover, cultivating your skills.",
        "You pickup that a man named Elijah has been trying to steal Clover's power for many years.",
        "You promise Clover that you will bring an end to Elijah's reign of terror.",
        "Clover is touched by your commitment.\n"
        ]
    time_print_loop(lst)
    contine_reading()           
    lst = [
        "To conclude your final day of training, Clover requests that you meet her infront of her house.",
        f'''(Clover) "{items['player_name']}, everything that you have endured was to prepare you for this."''',
        '''(Clover) "*Primal Command* is my greatest weapon and now it is yours."''',
        f'''(Clover) "Remember your promise and good luck on your travels {items['player_name']}."\n'''
        ]
    time_print_loop(lst)
    items['key'] = '*Primal Command*'
    contine_reading()
    lst = [
        "You recieve *Primal Command!*\n",
        "With the training from Clover and the power of *Primal Command*, you leave and head into town.",
        ]
    time_print_loop(lst)
    town(items)

def clover_turned_down(items):
    lst = [
        '''(Clover) "I hope you will reconsider my offer." ''',
        "You leave the small house and return to town."
        ]
    time_print_loop(lst)
    town(items)

# <----- Clover Flow ----->

def clover(items):
    time_print("You find yourself in front of a small wooden house surrounded by tall grass and massive pine trees.")
    if items['key'] == '*Primal Command*':
        clover_not_home()
    elif items['key'] == '*Banishing Light*':
        clover_fight(items)
    else:
        clover_offer(items)
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            clover_training(items)
        elif answer == "2":
            clover_turned_down(items)

#<-------------------------------- Elijah Functions -------------------------------->

def print_elijah_house(items):
    lst = [
                
        "         .           .       (    )       *                *",
        "    *                          )  )",
        "        .                     (  (              .      /\ ",
        "                           .   (_)                    /  \  /\ ",
        "      *       *     ___________[_]___________      /\/    \/  \ ",
        "           /\      /\   *       ______    *  \    /   /\/\  /\/\ ",
        "          /  \    //_\          \    /\       \  /\/\/    \/    \ ",
        "   /\    / /\/\  //___\       *  \__/  \  .    \/       *",
        "  /  \  /\/*   \//_____\          \ |[]|        \ ",
        " /\/\/\/       //_______\          \|__|         \           .",
        "/   __ \      /XXXXXXXXXX\                        \       __",
        "   /  \ \    /_I_I___I__I_\________________________\     /  \ ",
        "  { () }       I_I   I__I_________[]_|_[]_________I     ( () )",
        "   (  )  /\    I_II  I__I_________[]_|_[]_________I      (  )",
        "    []  (  )   I I___I  I         XXXXXXX    /\   I       []",
        " ~~~[] ~~[] ~~~~~____~~~~~~~~~~~~~~~~~~~~~~~{  }~~~~~~~~~~[] ~~~~~",
        "          ~~~~~~_____~~~~~~~~~~      ~~~~~~~~[] ~~~~~~~~~"
        ]
    time_print_img(lst)

def elijah_offer(items):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes out to greets you.",
        "He sizes you up, feeling your desire for power...",
        f'''(Elijah) "{items['player_name']}, I am the master you seek."''',
        '''(Elijah) "Take my guidence and uncover the limitless potential of the spirit relm."\n''',
        "Will you accept his offer?"
        ]
    time_print_loop(lst)

def elijah_not_home(items):
    lst = [
        "Elijah isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.\n"
        ]
    time_print_loop(lst)
    town(items)

def elijah_fight(items):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes out to greets you.",
        f"He smiles at you and begins to glow bright red as he notices you possess {items['key']}.",
        f'''(Elijah) "I crave the power of {items['key']} and i will crush you to obtain it!"''', 
        "Elijah gets into a fighting stance.\n"
        ]
    time_print_loop(lst)
    contine_reading()
    fight(items)

def elijah_training(items):
    lst = [
        "For the next year you memorize every mystical technique offerered to you by Elijah.",
        "Elijah shares his disire to increase his capabilities by defeating other masters and taking their power.",
        "He wants you to assist him and share the bounty, both of you becomming allpowerful.",
        "Elijah feels that with you, his dreams can be realized.\n",
        ]
    time_print_loop(lst)
    contine_reading()    
    lst = [    
        "To conclude your final day of training, Elijah requests that you meet him infront of his house.",
        f'''(Elijah) "{items['player_name']}, everything that you have encountered has prepare you for this."''',
        '''(Elijah) "*Banishing Light* is my greatest technique and now it is yours."''',
        f'''(Elijah) "{items['player_name']}, I want you to defeat a master named Clover to the east and take her power.''',
        '''(Elijah) "Leave now and only return when you have completed your mission."\n'''
        ]
    time_print_loop(lst)
    contine_reading()
    items['key'] = '*Banishing Light*'
    lst = [
        "You recieve *Banishing Light*\n",
        "With the training from Elijah and the power of *Banishing Light*, you leave and head into town."
        ]
    time_print_loop(lst)
    town(items)

def elijah_turned_down(items):
    lst = [
        '''(Elijah) - "I hope you will reconsider my offer." ''',
        "You leave the massive log cabin and return to town."
        ]
    time_print_loop(lst)
    town(items)

# <----- Elijah Flow ----->

def elijah(items):
    time_print("You find yourself in front of a sizable log cabin surrounded by odd stone sculpturs, both covered in snow.")
    if items['key'] == '*Banishing Light*':
        elijah_not_home(items)
    elif items['key'] == '*Primal Command*':
        elijah_fight(items)
    else:
        elijah_offer(items)
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            elijah_training(items)
        elif answer == "2":
            elijah_turned_down(items)

#<----- Game Play / Items ----->

def play():
    items = {
    'key':'', 
    'player_name':''
    }
    title()
    get_name(items)
    intro_story()
    town(items)

#<----- Play ----->

play()