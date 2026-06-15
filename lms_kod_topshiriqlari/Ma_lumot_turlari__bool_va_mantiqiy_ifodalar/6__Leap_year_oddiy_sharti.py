yil = int(input())
print(yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0))