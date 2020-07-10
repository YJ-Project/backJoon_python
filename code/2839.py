n = int(input())
if n % 5 == 0:
    print(n//5)
else:
    calc = n//5
    cnt = 0
    result = 0
    while True:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            result = cnt + (n//5)
            break
        if n < 0:
            result = -1
            break
    print(result)