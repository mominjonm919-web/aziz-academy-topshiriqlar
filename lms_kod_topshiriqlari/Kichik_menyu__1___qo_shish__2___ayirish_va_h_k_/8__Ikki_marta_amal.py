import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        try:
            a = float(input_data[idx])
            b = float(input_data[idx+1])
            op = input_data[idx+2]
            idx += 3
            
            if op == '0':
                print("Exit")
                break
            
            a_int, b_int = int(a), int(b)
            if op == '1': print(a_int + b_int)
            elif op == '2': print(a_int - b_int)
            elif op == '3': print(a_int * b_int)
            elif op == '4': print(a / b)
        except:
            break

solve()
