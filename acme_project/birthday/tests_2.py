import unittest


def bubble_sort(array: list[float]) -> list[float]:
    """Сортировка списка методом пузырька по возрастанию."""
    length = len(array)
    for bypass in range(1, length):
        for k in range(length - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


class TestBubbleSort(unittest.TestCase):
    """Тестируем функцию bubble_sort."""

    def test_int_float(self):
        """Проверка сортировки списка с int и float."""
        call = bubble_sort([5, 3.2, 4, 1, 2.5])
        result = [1, 2.5, 3.2, 4, 5]
        self.assertEqual(
            call, result, 'Функция bubble_sort некорректно работает со списком чисел'
        )

    def test_empty(self):
        """Проверка сортировки пустого списка."""
        call = bubble_sort([])
        result = []
        self.assertEqual(
            call, result, 'Функция bubble_sort некорректно работает с пустым списком'
        )


if __name__ == '__main__':
    unittest.main()
