from typing import Optional, Set
from pattern_matching.glob_null import CommonMatch, Match


class Charset(CommonMatch):
    def __init__(self, char_set: Set[str], rest: Optional[Match] = None):
        super().__init__(rest)
        self.char_set = char_set

    # def _match(self, text: str, start: int) -> Optional[int]:
    #     if text[start] not in self.char_set:
    #         return None
    #     return self.rest._match(text, start=start + 1)
