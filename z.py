def min_gifts_to_satisfy_friends(test_cases):
    results = []
    for case in test_cases:
        N, satisfying_factors, K = case
        # Sort the satisfying factors in ascending order
        satisfying_factors.sort()
        # Sum the first K smallest satisfying factors
        min_gifts = sum(satisfying_factors[:K])
        results.append(min_gifts)
    return results

def main():
    T = int(input())  # Number of test cases
    test_cases = []
    
    for _ in range(T):
        N = int(input())  # Number of friends
        satisfying_factors = list(map(int, input().split()))  # Satisfying factors of each friend
        K = int(input())  # Number of friends Messi wants to satisfy
        test_cases.append((N, satisfying_factors, K))
    
    results = min_gifts_to_satisfy_friends(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
