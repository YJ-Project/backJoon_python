import math
k = 100011
num_list = [True]*k
for i in range(1, k):
    if i == 1:
        continue
    for k in range(2, int(math.sqrt(i))+1):
        if i % k == 0:
            num_list[i] = False
            break

t = int(input())
for _ in range(t):
    n = int(input())
    k = n
    diff = n
    for i in range(2, n//2 + 1):
        if num_list[i] and num_list[n-i] and diff > (n-2*i):
            k = i
            diff = n-2*i
    print(k, n-k, end=" ")