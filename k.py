def min_gifts(N, S, K):
    S.sort()
    total_gifts = 0
    satisfied_friends = 0
    for i in range(N):
        total_gifts += S[i]
        satisfied_friends += 1
        if satisfied_friends == K:
            break
    return total_gifts

T = int(input())
for _ in range(T):
    N = list(map(int, input().split()))
    N_friends = N[0]
    satisfying_factors = list(map(int, input().split()))
    K = int(input())
    print(min_gifts(N_friends, satisfying_factors, K))