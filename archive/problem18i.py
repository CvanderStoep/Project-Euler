def simple_sieve(limit):
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    root = int(limit**0.5)
    for num in range(2, root + 1):
        if sieve[num]:
            step = num
            start = num * num
            sieve[start:limit + 1:step] = b'\x00' * (((limit - start) // step) + 1)
    return [i for i, present in enumerate(sieve) if present]


def primes_in_range(low, high, segment_size=10_000_000):
    if high <= low:
        return
    low = max(low, 2)
    limit = int(high**0.5) + 1
    base_primes = simple_sieve(limit)
    for segment_low in range(low, high, segment_size):
        segment_high = min(segment_low + segment_size, high)
        segment = bytearray(b'\x01') * (segment_high - segment_low)
        for prime in base_primes:
            start = prime * prime
            if start >= segment_high:
                break
            start = max(start, ((segment_low + prime - 1) // prime) * prime)
            for multiple in range(start, segment_high, prime):
                segment[multiple - segment_low] = 0
        for offset, is_prime in enumerate(segment):
            if is_prime:
                yield segment_low + offset


def multiply_polynomials(a, b, p):
    """Multiply two quadratic polynomials modulo p.

    The input polynomials are represented as tuples of three coefficients
    (a0, a1, a2) corresponding to a0 + a1*x + a2*x^2. The multiplication
    is performed with a reduction step that applies the relation x^3 = 4*x - 3
    before taking the result modulo p.

    Args:
        a: Tuple[int, int, int] representing the first polynomial.
        b: Tuple[int, int, int] representing the second polynomial.
        p: Integer modulus.

    Returns:
        Tuple[int, int, int] for the resulting polynomial coefficients modulo p.
    """
    a0, a1, a2 = a
    b0, b1, b2 = b
    c0 = (a0 * b0) % p
    c1 = (a0 * b1 + a1 * b0) % p
    c2 = (a0 * b2 + a1 * b1 + a2 * b0) % p
    c3 = (a1 * b2 + a2 * b1) % p
    c4 = (a2 * b2) % p
    new_c0 = (c0 - 4 * c3) % p
    new_c1 = (c1 + 3 * c3 - 4 * c4) % p
    new_c2 = (c2 + 3 * c4) % p
    return (new_c0, new_c1, new_c2)


def pow_poly(poly, exponent, p):
    """Raise a polynomial to an integer power modulo p.

    Args:
        poly: A tuple of three coefficients (a0, a1, a2) representing
            the polynomial a0 + a1*x + a2*x^2.
        exponent: A non-negative integer exponent.
        p: A positive integer modulus.

    Returns:
        A tuple of three coefficients for the polynomial result = poly**exponent
        computed modulo p.
    """
    result = (1, 0, 0)
    base = poly
    while exponent:
        if exponent & 1:
            result = multiply_polynomials(result, base, p)
        base = multiply_polynomials(base, base, p)
        exponent >>= 1
    return result


def product_poly(p):
    """Compute the product of (x**3 - 3*x + 4) for x in 0..p-1 modulo p.

    The polynomial product is computed directly for small p values and
    using an algebraic reduction for larger p values. The reduction relies
    on polynomial exponentiation modulo p and a deterministic relation
    for the resulting coefficients.

    Args:
        p: A non-negative integer modulus. When p <= 0, the function
            returns 1 as the empty product.

    Returns:
        The product of the polynomial values for x in range(p), reduced
        modulo p.
    """
    if p <= 0:
        return 1
    if p <= 3:
        prod = 1
        for x in range(p):
            prod = (prod * (x**3 - 3 * x + 4)) % p
        return prod

    x_poly = (0, 1, 0)
    c0, c1, c2 = pow_poly(x_poly, p, p)
    a0 = c0 % p
    a1 = (c1 - 1) % p
    a2 = c2 % p

    d = (3 * a2 + a0) % p
    b00 = a0
    b01 = (-4 * a2) % p
    b02 = (-4 * a1) % p
    b10 = a1
    b11 = d
    b12 = (-4 * a2 + 3 * a1) % p
    b20 = a2
    b21 = a1
    b22 = d

    det = (
        b00 * ((b11 * b22 - b12 * b21) % p)
        - b01 * ((b10 * b22 - b12 * b20) % p)
        + b02 * ((b10 * b21 - b11 * b20) % p)
    ) % p
    return (-det) % p


if __name__ == '__main__':

    low = 1_000_000_000
    high = 1_100_000_000

    total_sum = 0
    for prime in primes_in_range(low, high): 
        print(f"Processing prime: {prime}")   
        total_sum = (total_sum + product_poly(prime))
    print(f"Total sum of products modulo p for all primes between {low} and {high}: {total_sum}")

# 842507000531275