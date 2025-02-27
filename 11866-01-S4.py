from collections import deque

n, k = map(int, input().split())
pos = k - 1
yose = deque(range(1, n+1))
result = []

while yose: # 학습 필요 - rotate는 원형 큐 방식으로 회전
    yose.rotate(-(k-1))
    result.append(yose.popleft())

print(f"<{", ".join(map(str, result))}>")