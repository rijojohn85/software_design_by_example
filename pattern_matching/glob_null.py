from typing import Optional


class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()

    def _match(self, text: str, start: int) -> Optional[int]:
        raise NotImplementedError

    def match(self, text):
        result: int | None = self._match(text, 0)
        return result == len(text)


class Null(Match):
    def __init__(self) -> None:
        self.rest = None

    def _match(self, text: str, start: int) -> int:
        return start


class CommonMatch(Match):
    """
    since both Range and Char set have the same _match function
    """

    def _match(self, text: str, start: int) -> Optional[int]:
        if text[start] not in self.char_set:  # type: ignore
            return None
        return self.rest._match(text, start=start + 1)
