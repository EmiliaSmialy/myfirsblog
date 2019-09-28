print('Hello, Django girls!')
if 3>2:
    print('To działa!')
if 5>2:
    print('5 jest jednak wieksze od 2')
else:
    print('5 nie jest większe od 2')
name = 'Sonja'
if name =='Ola':
    print('Hej Ola!')
elif name =='Sonja':
    print('Hej Sonja')
else:
    print('Hej anonimie!')
volume =57
if volume <20:
    print("It's kinda qitet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi():
    print ('Hej!')
    print ('Jak się masz?')

hi()
hi()

def hi(imie):
    if imie=='Ola':
        print('Hej Ola!')
    elif imie =='Sonja':
        print('Hej Sonja!')
    else:
        print('hej nieznajoma!')


hi('Ola')

def hi(imie):
    print('Hej'+ imie + '!')
hi("Rachel")

def hi2(imie):
    print('Witaj ' + imie + '!')
dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hi2(imie)
    print('Kolejna dziewczyna')

hi2('Monica')

for i in range(1,6):
    print(i)



