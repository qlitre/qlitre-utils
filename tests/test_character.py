from src.qlitreutils import character


def test_is_anagram():
    s1 = 'shibatasatoko'
    s2 = 'satokoshibata'
    assert character.is_anagram(s1, s2)
    s1 = "インターネット土鳩"
    s2 = '鳩ン土ネイトータッ'
    assert character.is_anagram(s1, s2)
    s1 = '静かなるドン'
    s2 = 'ドンファン'
    assert not character.is_anagram(s1, s2)


def test_is_palindrome():
    s = 'madamimadam'
    assert character.is_palindrome(s)
    s = 'satokoshibata'
    assert not character.is_palindrome(s)


def test_cipher():
    key = 3
    s = 'abc'
    encrypt = character.cipher(s, key)
    assert encrypt == 'def'
    key = 4
    s = 'vwxyz'
    encrypt = character.cipher(s, key)
    assert encrypt == 'zabcd'


def test_():
    s = 'ABCU1234067'
    assert character.van_no_check_digit(s)
    s = 'abcu1234067'
    assert character.van_no_check_digit(s)
    s = 'abcu1234067'
    assert character.van_no_check_digit(s)
    s = 'BEAU2427730'
    assert character.van_no_check_digit(s)
    s = 'ABCU12340C7'
    assert not character.van_no_check_digit(s)
    s = 'HOGE123456H'
    assert not character.van_no_check_digit(s)
    s = 'AAA'
    assert not character.van_no_check_digit(s)


def test_run_length_encode():
    s = "aabbbbaaca"
    assert character.run_length_encode(s) == [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]


def test_run_length_decode():
    a_list = [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
    assert character.run_length_decode(a_list) == "aabbbbaaca"


def test_run_length_encode_to_string():
    s = "aabbbbaaca"
    assert character.run_length_encode_to_string(s) == "a2b4a2c1a1"
