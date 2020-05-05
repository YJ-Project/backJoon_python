n, x = map(int, input().split())
j = list(map(int, input().split()))

for i in j:
    if x > i:
        print(i, end=' ')