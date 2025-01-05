import unittest


class Calculator:
    """Производит арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()

    def test_divider(self):
        """Проверка правильной работы деления."""
        act = self.calculator.divider(10, 2)
        self.assertEqual(act, 5.0, 'Функция divider некорректно работает с валидными аргументами')

    def test_divider_zero_division(self):
        """Проверка выброса исключения при делении на 0."""
        with self.assertRaises(ZeroDivisionError, msg='Функция divider должна выбрасывать ZeroDivisionError при делении на 0'):
            self.calculator.divider(10, 0)


if __name__ == '__main__':
    unittest.main()
