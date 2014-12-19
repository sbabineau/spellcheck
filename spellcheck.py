import collections
import sys
import os

class Word(object):

    def __init__(self, word):
        self.word        = word
        self.suggestions = []
    def check(self):
        """will return a boolean in regards to it be spelled correctly"""

    def suggest(self):
        """will return a list of strings for possible spellcheck matches"""
        def _order(self):
            """orders the possible matches"""
