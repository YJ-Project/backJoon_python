import math
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    max = int(math.sqrt(distance))
    if max == math.sqrt(distance):
        print(2*max-1)
    elif math.sqrt(distance) - max <= 0.5:
        print(2*max)
    else:
        print(2*max+1)
