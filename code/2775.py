t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    apartment = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            apartment[j] += apartment[j-1]
    print(apartment[n-1])

