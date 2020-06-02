n = int(input())
for i in range(n):
    result = 0
    count = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j].__eq__('O'):
            count += 1
            result += count
        else:
            count = 0
    print(result)

