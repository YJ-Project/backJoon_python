word = input().upper()
w_list = set(word)
result = ''
max_cnt = 0

for i in w_list:
    if max_cnt < word.count(i):
        max_cnt = word.count(i)
        result = i
    elif max_cnt == word.count(i):
        result = '?'
print(result)