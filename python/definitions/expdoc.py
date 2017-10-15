#!/usr/bin/env python

def expdoc(mydic, name, doctype='def'):
    myfile = open(name, 'r')
    lineZero = myfile.readline()
    print(lineZero)
    print(lineZero.split('{')[1].split('}')[0])
    lineZero = '{' + (lineZero.split('{')[1].split('}')[0]) + '}'
    style = eval(lineZero)
    if doctype == 'auto': style['type']
    if not(style['type'] == doctype):
        return('error: doctypes do not match')
    myfile.close()

    myfile = open(name, 'w')
    myfile.truncate(0)

    myfile.write("[//]: ({'type': '" + doctype + "'})\n")
    if doctype == 'def':
        for x in mydic:
            myfile.write("'{0}': '{1}',\n".format(x, mydic[x]))

    myfile.close()
