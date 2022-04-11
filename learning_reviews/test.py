def caesarCipher(s, k):
    # Write your code here
    if k == 0:
        return s
    new_s = []
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            print(c)
            if c.islower():
                c = (ord(c) + k - 97)%26 + 97
                
            else:
                c = (ord(c) + k - 65)%26 + 65
            print(c)
            c = chr(c)
        new_s.append(c)
    return ''.join(new_s)

caesarCipher('hello-World',3)

a = 107
c = char(107)
print(c)