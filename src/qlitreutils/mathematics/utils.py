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
