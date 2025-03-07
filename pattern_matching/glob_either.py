from pattern_matching.glob_null import Match
from typing import Optional


class Either(Match):
    """
    Either/or matching works much the same way.
    If the first alternative matches, we try the rest of the chain.
    If not, we try the second alternative, and if that doesn’t work either, we fail:
    /{a,b}/ matches either a or b
    """

    def __init__(self, left: Match, right: Match, rest: Optional[Match] = None) -> None:
        super().__init__(rest=rest)
        self.left = left
        self.right = right

    def _match(self, text: str, start: int = 0) -> Optional[int]:
        for pat in [self.left, self.right]:
            end = pat._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
