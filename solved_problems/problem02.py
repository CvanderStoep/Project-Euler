from helper.utils import fib_generator, fibonacci

# Example usage
if __name__ == "__main__":
    num_terms = 10
    fib_sequence = fibonacci(num_terms)
    print(f"First {num_terms} Fibonacci numbers: {fib_sequence}")

    # Generator function for Fibonacci sequence


    # Example usage
    gen = fib_generator()
    total_fibinacci = 0
    while True:
        next_fib = next(gen)
        if 2<= next_fib <= 4_000_000 and next_fib % 2 == 0:
            total_fibinacci += next_fib
        elif next_fib > 4000000:
            break
        # print(next_fib)
    print(f'Total of even Fibonacci numbers up to 4 million: {total_fibinacci}')
