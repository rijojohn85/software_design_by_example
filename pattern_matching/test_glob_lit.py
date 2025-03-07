from pattern_matching.glob_literal import Lit


def test_literal_match_entire_string():
    # /abc/ matches "abc"
    assert Lit("abc").match("abc")


def test_literal_substring_no_match():
    # ab does not match abc
    assert not Lit("ab").match("abc")


def test_listernal_superstring_no_match():
    # abc does not match ab
    assert not Lit("abc").match("ab")


def test_liternal_followed_by_literal_match():
    # /a/ + /b/ matches "ab"
    assert Lit("a", Lit("b")).match("ab")


def test_literal_followed_by_liternal_no_match():
    # /a/ + /c/ does not match ab
    assert not Lit("a", Lit("b")).match("ac")
