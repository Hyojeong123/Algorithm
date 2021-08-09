import sys
sys.stdin = open('input.txt', 'r')

M, N = int(input()), int(input())
res = []

# 2 ~ 제곱근까지 약수가 있는지 확인
for num in range(M, N+1):
    flag = 0
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        res.append(num)

if M == 1:
    res.pop(0)

if len(res) > 0:
    print(sum(res))
    print(min(res))
else:
    print(-1)
