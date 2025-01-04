import unittest


def bartender(order):
    if isinstance(order, int) and order > 0:
        return order
    return 'Извините, я не могу вас обслужить!'


class TestBar(unittest.TestCase):
    """Тестируем функцию bartender."""

    def test_bartender(self):
        test_cases = [
            (5, 5),  # Заказывает 5 стаканов газировки
            (0, 'Извините, я не могу вас обслужить!'),  # Заказывает 0 стаканов газировки
            (0.33, 'Извините, я не могу вас обслужить!'),  # Заказывает 0.33 стакана газировки
            (-1.999999, 'Извините, я не могу вас обслужить!'),  # Заказывает -1.999999 стакана газировки
            ('фываолдж', 'Извините, я не могу вас обслужить!'),  # Заказывает фываолдж стаканов газировки
        ]
        
        for order, expected in test_cases:
            with self.subTest(order=order):
                self.assertEqual(
                    bartender(order), expected,
                    f'Ошибка для заказа: {order}'
                )


if __name__ == '__main__':
    unittest.main()
