l, n, m = map(int, input().split())
cnt =0
x = l
while 1 :
    if cnt >= m - 1 :
        break
    else :
        cnt += 1
        x *= n
print(x)
