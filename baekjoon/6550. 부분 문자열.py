import sys
sys.stdin = open('input.txt', 'r')


for line in sys.stdin:
    S, T = line.split()
    idx = 0
    res = 'No'

    for i in range(len(T)):
        if T[i] == S[idx]:
            idx += 1
            if idx == len(S):
                res = 'Yes'
                break
    print(res)
