username = input()
user, age = username.split()
if int(age) <= 20:
    print("Full access")
else:
    print("No access")