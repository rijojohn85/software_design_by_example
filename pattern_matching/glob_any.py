from pattern_matching.glob_null import Match
from typing import Optional


class Any(Match):
    """
    A * character in our pattern matches zero or more characters,
    so if there are no more matchers in the chain, then this * matches to the end
    of the target string and match returns True right away.
    If there are other matchers, on the other hand,
    we try matching no characters, one character, two characters,
    and so on and see if those other matchers can get us to the end of the string if we do so.
    If none of these possibilities succeeds, the overall match fails
    """

    def __init__(self, rest: Optional[Match] = None) -> None:
        super().__init__(rest=rest)

    def _match(self, text: str, start: int = 0) -> Optional[int]:
        # else, we check if try matching 0, 1,2,3..chars to see if we can get a match and return true
        # eg Any(Lit("def")) = /*def/
        # so we send 1. "abcdef" with start = 0 to Lit.match then we send "abcdef" with start at 1 (matching "bcdef")
        # and so on till we can get a match
        # if we do not get a match, then return False
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None
