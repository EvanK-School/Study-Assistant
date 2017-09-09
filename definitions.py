#!/usr/bin/env python

import random as rd

definitions = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
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
        print(alpha[x] + ' ' + str(foo))

    print()

    answer = input('\007>>> ')

    print()
    print(choices[alpha.index(answer)] == rslt)

choice(definitions, 'b')
