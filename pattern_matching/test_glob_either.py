from pattern_matching.glob_either import Either
from pattern_matching.glob_literal import Lit


def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")
    # /{a,b}/ matches "b"
    assert Either(Lit("a"), Lit("b")).match("b")


def test_either_two_literals_not_both():
    # /{a,b}/ does not match "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")


def test_eiter_followed_by_literal_match():
    # /{a,b}c/ matches "ac"
    assert Either(left=Lit("a"), right=Lit("b"), rest=Lit("c")).match("ac")


def test_eiter_followed_by_literal_no_match():
    # /{a,b}c/ does not matches "ax"
    assert not Either(left=Lit("a"), right=Lit("b"), rest=Lit("c")).match("ax")
