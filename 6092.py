n = int(input())
cnt = [0] * 30

a = input()
num = a.split()
for num in num:
    cnt[int(num)] += 1

for i in range(1, 24):
    print(cnt[i], end=" ")
