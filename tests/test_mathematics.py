import unittest
from src.qlitreutils.mathematics import (base_10_to_base_n, base_n_to_base_10, get_divisor_list, get_divisor_count,
                                         get_gcf_euclid, get_gcf_using_math, get_lcm_using_math, get_lcm_multiple,
                                         get_gcf_multiple, is_prime, prime_factorize, eratos_sieve, n_combi_r,
                                         n_combi_r_using_mod, generate_primes_fast, get_primes_set, power,
                                         division_using_mod, division_using_mod_pow, cosine_law,
                                         generate_lunlun_numbers, count_set_bits_at_position)

assertions = unittest.TestCase('__init__')


def test_base_10_to_base_n():
    num_10 = 8
    assert base_10_to_base_n(num_10, 2) == 1000

    num_10 = 10
    assert base_10_to_base_n(num_10, 3) == 101


def test_base_n_to_base_10():
    num_2 = 1000
    assert base_n_to_base_10(num_2, 2) == 8
    num_3 = 101
    assert base_n_to_base_10(num_3, 3) == 10


def test_get_divisor_list():
    num = 6
    ans = [1, 2, 3, 6]
    assert get_divisor_list(num) == ans
    num = 1
    ans = [1]
    assert get_divisor_list(num) == ans
    num = 40
    ans = [1, 2, 4, 5, 8, 10, 20, 40]
    assert get_divisor_list(num) == ans


def test_get_divisor_count():
    num = 6
    ans = [1, 2, 3, 6]
    assert get_divisor_count(num) == len(ans)
    num = 1
    assert get_divisor_count(num) == 1
    num = 40
    ans = [1, 2, 4, 5, 8, 10, 20, 40]
    assert get_divisor_count(num) == len(ans)


def test_get_gcf_simple():
    a, b = 12, 8
    assert get_gcf_euclid(a, b) == 4


def test_get_gcf_euclid():
    a, b = 12, 8
    assert get_gcf_euclid(a, b) == 4


def test_get_gcf_using_math():
    a, b = 12, 8
    assert get_gcf_using_math(a, b) == 4


def test_get_lcm_using_math():
    a, b = 12, 8
    assert get_lcm_using_math(a, b) == 24


def test_get_lcm_simple():
    a, b = 12, 8
    assert get_lcm_using_math(a, b) == 24


def test_get_gcf_multiple():
    numbers = [8, 12, 20]
    assert get_gcf_multiple(*numbers) == 4


def test_get_lcm_multiple():
    numbers = [8, 12, 20]
    assert get_lcm_multiple(*numbers) == 120


def test_is_prime():
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(17)
    assert is_prime(23)


def test_prime_factorize():
    ret = prime_factorize(24)
    assert ret == [2, 2, 2, 3]
    ret = prime_factorize(1)
    assert ret == []
    ret = prime_factorize(13)
    assert ret == [13]


def test_eratos_sieve():
    ret = eratos_sieve(5)
    assert ret == [2, 3, 5]
    ret = eratos_sieve(1)
    assert not ret
    ret = eratos_sieve(10)
    assert ret == [2, 3, 5, 7]
    ret = eratos_sieve(0)
    assert not ret


def test_n_combi_r():
    assert n_combi_r(4, 2) == 6
    assert n_combi_r(3, 3) == 1


def test_n_combi_r_using_mod():
    assert n_combi_r_using_mod(5, 2, 10 ** 9 + 7) == 10
    assert n_combi_r_using_mod(5, 2, 7) == 3


def test_generate_primes_fast():
    a_list = [2, 6, 7, 12]
    ret = list(generate_primes_fast(a_list))
    assert ret[0] == [2]
    assert ret[1] == [2, 3]
    assert ret[2] == [7]
    assert ret[3] == [2, 2, 3]


def test_get_primes_set():
    assert get_primes_set([2, 3, 4, 5, 6, 7, 8, 9, 10]) == {2, 3, 5, 7}
    assert get_primes_set([11, 13, 17, 19]) == {11, 13, 17, 19}
    assert get_primes_set([12, 15, 18, 21]) == {2, 3, 5, 7}
    assert get_primes_set([2, 2, 2, 2]) == {2}
    assert get_primes_set([3, 3, 3, 3]) == {3}


def test_power():
    mod = 10 ** 9 + 7
    a = 2
    b = 3
    assert power(a, b, mod) == 8
    a = 123456789
    b = 123456789012345678
    assert power(a, b, mod) == 3599437


def test_division_using_mod():
    mod = 10 ** 9 + 7
    a = 6
    b = 3
    assert division_using_mod(a, b, mod) == 2
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

    assert division_using_mod(a, b, mod) == 409085577


def test_division_using_mod_pow():
    mod = 10 ** 9 + 7
    a = 6
    b = 3
    assert division_using_mod_pow(a, b, mod) == 2
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

    assert division_using_mod_pow(a, b, mod) == 409085577


def test_cosine_law():
    assert cosine_law(3, 4, 90) == 5
    assertions.assertAlmostEqual(cosine_law(3, 4, 60), 3.60555127)


def test_generate_lunlun_numbers():
    # 最初の10個のルンルン数をテスト
    first_10_lunlun_numbers = generate_lunlun_numbers(10)
    assert first_10_lunlun_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 最初の15個のルンルン数をテスト
    first_20_lunlun_numbers = generate_lunlun_numbers(20)
    assert first_20_lunlun_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 21, 22, 23, 32, 33, 34, 43, 44]

    # 100000番目のルンルン数をテスト
    lunlun_100000 = generate_lunlun_numbers(100000)[-1]
    assert lunlun_100000 == 3234566667


class TestCountSetBitsAtPosition(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(count_set_bits_at_position(20, 2), 9)
        self.assertEqual(count_set_bits_at_position(10, 0), 5)
        self.assertEqual(count_set_bits_at_position(10, 1), 5)
        self.assertEqual(count_set_bits_at_position(20, 3), 8)
        self.assertEqual(count_set_bits_at_position(0, 2), 0)

    def test_edge_cases(self):
        self.assertEqual(count_set_bits_at_position(0, 0), 0)
        self.assertEqual(count_set_bits_at_position(1, 0), 1)
        self.assertEqual(count_set_bits_at_position(1, 1), 0)
        self.assertEqual(count_set_bits_at_position(2, 1), 1)
        self.assertEqual(count_set_bits_at_position(3, 1), 2)

    def test_large_cases(self):
        self.assertEqual(count_set_bits_at_position(1023, 10), 0)
        self.assertEqual(count_set_bits_at_position(1024, 10), 1)
        self.assertEqual(count_set_bits_at_position(1048575, 20), 0)
        self.assertEqual(count_set_bits_at_position(1048576, 20), 1)
