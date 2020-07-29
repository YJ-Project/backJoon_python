import math
m, n = map(int, input().split())
for i in range(m, n+1):
    result = 0
    if i == 1:
        result += 1
        continue

    x = int(math.sqrt(i))
    for k in range(2, x+1):
        if i % k == 0:
            result += 1
            break

    if result == 0:
        print(i)