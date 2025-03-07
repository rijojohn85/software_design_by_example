class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars
        self.rest = rest

    def match(self, text, start=0):
        # eg if chars(patterns) = abc and text = abcd
        # end = start(0) + len("abc") = 3
        end = start + len(self.chars)

        # ccompares substring of text with chars
        if text[start:end] != self.chars:
            return False

        # if other checks are present, run them
        if self.rest:
            return self.rest.match(text=text, start=end)

        # else return true if text does not have any additional characters other than char
        return end == len(text)
