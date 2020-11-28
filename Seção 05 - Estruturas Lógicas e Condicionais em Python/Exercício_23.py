"""
23) Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Por exemplo: 1988, 1992, 1996.
"""

year = int(input('Enter year: '))
if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
    print('Leap year!')
else:
    print('Year is not leap!')
