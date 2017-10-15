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
            sets = []
            for x, y in enumerate(lines):
                if '**:' in y:
                    if y.strip()[0:2] == '- ':
                        sets.append(y.strip()[2:])
                    else:
                        sets.append(y.strip())
                elif '**:' in lines[x-1] and y.strip()[0:2] != '- ':
                    print(True)
                    sets[-1] = sets[-1] + ' ' + y.strip()
            info = {}
            for x in sets:
                index = x.split('**')[1]
                data = ' '.join(x.split('**')[2::])
                data = data[2::]                                    # removes ': '
                info[index] = data
            return(info)
