from typing import Optional
from pattern_matching.glob_null import Match


class OneOrMore(Match):
    def __init__(self, char: str, rest: Optional[Match] = None) -> None:
        super().__init__(rest)
        self.char = char

    def _match(self, text: str, start: int) -> Optional[int]:
        # if first char is not self.char return None: fail
        if text[start] != self.char or start >= len(text):
            return None
        # find index after start + 1 where char is not self.char
        next_index = next(
            (i for i, char in enumerate(text[start + 1 :]) if char != self.char), -1
        )
        # if next index == -1, we have reached end of string, so send len(text) else poisition of next char
        index = len(text) if next_index == -1 else (start + next_index + 1)

        # pass it on the to next check.
        return self.rest._match(text, index)
