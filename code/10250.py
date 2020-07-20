t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    cnt = 0
    room = 0
    floor = 0
    for i in range(1, w+1):
        if cnt == n:
            break
        room = i
        for j in range(1, h+1):
            if cnt == n:
                break
            cnt += 1
            floor = j
    room = format(room, '02')
    print('%s%s' % (floor, room))