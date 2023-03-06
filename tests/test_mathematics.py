import unittest
from src.qlitreutils import mathematics

assertions = unittest.TestCase('__init__')


def test_base_10_to_base_n():
    num_10 = 8
    assert mathematics.base_10_to_base_n(num_10, 2) == 1000

    num_10 = 10
    assert mathematics.base_10_to_base_n(num_10, 3) == 101


def test_base_n_to_base_10():
    num_2 = 1000
    assert mathematics.base_n_to_base_10(num_2, 2) == 8
    num_3 = 101
    assert mathematics.base_n_to_base_10(num_3, 3) == 10


def test_get_divisor_list():
    num = 6
    ans = [1, 2, 3, 6]
    assert mathematics.get_divisor_list(num) == ans
    num = 1
    ans = [1]
    assert mathematics.get_divisor_list(num) == ans
    num = 40
    ans = [1, 2, 4, 5, 8, 10, 20, 40]
    assert mathematics.get_divisor_list(num) == ans


def test_get_divisor_count():
    num = 6
    ans = [1, 2, 3, 6]
    assert mathematics.get_divisor_count(num) == len(ans)
    num = 1
    assert mathematics.get_divisor_count(num) == 1
    num = 40
    ans = [1, 2, 4, 5, 8, 10, 20, 40]
    assert mathematics.get_divisor_count(num) == len(ans)


def test_get_gcf_simple():
    a, b = 12, 8
    assert mathematics.get_gcf_euclid(a, b) == 4


def test_get_gcf_euclid():
    a, b = 12, 8
    assert mathematics.get_gcf_euclid(a, b) == 4


def test_get_gcf_using_math():
    a, b = 12, 8
    assert mathematics.get_gcf_euclid(a, b) == 4


def test_get_lcm_using_math():
    a, b = 12, 8
    assert mathematics.get_lcm_using_math(a, b) == 24


def test_get_lcm_simple():
    a, b = 12, 8
    assert mathematics.get_lcm_using_math(a, b) == 24


def test_get_gcf_multiple():
    numbers = [8, 12, 20]
    assert mathematics.get_gcf_multiple(*numbers) == 4


def test_get_lcm_multiple():
    numbers = [8, 12, 20]
    assert mathematics.get_lcm_multiple(*numbers) == 120


def test_is_prime():
    assert mathematics.is_prime(3)
    assert not mathematics.is_prime(4)
    assert mathematics.is_prime(17)
    assert mathematics.is_prime(23)


def test_prime_factorize():
    ret = mathematics.prime_factorize(24)
    assert ret == [2, 2, 2, 3]
    ret = mathematics.prime_factorize(1)
    assert ret == [1]
    ret = mathematics.prime_factorize(13)
    assert ret == [13]


def test_eratos_sieve():
    ret = mathematics.eratos_sieve(5)
    assert ret == [2, 3, 5]
    ret = mathematics.eratos_sieve(1)
    assert not ret
    ret = mathematics.eratos_sieve(10)
    assert ret == [2, 3, 5, 7]
    ret = mathematics.eratos_sieve(0)
    assert not ret


def test_n_combi_r():
    assert mathematics.n_combi_r(4, 2) == 6
    assert mathematics.n_combi_r(3, 3) == 1


def test_n_combi_r_using_mod():
    assert mathematics.n_combi_r_using_mod(5, 2, 10 ** 9 + 7) == 10
    assert mathematics.n_combi_r_using_mod(5, 2, 7) == 3


def test_generate_primes_fast():
    a_list = [2, 6, 7, 12]
    ret = list(mathematics.generate_primes_fast(a_list))
    assert ret[0] == [2]
    assert ret[1] == [2, 3]
    assert ret[2] == [7]
    assert ret[3] == [2, 2, 3]


def test_power():
    mod = 10 ** 9 + 7
    a = 2
    b = 3
    max_b = 10 ** 18
    assert mathematics.power(a, b, mod, max_b) == 8
    a = 123456789
    b = 123456789012345678
    assert mathematics.power(a, b, mod, max_b) == 3599437


def test_division_using_mod():
    mod = 10 ** 9 + 7
    a = 6
    b = 3
    assert mathematics.division_using_mod(a, b, mod) == 2
    # 77777の組み合わせから44444を選ぶ方法
    n = 77777
    r = 44444
    # 分子
    a = 1
    for i in range(1, n + 1):
        a *= i
        a = a % mod
    # 分母
    b = 1
    for i in range(1, r + 1):
        b *= i
        b = b % mod
    for i in range(1, n - r + 1):
        b *= i
        b = b % mod

    assert mathematics.division_using_mod(a, b, mod) == 409085577


def test_division_using_mod_pow():
    mod = 10 ** 9 + 7
    a = 6
    b = 3
    assert mathematics.division_using_mod_pow(a, b, mod) == 2
    # 77777の組み合わせから44444を選ぶ方法
    n = 77777
    r = 44444
    # 分子
    a = 1
    for i in range(1, n + 1):
        a *= i
        a = a % mod
    # 分母
    b = 1
    for i in range(1, r + 1):
        b *= i
        b = b % mod
    for i in range(1, n - r + 1):
        b *= i
        b = b % mod

    assert mathematics.division_using_mod_pow(a, b, mod) == 409085577


def test_cosine_law():
    assert mathematics.cosine_law(3, 4, 90) == 5
    assertions.assertAlmostEqual(mathematics.cosine_law(3, 4, 60), 3.60555127)
