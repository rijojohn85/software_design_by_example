from pattern_matching.glob_charset import Charset
from pattern_matching.glob_literal import Lit


def test_Charset_single_char():
    # [aeiou] will match "e"
    assert Charset(set("aeiou")).match("e")
    # [aeiou] will not match "d"
    assert not Charset(set("aeiou")).match("d")


def test_Charset_prefix():
    # /[aeiou]bc will match "ebc"
    assert Charset(set("aeiou"), Lit("bc")).match("ebc")
    # /[aeiou]bc will match "abc"
    assert Charset(set("aeiou"), Lit("bc")).match("abc")
    # /[aeiou]bc will not match "xbc"
    assert not Charset(set("aeiou"), Lit("bc")).match("xbc")


def test_Charset_suffix():
    # /bc[aeiou] will match "bce"
    assert Lit("bc", Charset(set("aeiou"))).match("bce")
    # /bc[aeiou] will not match "bcx"
    assert not Lit("bc", Charset(set("aeiou"))).match("bcx")
