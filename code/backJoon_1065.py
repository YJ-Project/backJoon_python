n = int(input())
result = 0
if n < 100:
    result = n
else :
    result = 99
    for i in range(100, n+1):
        if 2*(i // 10 % 10) == i // 100 + i % 10:
            result += 1
print(result)