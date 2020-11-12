# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def last_digit_of_fibonacci_number(n):
    n = n % 60
    if n <= 1:
        return n
    fib = [None] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10
    return fib[n]


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return (last_digit_of_fibonacci_number(n) * last_digit_of_fibonacci_number(n + 1)) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
