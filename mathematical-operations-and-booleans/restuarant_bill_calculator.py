#Restaurant bill calculator

#storing values in variables
customer_name = input('Customer name ').strip().title()
num_of_people = int(input('How many people ? '))
original_bill_amt = abs(float(input('Enter Original bill Amount ')))
tip = 0
discount = 0

#Tip logic 

if original_bill_amt <500:
    tip = 0
if original_bill_amt >=500 and original_bill_amt <1500:
    tip = 0.10*original_bill_amt

else:
    tip = 0.15*original_bill_amt


#Discount calculations

if num_of_people >=5:
    discount = 0.08*original_bill_amt
else:
    discount = 0

#Mandotory Tax of 5%

tax = 0.05*original_bill_amt

#Print of reciept !

print('-'*60)
print('-'*60)
print(f'                   RESTAURANT BILL RECIEPT')
print('-'*60)
print('-'*60)
print(f'Customer :     {customer_name}')
print(f'Table size:     {num_of_people}')
print(' '*150)
print(f'Original Bill:        ₹{round(original_bill_amt, 2)}')
if discount != 0:
    print(f'Discount({(round(discount/original_bill_amt*100))}%)          ₹{round(discount, 2)}')
else:
    pass
if tip != 0:
    print(f'Tip({round(tip/original_bill_amt*100)}%):             ₹{round(tip, 2)}')
else:
    pass
print(f'Tax(5%):              ₹{round(tax, 2)}')
print(f'-'*60)
grand_total = (original_bill_amt - discount) + tip + tax
print(f'Amount:               ₹{round(grand_total, 2)}')
print(f'Total Payable:        ₹{round(grand_total, 0)}')
print('-'*60)
print('-'*60)
print(f'Thank you for dining with us !')







