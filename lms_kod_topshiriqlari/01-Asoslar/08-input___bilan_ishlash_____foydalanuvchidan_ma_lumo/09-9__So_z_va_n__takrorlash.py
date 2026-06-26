soz = input().strip()
n = int(input().strip())
natija = (soz + ' ') * (n - 1) + soz if n > 0 else ''
print(natija)