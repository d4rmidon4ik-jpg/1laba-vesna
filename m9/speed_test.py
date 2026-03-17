import speed_compare
import time

def sum_squares_python(numbers):
    result = 0
    for x in numbers:
        result += x * x
    return result

numbers = [i for i in range(1, 10_000_000)] 

start = time.time()
rust_result = speed_compare.sum_squares_rust(numbers)
rust_time = time.time() - start

start = time.time()
python_result = sum_squares_python(numbers)
python_time = time.time() - start

print(f"Rust время:   {rust_time:.4f} сек")
print(f"Python время: {python_time:.4f} сек")
print(f"Rust быстрее в {python_time/rust_time:.1f} раз")
