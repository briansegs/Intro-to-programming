import random
import words


def silly_string(nouns, verbs, templates):
    temp = random.choice(templates)
    n = '{{noun}}'
    v = '{{verb}}'
    out = []
    i = 0
    while i < len(temp):
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        if temp[i: i + len(n)] == n:
            out.append(noun)
            i += len(n)
        elif temp[i: i + len(v)] == v:
            out.append(verb)
            i += len(v)
        else:
            out.append(temp[i])
            i += 1
    return "".join(out)


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs, 
    words.templates))
