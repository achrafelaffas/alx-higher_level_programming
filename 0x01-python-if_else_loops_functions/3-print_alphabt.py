#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) not in ('e', 'q'):
        print("{}".format(chr(a)), end='')
