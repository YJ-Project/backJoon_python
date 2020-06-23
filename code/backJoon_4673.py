all_set = set(range(1, 10001))
generate_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generate_set.add(i)

self_num = all_set - generate_set
for k in sorted(self_num):
    print(k)