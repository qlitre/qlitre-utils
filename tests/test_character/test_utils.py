from src.qlitreutils.character import utils


def test_is_anagram():
    s1 = 'shibatasatoko'
    s2 = 'satokoshibata'
    assert utils.is_anagram(s1, s2)
    s1 = "インターネット土鳩"
    s2 = '鳩ン土ネイトータッ'
    assert utils.is_anagram(s1, s2)
    s1 = '静かなるドン'
    s2 = 'ドンファン'
    assert not utils.is_anagram(s1, s2)


def test_is_palindrome():
    s = 'madamimadam'
    assert utils.is_palindrome(s)
    s = 'satokoshibata'
    assert not utils.is_palindrome(s)


def test_cipher():
    key = 3
    s = 'abc'
    encrypt = utils.cipher(s, key)
    assert encrypt == 'def'
    key = 4
    s = 'vwxyz'
    encrypt = utils.cipher(s, key)
    assert encrypt == 'zabcd'


def test_():
    s = 'ABCU1234067'
    assert utils.van_no_check_digit(s)
    s = 'abcu1234067'
    assert utils.van_no_check_digit(s)
    s = 'abcu1234067'
    assert utils.van_no_check_digit(s)
    s = 'BEAU2427730'
    assert utils.van_no_check_digit(s)
    s = 'ABCU12340C7'
    assert not utils.van_no_check_digit(s)
    s = 'HOGE123456H'
    assert not utils.van_no_check_digit(s)
    s = 'AAA'
    assert not utils.van_no_check_digit(s)
