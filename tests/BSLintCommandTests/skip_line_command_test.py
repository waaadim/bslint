import unittest
import bslint
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import bslint.commands as commands


class TestSkipLineCommand(unittest.TestCase):

    WARNINGS = 'Warnings'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.ErrorMessageHandler()

    def testSkipLineCommandSkipTypo(self):
        config = bslint.load_config_file()
        commands.config = config
        lexer = bslint.Lexer(config)
        exp_result = []
        result = lexer.lex("'BSLint_skip_line \nxgygu= 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandEmptyLine(self):
        config = bslint.load_config_file()
        lexer = bslint.Lexer(config)
        exp_result = []
        result = lexer.lex("'BSLint_skip_line \n\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandWithTypo(self):
        config = bslint.load_config_file()
        commands.config = config
        lexer = bslint.Lexer(config)
        exp_result = [self.error.get(ErrConst.TYPO_IN_CODE, [3])]
        result = lexer.lex("'BSLint_skip_line \ny=4\nxgygu = 22\n")
        self.assertEqual(exp_result, result[self.WARNINGS])

    def testSkipLineCommandInactive(self):
        config = bslint.load_config_file("BSLintCommands/inactive-skip-line-config.json")
        commands.config = config
        lexer = bslint.Lexer(config)
        exp_result = [self.error.get(ErrConst.TYPO_IN_CODE, [2])]
        result = lexer.lex("'BSLint_skip_line \nxgygu = 22\ny = 4")
        self.assertEqual(exp_result, result[self.WARNINGS])