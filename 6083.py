l, n, m = map(int, input().split())
cnt =0
for i in range (0, l) :
    for j in range (0, n) :
        for k in range (0, m) :
            cnt += 1
            print(i, j, k)
print(cnt)
