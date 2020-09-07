def solution(n, h):
    peaks = 0
    for j in range(1, n - 1):
        if h[j] > h[j - 1] and h[j] > h[j + 1]:
            peaks += 1
    return peaks


t = int(input())

for i in range(t):
    n, h = int(input()), list(map(int, input().split()))

    print('Case #{}:'.format(i + 1), solution(n, h))
    
# 4
# 3
# 10 20 14
# 4
# 7 7 7 7
# 5
# 10 90 20 90 10
# 3
# 10 3 10
