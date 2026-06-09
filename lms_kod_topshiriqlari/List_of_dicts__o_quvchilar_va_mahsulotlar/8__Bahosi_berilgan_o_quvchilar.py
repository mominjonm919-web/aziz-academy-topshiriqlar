n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append(int(score))
target = int(input())
print(students.count(target))