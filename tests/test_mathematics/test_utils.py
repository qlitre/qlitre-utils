from src.qlitreutils.mathematics import utils


def test_base_10_to_base_n():
    num_10 = 8
    assert utils.base_10_to_base_n(num_10, 2) == 1000

    num_10 = 10
    assert utils.base_10_to_base_n(num_10, 3) == 101


def test_base_n_to_base_10():
    num_2 = 1000
    assert utils.base_n_to_base_10(num_2, 2) == 8
    num_3 = 101
    assert utils.base_n_to_base_10(num_3, 3) == 10


def test_get_divisor_list():
    num = 6
    ans = [1, 2, 3, 6]
    assert utils.get_divisor_list(num) == ans
    num = 1
    ans = [1]
    assert utils.get_divisor_list(num) == ans
    num = 40
    ans = [1, 2, 4, 5, 8, 10, 20, 40]
    assert utils.get_divisor_list(num) == ans


def test_get_gcf_simple():
    a, b = 12, 8
    assert utils.get_gcf_euclid(a, b) == 4


def test_get_gcf_euclid():
    a, b = 12, 8
    assert utils.get_gcf_euclid(a, b) == 4


def test_get_gcf_using_math():
    a, b = 12, 8
    assert utils.get_gcf_euclid(a, b) == 4


def test_get_lcm_using_math():
    a, b = 12, 8
    assert utils.get_lcm_using_math(a, b) == 24


def test_get_lcm_simple():
    a, b = 12, 8
    assert utils.get_lcm_using_math(a, b) == 24


def test_get_gcf_multiple():
    numbers = [8, 12, 20]
    assert utils.get_gcf_multiple(*numbers) == 4


def test_get_lcm_multiple():
    numbers = [8, 12, 20]
    assert utils.get_lcm_multiple(*numbers) == 120


def test_prime_factorize():
    ret = utils.prime_factorize(24)
    assert ret == [2, 2, 2, 3]
    ret = utils.prime_factorize(1)
    assert ret == [1]
    ret = utils.prime_factorize(13)
    assert ret == [13]


def test_n_combi_r_using_mod():
    assert utils.n_combi_r_using_mod(5, 2, 10 ** 9 + 7) == 10
    assert utils.n_combi_r_using_mod(5, 2, 7) == 3


def test_generate_primes_fast():
    a_list = [2, 6, 7, 12]
    ret = list(utils.generate_primes_fast(a_list))
    assert ret[0] == [2]
    assert ret[1] == [2, 3]
    assert ret[2] == [7]
    assert ret[3] == [2, 2, 3]
