import string
s = input()
for i in list(string.ascii_lowercase):
    print(s.find(i), end=' ')