arr = [3, 6, 7,8]


for i in range(1<<len(arr)):
        for j in range(len(arr)):
                if i & (1<<j):
                        print(arr[j],end=',')
        print()