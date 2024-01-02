#!/usr/bin/python3
def uppercase(str):
    dif = ord('z') - ord('Z')
    for c in str:
        if 'a' <= c <= 'z':
            o = ord(c) - dif
        else:
            o = ord(c)
        print('{:c}'.format(o), end='')
    print()
