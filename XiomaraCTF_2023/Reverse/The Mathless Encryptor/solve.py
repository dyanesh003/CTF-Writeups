#!/bin/python3

from ctypes import cdll
libc = cdll.LoadLibrary("libc.so.6")

f = open('flag.txt','rb')
data = f.read()
f.close()

l = []
for i in data:
    l.append(i)

tmp = l[0]
prev = l[0]
for i in range(1,len(l)):
    tmp = l[i]
    l[i] = l[i] ^ prev
    prev = tmp

key = 'Xiomara{' # first eight bytes of was used to xor
nkey = []
tmp = ''
for i in range(8):
    if i%2:
        tmp +=  bin(ord(key[i]))[2:].zfill(8)[4:]
        nkey.append(int(tmp,2))
        tmp = ''
    else:
        tmp += bin(ord(key[i]))[2:].zfill(8)[:4]

for i in range(len(l)):
    l[i] = l[i] ^ nkey[i%4]

epoch = 1682247726 #time of file creation (seed)
libc.srand(epoch)

for i in range(len(l)):
    for j in range(i):
        l[i] = l[i] ^ libc.rand()%256

print(chr(int(bin(l[-1])[2:].zfill(8)[4:] + bin(l[0])[2:].zfill(8)[:4],2)),end='')
for i in range(1,len(l)):
    print(chr(int(bin(l[i-1])[2:].zfill(8)[4:] + bin(l[i])[2:].zfill(8)[:4] ,2)),end="")
print()