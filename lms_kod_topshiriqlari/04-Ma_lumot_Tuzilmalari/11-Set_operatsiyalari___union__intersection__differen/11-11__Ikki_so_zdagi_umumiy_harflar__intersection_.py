a = input().strip()
b = input().strip()
set_a = set(a)
set_b = set(b)
common = set_a & set_b
if common:
    print(''.join(sorted(common)))
else:
    print("BO'SH")