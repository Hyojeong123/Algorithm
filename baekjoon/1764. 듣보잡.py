import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
names = []
res = []
for i in range(N+M):
    names.append(input())

names.sort()

for i in range(N+M-1):
    if names[i] == names[i+1]:
        res.append(names[i])

print(len(res))
for name in res:
    print(name)
