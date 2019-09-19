guests=['Ann','Bnn','Cnn','Dnn']
print(guests)
print('I will invite those people: '+guests[0]+'、'+guests[1]+'、'+guests[2]+' and '+guests[3]+'.')

del guests[0]
print(guests)

guests.insert(0,'Enn')
print(guests)
print('I will invite them: '+guests[0]+'、'+guests[1]+'、'+guests[2]+' and '+guests[3]+'.')

print('I find a big hall.')

guests.insert(0,'1cc')
print(guests)

guests.insert(2,'2cc')
print(guests)

guests.append('3cc')
print(guests)
print(guests[0]+' ,welcome!')
print(guests[1]+' ,welcome!')

print('\nSorry I can just invite two people')

sorry=guests.pop()
print('\n'+sorry+', I am sorry.')
print(guests)

sorry=guests.pop()
print('\n'+sorry+', I am sorry.')
print(guests)

sorry=guests.pop()
print('\n'+sorry+', I am sorry.')
print(guests)

sorry=guests.pop()
print('\n'+sorry+', I am sorry.')
print(guests)

sorry=guests.pop()
print('\n'+sorry+', I am sorry.')
print(guests)

sorry=guests.pop()
print('\n'+sorry+', I wil invite you.')

sorry=guests.pop()
print('\n'+sorry+', I will invite you .'+'\n')

print(guests)

