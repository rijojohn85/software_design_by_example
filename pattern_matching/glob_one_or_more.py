from typing import Optional
from pattern_matching.glob_null import Match


class OneOrMore(Match):
    def __init__(self, char: str, rest: Optional[Match] = None) -> None:
        super().__init__(rest)
        self.char = char

    def _match(self, text: str, start: int) -> Optional[int]:
        if text[start] != self.char:
            return None
        next_index = next(
            (i for i, char in enumerate(text[start + 1 :]) if char != self.char), -1
        )
        if next_index == -1:
            return self.rest._match(text, len(text))
        return self.rest._match(text, start + next_index + 1)
