import unittest


def bartender(order):
    if isinstance(order, int) and order > 0:
        return order
    return 'Извините, я не могу вас обслужить!'


class TestBar(unittest.TestCase):

    def test_bartender(self):
        values_results = (
            (5, 5),
            (0, 0),
            (0.33, 0.33),
            (-1.999999, -1.999999),
            (фываолдж, фываолдж),)

    for value in values_results:
        # subTest в качестве контекстного менеджера.
        with self.subTest():
            result = bartender(value)
            # Тестовое утверждение, которое будет вызвано несколько раз
            # с разными значениями переменных.
            self.assertEqual(result, result)
