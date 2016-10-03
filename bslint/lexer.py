from bslint.tokenizer import Tokenizer as Tokenizer


class Lexer(Tokenizer):

    def __init__(self, characters):
        Tokenizer.__init__(self, characters)

    def lex(self):
        return Tokenizer.tokenize(self)

    def check_valid_token(self, preceding_token, current_token):
        return
