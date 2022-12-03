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
