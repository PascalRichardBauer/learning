gerichte = ['klöse', 'kloepse']
print(gerichte[1] == 'kloepse')
print(gerichte == 'hamburger')

car = 'Hyundai'
print(car.lower() == 'hyundai')

number = 18
print(number == 18)
print(number != 19)
print(number <= 15)
print(number <= 21)
print(number >= 19)
print(number <= 19)

print("\n")
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print(age_0 <= 17 and age_1 <= 16)

name_list = ['alfred', 'lasse', 'tobi']
if 'kalle' not in name_list:
    print("join game")

if 'alfred' in name_list:
    print("you've already joined!")