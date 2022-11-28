import math
from functools import reduce


def base_10_to_base_n(num_10: int, n: int) -> int:
    """10進数をn進数に変換して返す"""
    if n == 1:
        raise ValueError("1進数には対応していません")
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n = str(num_10 % n) + str_n
        num_10 = num_10 // n
    return int(str_n)


def base_n_to_base_10(num_n: int, n: int) -> int:
    """n進数を10進数に変換して返す"""
    num_10 = 0
    for s in str(num_n):
        num_10 = num_10 * n
        num_10 += int(s)
    return num_10


def get_divisor_list(num: int) -> list:
    """約数のリストを返す"""
    if num == 1:
        return [1]
    divisors = []
    # 平方根
    max_num = int(pow(num, 0.5)) + 1

    for n in range(1, max_num):
        if num % n == 0:
            divisors.append(n)
            div = num // n
            if div != n:
                divisors.append(div)

    divisors.sort()
    return divisors


def get_gcf_simple(x: int, y: int) -> int:
    """最大公約数を返す。シンプルな実装"""
    if x < 0 or y < 0:
        raise ValueError('テストできるのは正の整数だけ')
    if x == 0:
        return y
    if y == 0:
        return x
    gcf_value = None
    if x > y:
        smaller = y
    else:
        smaller = x

    for divisor in range(1, smaller + 1):
        if (x % divisor == 0) and (y % divisor == 0):
            gcf_value = divisor
    return gcf_value


def get_gcf_euclid(x: int, y: int) -> int:
    """最大公約数を返す。ユークリッドの互除法"""
    if y == 0:
        (x, y) = (y, x)

    while y != 0:
        (x, y) = (y, x % y)

    return x


def get_gcf_using_math(x: int, y: int) -> int:
    """最大公約数を返す"""
    return math.gcd(x, y)


def get_lcm_using_math(x: int, y: int) -> int:
    """最小公倍数を返す"""
    product = x * y
    return product // get_gcf_using_math(x, y)


def get_lcm_simple(x: int, y: int) -> int:
    """最小公倍数を返す　mathを使わない版"""
    gcf = get_gcf_euclid(x, y)
    product = x * y
    return int(product / gcf)


def get_gcf_multiple(*numbers) -> int:
    """
    引数を複数指定した最大公約数
    """
    if len(numbers) <= 1:
        raise ValueError('要素を２つ以上指定してください')

    return reduce(get_gcf_using_math, numbers)


def get_lcm_multiple(*numbers) -> int:
    """
    引数を複数指定した最小公倍数
    """
    if len(numbers) <= 1:
        raise ValueError('要素を２つ以上指定してください')

    return reduce(get_lcm_using_math, numbers)


def is_prime(n: int) -> bool:
    """素数の場合Trueを返す"""
    for i in range(2, int(pow(n, .5)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorize(n: int) -> list:
    """素因数分解リストを返す"""
    if n == 1:
        return [1]
    ret = []
    while n % 2 == 0:
        ret.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ret.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        ret.append(n)
    return ret


def generate_primes_fast(numbers: list):
    """数字のリストを受け取り素因数分解リストをyieldして返す"""
    max_val = max(numbers)
    data = [0] * (max_val + 1)
    for i in range(2, max_val + 1):
        if data[i] != 0:
            continue
        for k in range(1, max_val + 1):
            if i * k < max_val + 1:
                if data[i * k] == 0:
                    data[i * k] = i
            else:
                break

    for num in numbers:
        primes = []
        x = num
        while 1 < x:
            primes.append(data[x])
            x //= data[x]
        yield primes


def n_combi_r_using_mod(n, r, mod):
    # 分子
    numerator = 1
    for i in range(n - r + 1, n + 1):
        numerator *= i
        numerator %= mod
    # 分母　r の階乗
    denominator = 1
    for i in range(1, r + 1):
        denominator *= i
        denominator %= mod
    # 分母の逆元
    denominator_inverse_element = pow(denominator, -1, mod)
    return numerator * denominator_inverse_element % mod
