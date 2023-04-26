def ans(n: int):
    cost = (n // 10) * 10
    temp = (n % 10) // 5
    cost += ((temp)) * 10
    return 100 - cost


T = int(input())
for _ in range(T):
    n = int(input())
    print(ans(n))
