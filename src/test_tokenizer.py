#!/usr/bin/env python2

import tokenizer

matches_a = '''
0 CHAR 97 97
MATCH
'''

def test_runs():
    assert tokenizer.tokenize(tokenizer.Config(nfa_program=matches_a, input="a")) == 0
