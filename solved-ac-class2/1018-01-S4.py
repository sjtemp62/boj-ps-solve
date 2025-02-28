m, n = map(int, input().split())

chess_map = list()

for i in range(m):
    chess_map.append(input())

min_count = 33

for i in range(m - 8 + 1):
    for j in range(n - 8 + 1):
        for BW in ["B", "W"]:
            count = 0
            for line in range(8):
                for block in range(8):
                    if line % 2 == 0:
                        if block % 2 == 0:
                            if chess_map[line + i][block + j] == BW:
                                continue
                            else:
                                count += 1
                        else:
                            if chess_map[line + i][block + j] != BW:
                                continue
                            else:
                                count += 1
                    else:
                        if block % 2 == 1:
                            if chess_map[line + i][block + j] == BW:
                                continue
                            else:
                                count += 1
                        else:
                            if chess_map[line + i][block + j] != BW:
                                continue
                            else:
                                count += 1

            min_count = min(min_count, count)

print(min_count)