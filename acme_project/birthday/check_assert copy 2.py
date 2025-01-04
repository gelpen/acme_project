def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result

mixed_numbers = []
print(series_sum(mixed_numbers))







# def series_sum(incoming):
#     # Конкатенирует все элементы списка, приводя их к строкам.
#     result = ''
#     for i in incoming:
#         result += str(i)
#     return result


# # Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# # если ей на вход передать список из целых и дробных чисел.

# mixed_numbers =  [1, 2.5, 3]
# result_numbers =  '12.53'

# # Вместо многоточия напишите утверждение, которое должно быть проверено.
# assert series_sum(mixed_numbers) == result_numbers, (
#     'Функция series_sum() некорректно обрабатывает смешанный список из int и float.'
# )