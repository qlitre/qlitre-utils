from src.qlitreutils.character import (is_anagram,
                                       is_palindrome,
                                       cipher,
                                       van_no_check_digit,
                                       run_length_encode,
                                       run_length_decode,
                                       run_length_encode_to_string)


def test_is_anagram():
    s1 = 'shibatasatoko'
    s2 = 'satokoshibata'
    assert is_anagram(s1, s2)
    s1 = "インターネット土鳩"
    s2 = '鳩ン土ネイトータッ'
    assert is_anagram(s1, s2)
    s1 = '静かなるドン'
    s2 = 'ドンファン'
    assert not is_anagram(s1, s2)


def test_is_palindrome():
    s = 'madamimadam'
    assert is_palindrome(s)
    s = 'satokoshibata'
    assert not is_palindrome(s)


def test_cipher():
    key = 3
    s = 'abc'
    encrypt = cipher(s, key)
    assert encrypt == 'def'
    key = 4
    s = 'vwxyz'
    encrypt = cipher(s, key)
    assert encrypt == 'zabcd'


def test_van_no_check_digit():
    s = 'ABCU1234067'
    assert van_no_check_digit(s)
    s = 'abcu1234067'
    assert van_no_check_digit(s)
    s = 'abcu1234067'
    assert van_no_check_digit(s)
    s = 'BEAU2427730'
    assert van_no_check_digit(s)
    s = 'ABCU12340C7'
    assert not van_no_check_digit(s)
    s = 'HOGE123456H'
    assert not van_no_check_digit(s)
    s = 'AAA'
    assert not van_no_check_digit(s)


def test_run_length_encode():
    s = "aabbbbaaca"
    assert run_length_encode(s) == [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]


def test_run_length_decode():
    a_list = [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
    assert run_length_decode(a_list) == "aabbbbaaca"


def test_run_length_encode_to_string():
    s = "aabbbbaaca"
    assert run_length_encode_to_string(s) == "a2b4a2c1a1"
