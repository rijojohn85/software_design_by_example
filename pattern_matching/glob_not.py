from typing import Optional
from pattern_matching.glob_null import Match


class Not(Match):
    def __init__(self, pattern: Match, rest: Optional[Match] = None):
        super().__init__(rest=rest)
        self.pattern = pattern

    def _match(self, text: str, start: int) -> Optional[int]:
        end = self.pattern._match(text=text, start=start)
        if end is not None:
            return None
        return self.rest._match(text=text, start=len(text))


# /^abcd+/ in "bcad"
