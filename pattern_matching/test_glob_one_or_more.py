from pattern_matching.glob_literal import Lit
from pattern_matching.glob_one_or_more import OneOrMore


def test_OneOrMore_match_single_char():
    # /a+/ matches "a"
    assert OneOrMore("a").match("aaaa")


def test_OneOrMore_match_prefix_lit():
    # /a+"bc"/ matches "aabc"
    assert OneOrMore("a", Lit("bc")).match("aabc")


def test_OneOrMore_match_suffix_lit():
    # /"bc"a+/ matches ("bcaaaa")
    assert (Lit(chars="bc", rest=OneOrMore("a"))).match("bcaaaa")


def test_OneOrMore_match_suffix_lit_fail():
    # /"bc"a+/ fails to match ("bcc")
    assert not (Lit(chars="bc", rest=OneOrMore("a"))).match("bcc")
