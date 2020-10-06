def find_wut_times(num):
    for x in range(100):
        for y in range(100):
            if x * y == num:
                 return f"{x} * {y} == {num}"
    


print(find_wut_times(783))

def find_wut_pow(num):
    for x in range(100):
        for y in range(100):
            if x ** y == num:
                 return f"{x} ** {y} == {num}"
    


print(find_wut_pow(3600))

def find_wut_plus(num):
    for x in range(100):
        for y in range(100):
            if x + y == num:
                 return f"{x} + {y} == {num}"
    


print(find_wut_plus(145))