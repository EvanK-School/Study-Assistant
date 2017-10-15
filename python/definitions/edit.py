#!/usr/bin/env python

def edit(mydic, key, rslt=None):
    if not(rslt):
        mydic.__delitem__(key)
    else:
        mydic[key] = rslt
