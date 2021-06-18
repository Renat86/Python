numbers = int(input('Введите число до 20 - '))
words = ['процент', 'процентов', 'процента']
for word in words:
    if 1 < numbers < 5:
        print(numbers, words[2])
        break
    elif numbers == 1:
        print(numbers, words[0])
        break
    else:
        print(numbers, words[1])
        break
