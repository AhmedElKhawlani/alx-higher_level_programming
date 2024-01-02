#!/usr/bin/python3
for asc in range(ord('a'), ord('z') + 1):
    if not chr(asc) in ('q', 'e'):
        print('{:c}'.format(asc), end='')
