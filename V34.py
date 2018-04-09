# Scramlber V.34

import random
from operator import xor

data = [1,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1]
out = []

x  = 7

SYNC = []
for sync_i in range(0,x):
    SYNC.append(random.randint(0,1))

print("SYNC: ", SYNC)
print("DATA:   ", data)

data_len = int(len(data))
print("Data count: ", data_len)

for i in range(0,data_len):

    XOR_VALUE = xor(SYNC[x-1],SYNC[x-2])

    SYNC.insert(0,SYNC.pop())
    SYNC[0]=XOR_VALUE

    out.append(xor(XOR_VAL,data[i]))

print("Data output: ", out)








