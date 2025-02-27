from collections import deque

n, k = map(int, input().split())
pos = k - 1
yose = deque(range(1, n+1))
result = []

while yose:
    yose.rotate(-(k-1))
    result.append(yose.popleft())

print(f"<{", ".join(map(str, result))}>")