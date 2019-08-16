my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorie foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorites food are:")
print(my_foods)
print("\nfriend's favorite food are:")
print(friend_foods)

print("The first three items are:")
print(my_foods[0:3])

my_foods.append('frikasse')
my_foods.append('frikadellen')
my_foods.append('kartoffelsalat')

print("Three items of the middle of the list are:")
print(my_foods[2:5])

print("These are the last three items of the list are:")
print(my_foods[-3:])