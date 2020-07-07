alpha = input()
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in word:
    alpha = alpha.replace(i, ' ')
print(alpha.__len__())
