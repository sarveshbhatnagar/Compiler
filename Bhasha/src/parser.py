
class Parser(object):
    """docstring for Parser."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLERATION" and token_value == "var":
                print(token_type, token_value)



            self.token_index += 1
