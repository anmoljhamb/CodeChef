# def check(arr: list):
#     for i in range(len(arr)):
#         sub = [arr[i]]
#         for j in range(i+1, len(arr)):
#             sub.append(arr[j])
#             if (sum(sub) % len(sub) == 0):
#                 return False
#     return True


T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n):
        if i % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
