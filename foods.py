myfoods=['pizza','falafel','carrot cake']
friendfoods=myfoods[:]
print('My favorite foods are:')
print(myfoods)
print("\nMy friend's favorite foods are:")
print(friendfoods)

print('\n')

myfoods=['pizza','falafel','carrot cake']
friendfoods=myfoods[:]
myfoods.append('cannoli')
friendfoods.append('ice cream')
print('My favorite foods are:')
print(myfoods)
print("\nMy friend's favorite foods are:")
print(friendfoods)

print('\n')

myfoods=['pizza','falafel','carrot cake']
# this is wrong!
friendfoods=myfoods
myfoods.append('cannoli')
friendfoods.append('ice cream')
print('My favorite foods are:')
print(myfoods)
print("\nMy friend's favorite foods are:")
print(friendfoods)

