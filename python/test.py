import antigravity

location = 1
size = 3
word = 'fascinating'

 
def test(target, word):
    for i in range(len(word)):
         if word[i : i + len(target)] == target:
            return True
    return False

# print(test('oo', 'book'))

# def is_substring():

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(lst):
    return '<br>'.join(lst)

# print(breakify(lines))

string = "Hello world!"
output = [] # Create empty list
index = 0
while index < len(string):
    output.append(string[index]) # Append current character
    index += 1 # Move on to next character

# print(output)

string = 'SPAM!HelloSPAM! worldSPAM!!'
output = []
index = 0
while index < len(string):
    if string[index:index+5] == 'SPAM!':
        index += 5
    else:
        output.append(string[index])
        index += 1
print("".join(output))

