from functools import reduce
import json


def red(n1, n2):
    return n1 + n2


with open('7_task.txt', 'r', encoding='utf-8') as firms:
    firms_prof = []
    firms_loss = []
    profit = []
    loss = []
    for line in firms:
        line_list = line.split()
        firms_prof.append(line_list[0])
        diff = int(line_list[2]) - int(line_list[3])
        if diff > 0:
            profit.append(diff)
        else:
            loss.append(diff)
            l_f = firms_prof.pop(-1)
            firms_loss.append(l_f)

prof_firms = {}
loss_firms = {}
av_prof = {}
av_profit = reduce(red, profit) // len(profit)
av_prof['average_profit'] = av_profit
i = 0
while i != len(firms_prof):
    prof_firms[firms_prof[i]] = profit[i]
    i += 1

i = 0
while i != len(firms_loss):
    loss_firms[firms_loss[i]] = loss[i]
    i += 1

result = []
result.append(prof_firms)
result.append(loss_firms)
result.append(av_prof)

with open('7_task.json', 'w', encoding='utf-8') as write_j:
    json.dump(result, write_j)

