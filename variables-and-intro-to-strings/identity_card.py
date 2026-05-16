print(f'**Identity card generator**')

user_full_name = input('Enter First and lastname ').strip().title()
user_age = int(input('enter your age '))
user_city = input('Enter your current city ').title()
user_hobby = input('Enter your hobby (any one) ').title()
second_intial = user_full_name.index(' ' )
user_name_intials1 = user_full_name[0:1]
user_name_intials2 = user_full_name[second_intial + 1 : second_intial + 2]

print('.'*40)
print(f'           Identity Card')
print('.'*40)
print(f'Name: {user_full_name}')
print(f'Initials: {user_name_intials1}.{user_name_intials2} ')
print(f'Age: {user_age}')
print(f'City: {user_city}')
print(f'Hobby: {user_hobby}')
print('.'*40)

