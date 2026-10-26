# L0008: print a cafe receipt with f-strings, then slice strings apart
shop = "Corner Cafe"
item1 = "Coffee"
price1 = 2.5
qty1 = 2
item2 = "Croissant"
price2 = 1.75
qty2 = 3
item3 = "Orange Juice"
price3 = 3.2
qty3 = 1
order_code = "ORD-2026-0042"

print(shop)
print(f'-' * 24)
print(f'{item1:<14} {price1:.2f} * {qty1:.2f} = {price1 * qty1:>6.2f}')
print(f'{item2:<14} {price2:.2f} * {qty2:.2f} = {price2 * qty2:>6.2f}')
print(f'{item3:<14} {price3:.2f} * {qty3:.2f} = {price3 * qty3:>6.2f}')
print(f'-' * 24)
print(f'Total: {price1 * qty1 + price2 * qty2 + price3 * qty3:>6.2f}')
print(f'First letter: {shop[0]}')
print(f'Last 3: {shop[-3:]}')
print(f'Reversed: {item1[::-1]}')
print(f'Code length: {len(order_code)}')
print(f'Prefix: {order_code[:3]}')
print(f'Year: {order_code[4:8]}')
print(f'Number: {order_code[-4:]}')