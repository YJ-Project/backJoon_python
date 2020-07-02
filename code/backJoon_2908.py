number = input().split()
result = []
for i in range(len(number)):
    reverse = ''
    size = len(number[i])
    for j in range(size):
        reverse += number[i][size-j-1]
    result.append(reverse)
print(max(result))