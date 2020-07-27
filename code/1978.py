n = int(input())
num_list = map(int, input().split())
result = n
for i in num_list:
    if i == 1:
        result -= 1
        continue

    for k in range(2, i):
        if i % k == 0:
            result -= 1
            break
print(result)