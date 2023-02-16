"""
文字列操作のユーティリティ
"""

import string


def is_anagram(s1: str, s2: str) -> bool:
    """アナグラム判定"""
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    return False


def is_palindrome(s1: str) -> bool:
    """回文判定"""
    s = s1.lower()
    if s == s[::-1]:
        return True
    return False


def cipher(a_string: str, key: int) -> str:
    """シーザー暗号を返す。アルファベット限定"""
    # ['ABCD...']
    uppercase = string.ascii_uppercase
    # ['abcd...']
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            # indexを特定し、% 26で折り返す
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


def van_no_check_digit(van_no: str) -> bool:
    """コンテナNOのチェックディジット"""
    if len(van_no) != 11:
        return False
    van_no = van_no.upper()
    for i, c in enumerate(van_no):
        if i < 4:
            if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return False
        else:
            if c not in '0123456789':
                return False

    d = {'A': 10, 'B': 12, 'C': 13, 'D': 14,
         'E': 15, 'F': 16, 'G': 17, 'H': 18,
         'I': 19, 'J': 20, 'K': 21, 'L': 23,
         'M': 24, 'N': 25, 'O': 26, 'P': 27,
         'Q': 28, 'R': 29, 'S': 30, 'T': 31,
         'U': 32, 'V': 34, 'W': 35, 'X': 36,
         'Y': 37, 'Z': 38}

    a_sum = 0
    for i in range(10):
        prod = 2 ** i
        char = van_no[i]
        if i < 4:
            num = d.get(char)
        else:
            num = int(char)
        a_sum += prod * num

    b_sum = a_sum // 11
    b_sum *= 11

    ans = a_sum - b_sum
    if ans >= 10:
        ans = int(str(ans)[-1])
    return int(van_no[-1]) == ans
