num = input()
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for i in range(len(num)):
    for j in alphabet:
        if num[i] in j:
            time += alphabet.index(j)+3
print(time)