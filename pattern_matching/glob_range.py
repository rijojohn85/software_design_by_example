from typing import Optional, Set
from pattern_matching.glob_null import Match, CommonMatch


class Range(CommonMatch):
    def __init__(self, start: str, end: str, rest: Optional[Match] = None):
        super().__init__(rest)
        self.char_set = {chr(c) for c in range(ord(start), ord(end) + 1)}
