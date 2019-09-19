motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]="ducati"
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(-1,'ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(1,'ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print('the last motorcycle I owned was a '+last_owned.title()+'.')
last=motorcycles.pop(0)
print('my favorite motor was a '+last.upper()+'.')

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
too_expensive="honda"
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+' is too expensive for me.')

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
expensive='ducati'
motorcycles.remove(expensive)
print(motorcycles)
print(expensive)
