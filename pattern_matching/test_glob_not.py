from pattern_matching.glob_not import Not
from pattern_matching.glob_literal import Lit


def test_Not_success():
    # /^abc/ in "def"
    assert Not(Lit("abc")).match("def")


def test_Not_failure():
    # /^abc/ in "abcdef"
    assert not Not(Lit("abc")).match("abcdef")
