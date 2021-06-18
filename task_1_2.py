# делаю список кубов нечетных чисел
numbers = [number ** 3 for number in range(1, 1000, 2)]
print(numbers)
# необходимо выбрать числа сумма которых делится на 7
result = 0
for number in numbers:
    sum_numb = 0
    item = number
    while item != 0:
        sum_numb += item % 10
        item = item // 10
    if sum_numb % 7 == 0:
        result += number
print(result)
# добавляем 17 к значения внутри списка и суммируем результат
new_result = 0
for number in numbers:
    new_sum_numb = 0
    number += 17
    new_item = number
    while new_item != 0:
        new_sum_numb += new_item % 10
        new_item = new_item // 10
    if new_sum_numb % 7 == 0:
        new_result += number
print(new_result)
















