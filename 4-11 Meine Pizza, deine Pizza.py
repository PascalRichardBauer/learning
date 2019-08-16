pizza_list = ['salami', 'magharita', 'vulcano']
for pizza in pizza_list:
    print("I like " + pizza.title() + " pizza.")
print("\nI like really Pizzaś!\n")

friend_pizza = pizza_list[:]

pizza_list.append('calzone')
friend_pizza.append('hawaii')

print("My favorite Pizza is:\n")
for my_pizza in pizza_list[:]:
    print(my_pizza)

print("\n\n")
    
print("My friends favorite pizza is:\n")
for friend_pizza in friend_pizza[:]:
    print(friend_pizza)

