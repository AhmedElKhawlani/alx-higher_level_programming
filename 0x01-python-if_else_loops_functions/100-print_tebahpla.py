#!/usr/bin/python3
dif = ord('t') - ord('T')
for asc in range(ord('z'), ord('a') - 1, -1):
    if asc % 2 == 0:
        transforme = 0
    else:
        transforme = 1
    print("{:c}".format(asc - transforme * dif), end='')
