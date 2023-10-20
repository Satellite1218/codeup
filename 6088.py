l, n, m = map(int, input().split())
cnt =0
x = 0
while 1 :
    if cnt >= m :
        break
    else :
        cnt += 1
        x += n
print(x+l-n)
