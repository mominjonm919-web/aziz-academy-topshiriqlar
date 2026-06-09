n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
if not items:
    print("")
else:
    max_item = items[0]
    for item in items[1:]:
        if item['price'] > max_item['price']:
            max_item = item
    print(max_item['name'])