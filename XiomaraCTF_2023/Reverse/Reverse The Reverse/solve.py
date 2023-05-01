l = [67, 74, 80, 95, 94, 68, 30, 91, 30, 75, 114, 95, 73, 114, 29, 29, 95, 65, 30, 114, 90, 114, 89, 69, 114, 89, 29, 29, 64, 30, 30, 28, 78, 76, 86, 122, 64, 76, 95, 117, 68, 66]

l = [chr(i^0x2d) for i in l]
s = ''.join(l)
ans = ''
for i in range(len(s),0,-6):

    ans += s[i-3:i]
    ans += s[i-6:i-3]

print(ans)

# print(s)

# actual_string
# checks for whether the input is 42 bytes
# then it divides the string into 6 bytes and reverses it

# then it divides each 6 byte string into 3 bytes and reverses it
# then it appends it to a single string and divides it again bytes for 3 and swaps even and odd indices of strings
# Atlast it xors it with 0x2d

#So its divided reverses twice, nullifying the effects of two reversing
#Now what we have to do is xor the array with 0x2d and divide the string into bytes of 3 and swap the even and odd indices of divided bytes.