m = int(input())
n = int(input())
sum = 0
min = n
for i in range(m, n+1):
    result = 0
    if i == 1:
        result += 1
        continue

    for k in range(2, i):
        if i % k == 0:
            result += 1
            break

    if result == 0:
        sum += i
        if min > i:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)