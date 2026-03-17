import unittest
import speed_compare
import time

class TestSpeedCompare(unittest.TestCase):
    
    def setUp(self):
        self.small_numbers = [1, 2, 3, 4, 5]
        self.empty_numbers = []
        self.negative_numbers = [-1, -2, -3]
        
    def test_sum_squares_rust_small(self):
        result = speed_compare.sum_squares_rust(self.small_numbers)
        self.assertEqual(result, 55)
        
    def test_sum_squares_rust_empty(self):
        result = speed_compare.sum_squares_rust(self.empty_numbers)
        self.assertEqual(result, 0)
        
    def test_sum_squares_rust_negative(self):
        result = speed_compare.sum_squares_rust(self.negative_numbers)
        self.assertEqual(result, 14)
        
    def test_benchmark_rust_returns_tuple(self):
        result = speed_compare.benchmark_rust(self.small_numbers)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], float)
        
    def test_consistency_with_python(self):
        def sum_squares_python(numbers):
            return sum(x * x for x in numbers)
        
        rust_result = speed_compare.sum_squares_rust(self.small_numbers)
        python_result = sum_squares_python(self.small_numbers)
        self.assertEqual(rust_result, python_result)
        
    def test_large_input(self):
        numbers = list(range(1, 10001))
        rust_result = speed_compare.sum_squares_rust(numbers)
        # Формула: n(n+1)(2n+1)/6
        expected = (10000 * 10001 * 20001) // 6
        self.assertEqual(rust_result, expected)
        
    def test_performance_benchmark(self):
        numbers = list(range(1, 100000))  # 100 тысяч элементов
        result, duration = speed_compare.benchmark_rust(numbers)
        self.assertGreater(duration, 0)
        self.assertIsNotNone(result)

class TestPythonFunctions(unittest.TestCase):
    
    def test_sum_squares_python(self):
        def sum_squares_python(numbers):
            return sum(x * x for x in numbers)
        
        self.assertEqual(sum_squares_python([1, 2, 3]), 14)
        self.assertEqual(sum_squares_python([]), 0)
        self.assertEqual(sum_squares_python([-1, -2]), 5)

if __name__ == '__main__':
    unittest.main()
