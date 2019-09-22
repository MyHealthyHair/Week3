mypizzas=['margherita','hawaii','pepperoni']
friendpizzas=mypizzas[:]
mypizzas.append('cheese')
friendpizzas.append('ham')

print("My favorite pizzas are:")
for pizza in mypizzas:
 print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friendpizzas:
 print(pizza)
