n = int(input())
row = 1
max_num = 1

while True:
    if max_num >= n:
        print(row)
        break
    max_num += 6*row
    row += 1