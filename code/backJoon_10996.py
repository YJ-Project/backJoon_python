n = int(input())
# 짝수의 별의 개수
even_num = n // 2
# 홀수의 별의 개수
old_num = n - n // 2

for i in range(n):
    print('* ' * old_num)
    print(' *' * even_num)