n = int(input())
score = list(map(int, input().split()))
m = max(score)
ave = []
for i in range(n):
    ave.append(score[i]/m*100)
print(sum(ave)/n)