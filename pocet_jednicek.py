#program, ktery nacte cele cislo a spocita pocet jednicek

def pocet_jednicek(cislo):
    pocet = 0
    while cislo > 0:
        zbytek = cislo % 10
        if zbytek == 1:
            pocet = pocet + 1
        cislo = cislo // 10
    return pocet

cislo = input('Zadej cislo: ')
pocet = pocet_jednicek(cislo)
print('Pocet jednicek v cisle {} je {}.'.format(cislo, pocet))

#cislo = input('Zadej cislo: ')
#
# pocet_jednicek = cislo.count('1')
#
# print('Pocet jednicek v cisle {} je {}.'.format(cislo, pocet_jednicek))
