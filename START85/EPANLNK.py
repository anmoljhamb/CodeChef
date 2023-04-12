T = int(input())
for _ in range(T):
    number = input()
    number = number[-2:]
    number = int(number)
    print(number % 20)
