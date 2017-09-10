#!/usr/bin/env python

import random as rd

definitions = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
    'd': 'dragon fruit',
    'e': 'elderberry'
}

def choice(mydic, string, num=4):
    if not(2 < num < 26):
        num = 4
    elif len(mydic) < 4:
        num = len(mydic)

    alpha = []
    for x in 'abcdefghijklmnopqrstuvwxyz':
        alpha.append('{0}.'.format(x))

    rslt = mydic[string]
    answ = [x for x in mydic]
    choices = []

    print('Define: {0}'.format(string))
    print()

    for x in range(num):
        foo = mydic[answ.pop(rd.randint(0, len(answ) - 1))]
        choices.append(foo)

    if not(rslt in choices):
        index = rd.randint(0, 3)
        choices[index] = rslt

    for x, y in enumerate(choices):    print(alpha[x] + ' ' + str(y))

    print()

    answer = input('\007>>> ')

    if not(answer == rslt):
        if len(answer) > 2: answer = answer[:2]
        if not(answer[1] == '.'): answer = answer[0] + '.'

    print()
    if answer == rslt:
        print(answer == rslt)
    elif choices[alpha.index(answer)] == rslt:
        print(choices[alpha.index(answer)] == rslt)
    else:
        print(False)
    print()

choice(definitions, 'b')
