#!/usr/bin/env python

import random as rd

definitions = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
    'd': 'dragon fruit',
    'e': 'elderberry'
}

# For only a single mutiple choice question
# Should be strung together for multiple questions
def choice(mydic, string=None, num=4):
    if not(2 < num < 26):
        num = 4
    elif len(mydic) < 4:
        num = len(mydic)
    if not(string in mydic.keys()):
        string = rd.choice([x for x in mydic.keys()])
    alpha = []
    for x in 'abcdefghijklmnopqrstuvwxyz':
        alpha.append('{0}.'.format(x))
    rslt, answ, choices = mydic[string], [x for x in mydic], []

    for x in range(num):
        foo = mydic[answ.pop(rd.randint(0, len(answ) - 1))]
        choices.append(foo)
    if not(rslt in choices):
        index = rd.randint(0, 3)
        choices[index] = rslt

    print('Define: {0}'.format(string))
    print()
    for x, y in enumerate(choices):    print(alpha[x] + ' ' + str(y))
    print()
    answer = input('\007>>> ')
    if not(answer == rslt):
        if len(answer) > 2: answer = answer[:2]
        if len(answer) < 2: answer += '.'
        if not(answer[1] == '.'): answer = answer[0] + '.'
    print()
    if answer == rslt:
        print(answer == rslt)
    elif choices[alpha.index(answer)] == rslt:
        print(choices[alpha.index(answer)] == rslt)
    else:
        print(False, rslt, sep='\n')
    print()

# Note that if only definitions.py is imported,
# will default to import definitions
# **Note that style syntax needs to be added to DOCS.md**
def impdoc(name, doctype='def'):
    myfile = open(name, 'r')
    style = eval(myfile.readline())
    if doctype == 'auto': style['type']
    if not(style['type'] == doctype):
        return('error: doctypes do not match')

    if doctype == 'def':
        info = ''.join(myfile.read().split('\n'))
        info = '{' + info + '}'
        return(eval(info))

    myfile.close()

def expdoc(mydic, name, doctype='def'):
    myfile = open(name, 'r')
    style = eval(myfile.readline())
    if doctype == 'auto': style['type']
    if not(style['type'] == doctype):
        return('error: doctypes do not match')
    myfile.close()

    myfile = open(name, 'w')
    myfile.truncate(0)

    if doctype == 'def':
        myfile.write("{'type': 'def'}\n")
        for x in mydic:
            myfile.write("'{0}': '{1}',\n".format(x, mydic[x]))

    myfile.close()

def edit(mydic, key, rslt=None):
    if not(rslt):
        mydic.__delitem__(key)
    else:
        mydic[key] = rslt
