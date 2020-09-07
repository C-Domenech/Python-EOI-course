def solution(n, d, x):
    for j in reversed(range(n)):
        d = x[j] * (d // x[j])
    return d


t = int(input())

for i in range(1, t + 1):
    n, d = [int(i) for i in input().split()]
    x = list(map(int, input().split()))

    print('Case #{}:'.format(i), solution(n, d, x))
    
    
# 3
# 3 10
# 3 7 2
# 4 100
# 11 10 5 50
# 1 1
# 1
