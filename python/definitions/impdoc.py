#!/usr/bin/env python

# Note that if only definitions.py is imported,
# will default to import definitions
# **Note that style syntax needs to be added to DOCS.md**
def impdoc(name, doctype='def', pull='def'):
    myfile = open(name, 'r')
    lineZero = myfile.readline()
    print(lineZero)
    print(lineZero.split('{')[1].split('}')[0])
    lineZero = '{' + (lineZero.split('{')[1].split('}')[0]) + '}'
    style = eval(lineZero)
    print(lineZero, style)
    if doctype == 'auto': style['type']
    if not(style['type'] == doctype):
        return('error: doctypes do not match')

    if doctype == 'def':
        info = ''.join(myfile.read().split('\n'))
        myfile.close()
        info = '{' + info + '}'
        return(eval(info))

    if doctype == 'note':
        lines = myfile.read().split('\n')
        myfile.close()
        if pull == 'def':
            lines = [x for x in lines if '**:' in x]
            info = {}
            for x in lines:
                index = x.split('**')[1]
                data = ' '.join(x.split('**')[2::])
                data = data[2::]                                    # removes ': '
                info[index] = data
            return(info)
