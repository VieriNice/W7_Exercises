# Exercise 1.D

name = input('Enter a name: ').lower()

def trunc_name(nam):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    n = nam[0]
    n2 = nam[1]
    if n in vowels:
        return nam
    elif n2 not in vowels:
        return nam[2:]
    else: 
        return nam[1:]

# print(trunc_name(name))

trunc_n = trunc_name(name)

def name_game(n):
    yield f'{n.capitalize()},{n.capitalize()}, bo-{trunc_n}'
    yield f'banana fan fo-f{trunc_n}'
    yield f'me my mo-m{trunc_n}'
    yield f'{n.capitalize()}'

for i in name_game(name):
    print(i)

