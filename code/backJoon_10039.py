s_list = []
for i in range(5):
    score = int(input())
    if score < 40:
        s_list.append(40)
    else:
        s_list.append(score)
print(sum(s_list)//len(s_list))