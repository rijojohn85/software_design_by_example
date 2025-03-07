from typing import Optional
from pattern_matching.glob_null import Match


class Lit(Match):
    def __init__(self, chars: str, rest: Optional[Match] = None):
        super().__init__(rest=rest)
        self.chars = chars

    def _match(self, text: str, start: int = 0) -> Optional[int]:
        # eg if chars(patterns) = abc and text = abcd
        # end = start(0) + len("abc") = 3
        end = start + len(self.chars)

        # ccompares substring of text with chars
        if text[start:end] != self.chars:
            return None

        return self.rest._match(text=text, start=end)
