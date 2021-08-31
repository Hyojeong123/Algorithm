import sys
sys.stdin = open('input.txt', 'r')

words = []
mx = 0
ans = ''
for _ in range(5):
    words.append(input())
    if len(words[-1]) > mx:
        mx = len(words[-1])

for i in range(mx):
    for word in words:
        if len(word)-1 >= i:
            ans += word[i]
print(ans)
