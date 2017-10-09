#!/usr/bin/env python

from StudyAssistant import definitions as df
from sys import argv
import os

prnt = False
inpt = ''
otpt = ''
if len(argv) == 1:
    output = os.popen('ls *.md').read().split('\n')
    if len(output) == 0:
        raise EOFError('No markdown files found, none specified.')
    else:
        inpt = output[0]
        otpt = 'definitions-{}.txt'.format(inpt[:-3])
else:
    pass

info = df.impdoc(inpt, doctype='note', pull='def')
os.popen('touch {}'.format(otpt))
df.expdoc(info, otpt)
