word = 'Hello1'
abr = 'abracadabra'
fullName = 'Пучков Никита Валерьевич'
numbersList = '1, 2,3,4, 5, 6,7, 8'
free = '   freeee     '

print(id(word))
print(id(word.upper()))
print('\t')

print(abr.count('ra'))
print(abr.count('ra', 1))
print(abr.count('ra', 1, 9))
print('\t')

print(abr.find('br'))
print(abr.find('br', 2))
print('\t')

print(abr.replace('a', 'o'))
print(abr.replace('ab', 'AB'))
print(abr.replace('a', ''))
print(abr.replace('a', '', 2))
print('\t')

print(abr.isalpha())
print(word.isalpha())
print('\t')

print(abr.rjust(13, 't'))
print('\t')

print(fullName.split(' '))
numbersList = numbersList.replace(' ', '').split(',')
print(numbersList)
print(', '.join(numbersList))

fullName = '.'.join(fullName.split())
print(fullName)
print('\t')

print(free.strip())

