num = int(input())
ans = 1000001

for i in range(num):
    sum = 0
    for j in str(i):
        sum += int(j)
    if num == i + sum:
        ans = min(ans, i)

if ans == 1000001:
    print(0)
else:
    print(ans)
