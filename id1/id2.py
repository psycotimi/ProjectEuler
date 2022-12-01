# sum of even fibonacci numbers that totals under 4M

luku1, luku2 = 0, 1
nakki = 0
summa = 0
loppu = 4000000

while nakki <= loppu:
    nakki = luku1 + luku2
    luku1 = luku2
    luku2 = nakki

    if nakki % 2 == 0:
        summa += nakki
print(summa)