a, b, v = map(int, input().split())
result = (v-a)//(a-b) + 1
if (v-a) % (a-b) == 0:
    print(result)
else:
    print(result+1)
