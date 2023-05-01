#!/bin/python3

from string import printable

l = [297, 517, 530, 287, 584, 468, 584, 556, 481, 481, 481, 491, 344, 318, 596, 313, 353, 305, 491, 318, 317, 282, 472, 491, 472, 331, 305, 468, 649, 256, 406, 472, 305, 491, 406, 318, 472, 491, 473, 353, 317, 455, 491, 481, 481, 481, 432]

def collatz(n):
    ctr = 0
    while n > 1:
        if n%2:
            n = 3*n + 1
        else:
            n = n//2
        ctr+=1
    return ctr

d = {}
for i in printable:
    if d.get(collatz(ord(i)*1056298169038583),0) == 0:
        d[collatz(ord(i)*1056298169038583)] = [i]
    else:
        d[collatz(ord(i)*1056298169038583)].append(i)

# print(d)

ans = ''
for i in l:
    if len(d[i]) == 1:
        ans += d[i][0]
    else:
        ans += str(d[i])
print(ans)
