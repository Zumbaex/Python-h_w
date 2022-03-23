from sys import argv

argv, hours, pay, prem = argv

try:
    salary = (int(hours) * int(pay)) + int(prem)
    print(f'Зарплата составляет: {salary} руб')

except ValueError as (er):
    print(er)
