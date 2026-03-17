use pyo3::prelude::*;
use std::time::Instant;

/// Функция на Rust для суммирования квадратов (доступна из Python)
#[pyfunction]
fn sum_squares_rust(numbers: Vec<i64>) -> i64 {
    numbers.iter().map(|x| x * x).sum()
}

/// Функция для замера времени выполнения (доступна из Python)
#[pyfunction]
fn benchmark_rust(numbers: Vec<i64>) -> (i64, f64) {
    let start = Instant::now();
    let result = sum_squares_rust(numbers);
    let duration = start.elapsed();
    (result, duration.as_secs_f64())
}

/// Модуль Python
#[pymodule]
fn speed_compare(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_squares_rust, m)?)?;
    m.add_function(wrap_pyfunction!(benchmark_rust, m)?)?;
    Ok(())
}

/// Тесты
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum_squares_rust_small() {
        let numbers = vec![1, 2, 3, 4, 5];
        let result = sum_squares_rust(numbers);
        assert_eq!(result, 55);
    }

    #[test]
    fn test_sum_squares_rust_empty() {
        let numbers: Vec<i64> = vec![];
        let result = sum_squares_rust(numbers);
        assert_eq!(result, 0);
    }

    #[test]
    fn test_sum_squares_rust_negative() {
        let numbers = vec![-1, -2, -3];
        let result = sum_squares_rust(numbers);
        assert_eq!(result, 14);
    }

    #[test]
    fn test_benchmark_rust_returns_tuple() {
        let numbers = vec![1, 2, 3];
        let (result, duration) = benchmark_rust(numbers);
        assert_eq!(result, 14);
        assert!(duration >= 0.0);
    }
}