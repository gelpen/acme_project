

def bubble_sort(array: list[float]) -> list[float]:
    """Сортировка списка методом пузырька по возрастанию."""
    length = len(array)
    for bypass in range(1, length):
        for k in range(length - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


print(bubble_sort([9.5, 9,8,7,6,5,4,3,2,1]))
