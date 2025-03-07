from pattern_matching.glob_range import Range
from pattern_matching.glob_literal import Lit


def test_Charset_single_char():
    # [a-z] will match "e"
    assert Range(start="a", end="z").match("e")
    # [a-z] will not match "A"
    assert not Range(start="a", end="z").match("A")


def test_Charset_prefix():
    # /[a-z]bc will match "ebc"
    assert Range(start="a", end="z", rest=Lit("bc")).match("ebc")
    # /[a-z]bc will not match "Abc"
    assert not Range(start="a", end="z", rest=Lit("bc")).match("Abc")


def test_Charset_suffix():
    # /bc[a-z] will match "bce"
    assert Lit("bc", Range(start="a", end="z")).match("bce")
    # /bc[a-z] will not match "bcA"
    assert not Lit("bc", Range(start="a", end="z")).match("bcA")
