from itertools import permutations, combinations
all_digits = list(range(10))
longest_length = 0
best_digits = None
for digits in combinations(all_digits, 4):
    # digits = list(range(1, 5))
    operators = ['+', '-', '*', '/']
    results = set()

    for perm in permutations(digits):
        a, b, c, d = perm
        for op1 in operators:
            for op2 in operators:
                for op3 in operators:
                    # Different bracket combinations
                    expressions = [
                        f"(({a} {op1} {b}) {op2} {c}) {op3} {d}",
                        f"({a} {op1} ({b} {op2} {c})) {op3} {d}",
                        f"({a} {op1} {b}) {op2} ({c} {op3} {d})",
                        f"{a} {op1} (({b} {op2} {c}) {op3} {d})",
                        f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
                    ]
                    
                    for expr in expressions:
                        try:
                            result = eval(expr)
                            if isinstance(result, (int, float)) and result > 0 and result == int(result):
                                results.add(int(result))
                        except ZeroDivisionError:
                            pass

    sorted_results = sorted(results)
    print(f"Possible outcomes: {sorted_results}")
    print(f"Total unique outcomes: {len(sorted_results)}")

    # Find longest sequence of consecutive integers
    max_length = 0
    max_start = 0

    if sorted_results:
        current_start = sorted_results[0]
        current_length = 1
        
        for i in range(1, len(sorted_results)):
            if sorted_results[i] == sorted_results[i-1] + 1:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
                current_start = sorted_results[i]
                current_length = 1
        
        if current_length > max_length:
            max_length = current_length
            max_start = current_start

    print(f"\nLongest consecutive sequence: {list(range(max_start, max_start + max_length))}")
    print(f"Digits: {digits}, Length of sequence: {max_length}")
    print(f"Length: {max_length}, Starting from: {max_start}")


    if max_length > longest_length:
        longest_length = max_length
        best_digits = digits

print(f"\nBest digits: {best_digits}, Longest sequence length: {longest_length}")
