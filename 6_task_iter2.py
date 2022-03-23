from itertools import cycle, count
li_st = [1, 2, 3, 4, 5]

i = 0
for el in cycle(li_st):
    if i > 24:
        break
    print(el)
    i += 1
