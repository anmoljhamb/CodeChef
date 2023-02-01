# def lastI(arr: list, i: int):
#     return arr[::-1][:i+1]


# def check(arr: list):
#     for i in range(len(arr)-1):
#         if (i+1) % 2:
#             if sum(arr[:i+1]) <= sum(lastI(arr, i)):
#                 return False
#         else:
#             if sum(arr[:i+1]) >= sum(lastI(arr, i)):
#                 return False
#     return True


def ans(n):
    temp = [5, -5] * (n//2)
    temp[-1] += 1
    return temp


T = int(input())
for _ in range(T):
    n = int(input())
    if (n % 2):
        print(-1)
    else:
        print(*ans(n))
