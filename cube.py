squares=[]
for value in range(1,11):
 square=value**3
 squares.append(square)
print(squares)

print('\n')

squares=[value**3 for value in range(1,11)]
print(squares)
