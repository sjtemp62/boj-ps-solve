# BOJ - 15829 - 01 - B2 - Hashing

str_len = int(input())
str_data = input()
ans = 0

for i in range(len(str_data)):
    ans += (ord(str_data[i]) - 96) * (31 ** i)

print(ans % 1234567891)