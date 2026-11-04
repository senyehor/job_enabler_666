# L0009: an interactive tip calculator that asks for the bill, tip percent and number of people
print("=== Tip calculator ===")
bill_amount = float(input("Bill amount: "))
tip_percent = int(input("Tip percent: "))
num_people = int(input("Number of people: "))

tip_amount = bill_amount * tip_percent / 100
total_amount = bill_amount + tip_amount
share = total_amount / num_people

print('')
print(f'Bill: {bill_amount:.2f}')
print(f'Tip: {tip_amount:.2f}')
print(f'Total: {total_amount:.2f}')
print(f'Recap', f'{bill_amount:.2f}', f'{tip_amount:.2f}', f'{total_amount:.2f}', f'{share:.2f}', sep=' | ')
print(f'Each person pays: ', end='')
print(f'{share:.2f}')

