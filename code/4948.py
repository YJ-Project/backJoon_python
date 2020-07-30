import math
k = 123456*2+1
num_list = [1]*k
for i in range(1, k):
    if i == 1:
        continue
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    sum = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        sum += num_list[i]
    print(sum)