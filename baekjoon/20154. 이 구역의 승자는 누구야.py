from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

nums = [3, 2, 1, 2, 3, 3, 3	, 3, 1, 1, 3, 1, 3, 3, 1, 2	, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
arr = deque()
for i in input():
    arr.append(nums[ord(i)-65])

while len(arr) > 1:
    if len(arr) % 2:
        for i in range(0, len(arr)-1, 2):
            a = arr.popleft()
            b = arr.popleft()
            arr.append(a+b)
        x = arr.popleft()
        arr.append(x)
    else:
        for i in range(0, len(arr), 2):
            a = arr.popleft()
            b = arr.popleft()
            arr.append(a+b)

if arr[0] % 2:
    print('I\'m a winner!')
else:
    print('You\'re the winner?')
