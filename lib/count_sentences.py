#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self.value = None

    def is_sentence(self):
        if self.value and self.value.endswith('.'):
            return True
        return False

    def is_question(self):
        if self.value and self.value.endswith('?'):
            return True
        return False

    def is_exclamation(self):
        if self.value and self.value.endswith('!'):
            return True
        return False

    def count_sentences(self):
        if self.value:
            sentences = self.value.split('.')
            sentences = [s for s in sentences if s]  # Remove empty strings
            return len(sentences)
        return 0
