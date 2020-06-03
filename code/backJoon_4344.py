for i in range(int(input())):
    total = list(map(int, input().split()))
    ave = (sum(total)-total[0]) / total[0]
    cnt = 0
    for j in total[1:]:
        if j > ave:
            cnt += 1
    print(str('%.3f' % round(cnt / total[0] * 100, 3))+'%')
