x = int(input())
line = 0
max = 0
for i in range(1, x+1):
    line = i
    max += i
    if max >= x:
        break

a = line-(max-x)
b = 1+max-x
if line % 2 == 0:
    print(a, '/', b, sep='')
else:
    print(b, '/', a, sep='')