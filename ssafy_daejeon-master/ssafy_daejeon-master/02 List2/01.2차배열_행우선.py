arr = [[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]


# N, M = len(arr), len(arr[0])
# for i in range(N):
#     for j in range(M):
#         print('%2d ' % arr[i][j], end='')
#     print()

for y in range(len(arr)):
    for x in range(len(arr[0])):
        print('%2d ' % arr[y][x], end='')
    print()

# 1. 행 우선순회
# for y in range(len(arr)):
#     for x in range(len(arr[0])):
#         arr[y][x]