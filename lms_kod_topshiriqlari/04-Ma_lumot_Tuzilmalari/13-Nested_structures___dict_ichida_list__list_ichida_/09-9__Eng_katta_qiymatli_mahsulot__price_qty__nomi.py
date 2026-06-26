
n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
eng_katta_maxsulot = max(items, key=lambda x: x['price'] * x['qty'])
print(eng_katta_maxsulot['name'])