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
