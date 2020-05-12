b_min = 2000
d_min = 2000

for i in range(3):
    b = int(input())
    b_min = min(b_min, b)


for j in range(2):
    d = int(input())
    d_min = min(d_min, d)

print(b_min+d_min-50)