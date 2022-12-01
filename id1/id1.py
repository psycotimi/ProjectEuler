# multiples of 3 or 5 under 1000 summed

summa = 0
i = 1

while i < 1000:
    if (i % 3 == 0) or (i % 5 == 0):
        summa += i
    i += 1
print(summa)