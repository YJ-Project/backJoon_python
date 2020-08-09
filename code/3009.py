x_map = [0 for _ in range(3)]
y_map = [0 for _ in range(3)]

for i in range(3):
    x_map[i], y_map[i] = map(int, input().split())

for i in range(3):
    if x_map.count(x_map[i]) == 1:
        x = x_map[i]
    if y_map.count(y_map[i]) == 1:
        y = y_map[i]
print(x, y, end=" ")