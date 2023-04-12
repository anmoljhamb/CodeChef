def ans(n: int):
    temp = 2 ** n

    ans = temp-1

    count = 0
    for x in range(1, temp+1):
        for y in range(1, temp+1):
            z = ans - x - y
            if (z > 0):
                if (x | y | z) == ans:
                    count += 1
    return (count)


for i in range(3, 61):
    temp = ans(i)
    print(f"if n == {i}")
    print(f"\t{temp}")
