#assigning variables
monthly_allowences = float(input('how much you get monthly ? '))
food = float(input('how much you spent of foods? '))
transport = float(input('how much you spent on transport ? '))
entertainment = float(input('how much you spent on entertainment ? '))
shopping = float(input('how much you spent on shopping ? '))
others = float(input('any other spends ? '))

#output visual asthetics
print(' '*500)
print('-'*60)
print('               **Analysis and recommendations**')
print(' '*60)
print('-'*60)

#main category-wise spends to percentage function. 
def percentage_cal(a, b):
    global spent_portion
    spent_portion = (a / b)*100
    return spent_portion

print(f'You spent {percentage_cal(food, monthly_allowences):.2f} % on Food ')
print(f'You spent {percentage_cal(transport, monthly_allowences):.2f} % on transport ')
print(f'You spent {percentage_cal(entertainment, monthly_allowences):.2f} % on entertainment ')
print(f'You spent {percentage_cal(shopping, monthly_allowences):.2f} % on shopping ')
print(f'You spent {percentage_cal(others, monthly_allowences):.2f} % on random small spend ')
#again visual asthetics only
print('-'*60)

print('                  SUGGETIONS')

#function to flag unusual high spends by comparing the maximum .
def compare_spends(a, b, c, d, e):
    global compare
    compare = [float(a), float(b), float(c), float(d), float(e)]
    return compare
categories = ['food', 'transport', 'entertainment', 'shopping', 'others']
compare_spends (f'{(food / monthly_allowences)*100:.2f}  ', 
f'{(transport/ monthly_allowences)*100:.2f} ', 
f'{(entertainment / monthly_allowences)*100:.2f} ', 
f'{(shopping/ monthly_allowences)*100:.2f} ', 
 f'{(others/ monthly_allowences)*100} ')

maximum = max(compare)
position = compare.index(maximum)
category = categories[position]
#logic for unusual high spending
if max(compare) > 40 :
    print(f'Unusual high spends : {max(compare):.2f} % on {category} ')
else:
    print('No unusual high spends detected !')

#visual ashethetics again!
print('-'*60)

#some more variables 
total_spent = food + transport + entertainment + shopping + others 
remaing_bal = (monthly_allowences - total_spent)

#function to calculate percentage of remaing funds 
def percentage_remain(x, y):
    global remain_percentage
    remain_percentage = (x / y)*100
    return remain_percentage

percentage_remain(remaing_bal, monthly_allowences)
print(f'your remaining balance is {remaing_bal:.2f} ie {remain_percentage:.2f} % of monthly allowence ')

#logic for remainig funds
if remain_percentage >= 50 :
    print('Healthy spendings ,You can invest the rest !')
elif remain_percentage < 50 and remain_percentage >= 20:
    print('moderate spendigs,Be careful and save more ! ')
else:
    print('Overspending , try to save money on non-inmportant things ! ')




