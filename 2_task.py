li_st = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [li_st[i] for i in range(len(li_st)) if li_st[i-1] < li_st[i]]

print(new_list)
