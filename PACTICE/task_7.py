word = str(input('Введите слово: '))

word = list(word)
word_reverse = word
word_reverse.reverse()

if word != word_reverse:
    print('НЕТ')
else:
    print('ДА')


print(''.join(word))
print(''.join(word_reverse))
