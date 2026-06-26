for _ in range(2):
    a, b = map(int, input().split())
    t = int(input())
    if t == 1: print(a + b)
    elif t == 2: print(a - b)
    elif t == 3: print(a * b)
    elif t == 4: print(a / b)
print("Exit")