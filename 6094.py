n = int(input())
num = list(map(int, input().split()))
cnt = 10000
for i in reversed(num):
    if cnt > i :
        cnt = i
print(cnt)
