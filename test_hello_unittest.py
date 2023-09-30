import unittest


def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    # assert True == False
    # 2つの整数の和を計算できるメソッド
    def test_2つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))
        self.assertEqual(6, add(2, 4))

    def test_2つの整数の和を計算できる(self):
        self.assertEqual(1, subtraction(4, 3))
        self.assertEqual(2, subtraction(5, 3))


if __name__ == "__main__":
    unittest.main()
