# python3
import math

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    i = 0
    while n > 0:
        summands.append[i]
        n -= i
        i += 1
        if n < i:
            return summands




if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
