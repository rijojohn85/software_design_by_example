from pattern_matching.glob_any import Any
from pattern_matching.glob_literal import Lit


def test_any_matches_empty():
    # /*/ matches ""
    assert Any().match("")


def test_any_matches_entire_string():
    # /*/ matches "ABC"
    assert Any().match("ABC")


def test_any_matches_as_prefix():
    # /*def/ matches "abcdef"
    assert Any(Lit("def")).match("abcdef")


def test_any_matches_as_suffix():
    # /abc*/ matches "abcdef"
    assert Lit("abc", Any()).match("abccdef")


def test_any_matches_interior():
    # /a*c/ matches "abc"
    assert Lit("a", Any(Lit("c"))).match("abc")
