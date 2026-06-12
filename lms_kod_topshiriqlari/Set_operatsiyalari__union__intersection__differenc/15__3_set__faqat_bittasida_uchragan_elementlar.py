A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
res = (A ^ B ^ C) - (A & B & C)
if res:
    print(*sorted(res))
else:
    print("BO'SH")