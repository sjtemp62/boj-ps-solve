card = int(input())
card_list = list(map(int, input().split()))
having_card = int(input())
having_card_list = list(map(int, input().split()))

dic = dict()

for i in card_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in having_card_list:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")