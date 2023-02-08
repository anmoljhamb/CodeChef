# from itertools import permutations


# def score(arr: list):
#     n = len(arr)
#     for i in range(n):
#         if (i+1) == arr[i]:
#             return False
#         arr[i] = arr[i] % (i+1)
#     return len(set(arr))


# n = 7
# min_score = n
# # ans = None
# arr = list(range(1, n+1))
# for per in permutations(arr, n):
#     temp = list(per)
#     temp = score(temp)
#     if temp != False:
#         if temp < min_score:
#             min_score = temp
#             ans = list(per)

# print(ans)
# print(score(ans))

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(2, n+1):
        print(i, end=" ")
    print(1)
