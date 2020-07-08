n = int(input())
result = n
for i in range(n):
    words = input()
    dup = ''
    for j in range(1, len(words)):
        if words[j-1] != words[j] and words[0:j-1].__contains__(words[j]):
            result -= 1
            break
print(result)