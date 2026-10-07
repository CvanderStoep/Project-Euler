def find_digit_power_numbers(limit):
    """Return sorted numbers below limit equal to a power of their digit sum."""
    max_digit_sum = 9 * len(str(limit - 1))
    matches = []

    for total in range(2, max_digit_sum + 1):
        number = total * total
        while number < limit:
            if number >= 10 and sum(int(digit) for digit in str(number)) == total:
                matches.append(number)
            number *= total

    return sorted(matches)


if __name__ == "__main__":
    for index, number in enumerate(find_digit_power_numbers(10**15), start=1):
        total = sum(int(digit) for digit in str(number))
        print(index, number, total)
      # a_30