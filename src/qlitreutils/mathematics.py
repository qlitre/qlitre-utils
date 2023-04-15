"""
数学問題のヘルパー関数
"""

import math
from functools import reduce
from collections import deque


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


def get_divisor_count(num: int) -> int:
    """
    約数の数を返す
    つまり、A*BがNになるようなAとBの組み合わせの数
    """
    if num == 1:
        return 1
    ret = 0
    max_num = int(pow(num, 0.5)) + 1
    for n in range(1, max_num):
        if num % n == 0:
            ret += 1
            div = num // n
            if div != n:
                ret += 1

    return ret


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
    return product // math.gcd(x, y)


def get_lcm_simple(x: int, y: int) -> int:
    """最小公倍数を返す　mathを使わない版"""
    product = x * y
    if y == 0:
        (x, y) = (y, x)

    while y != 0:
        (x, y) = (y, x % y)

    gcf = x
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
        return []
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


def get_primes_set(numbers: list) -> set:
    """数字のリストを受け取り、素因数のセットを返す"""
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
    primes = set()
    for num in numbers:
        x = num
        while 1 < x:
            primes.add(data[x])
            x //= data[x]
    return primes


def eratos_sieve(n: int) -> list:
    """
    エラトステネスのふるい
    素数のリストを返す
    """
    if n <= 1:
        return []
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not primes[i]:
            continue
        for j in range(i * 2, n + 1, i):
            primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


def n_combi_r(n: int, r: int) -> int:
    """n個からr個選ぶ組み合わせ数を返す"""
    # 分子
    numerator = 1
    for i in range(n - r + 1, n + 1):
        numerator *= i
    # 分母　r の階乗
    denominator = 1
    for i in range(1, r + 1):
        denominator *= i
    return numerator // denominator


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


def power(a: int, b: int, mod: int, max_b: int) -> int:
    """
    a の b 乗を m で割った余りを返す関数
    max_b:制約上のbの最大値
    """
    cnt = 1
    while max_b > 1:
        max_b //= 2
        cnt += 1
    p = a
    ret = 1
    for i in range(cnt):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            ret = (ret * p) % mod  # a の 2^i 乗が掛けられるとき
        p = (p * p) % mod
    return ret


def division_using_mod(a: int, b: int, mod: int) -> int:
    """
    a÷b を m で割った余りを返す関数
    Mを素数とし、bをMで割り切れない整数であるとする。
    このときMで割った余りを求める問題では「÷b」を「x b**(m-2)」
    と置き換えても計算結果は変わらない
    """
    return (a * power(b, mod - 2, mod, mod - 2)) % mod


def division_using_mod_pow(a: int, b: int, mod: int) -> int:
    """
    a÷b を m で割った余りを返す関数
    組み込みのpowでバージョン3.8からシンプルに書けるようになった。
    計算結果をxとすると、x * bをmodで割った余りがaになる点も留意する。
    """
    return (a * pow(b, mod - 2, mod)) % mod


def cosine_law(a, b, degree):
    """
    余弦定理
    辺a,bと間の角度が判明している際に、残りの１辺の長さを求める
    """
    radians = math.radians(degree)
    ret = a ** 2 + b ** 2 - 2 * (a * b * math.cos(radians))
    return pow(ret, 0.5)


def generate_lunlun_numbers(limit: int) -> list:
    """
    ルンルン数を小さい順に生成して返す。
    ルンルン数=>正の整数X を(leading zeroなしで)十進数表記した際に、隣り合うどの2つの桁の値についても、差の絶対値が1以下
    ex:
    1234
    1
    334
    """
    ret = []
    # 1桁のルンルン数をキューに入れる
    que = deque(range(1, 10))

    while len(ret) < limit:
        cur_num = que.popleft()
        ret.append(cur_num)
        # 最後の桁の数字
        last_digit = cur_num % 10
        # 最後の桁から1を引いた数
        if last_digit > 0:
            que.append(cur_num * 10 + last_digit - 1)
        # 最後の桁と同じ数
        que.append(cur_num * 10 + last_digit)
        # 最後の桁に1を足した数
        if last_digit < 9:
            que.append(cur_num * 10 + last_digit + 1)
    ret.sort()
    return ret
