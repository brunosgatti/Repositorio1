#!/usr/bin/env python3

import sys
import random

seq=sys.argv[1]
print(seq)
for x in range (0, len(seq)) :
    pos1=randrange(0,len(seq))
    pos2=randrange(0, len(seq))
    while pos1==pos2 :
        pos1=randrange(0,len(seq))
        pos2=randrange(0,len(seq))
    letra1=seq[pos1]
    letra2=seq[pos2]
    seq[pos2]=letra1
    seq[pos1]=letra2
print(seq)
