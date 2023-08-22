#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value[-1] == '.':
            return True
        else:
            return False

    def is_question(self):
        if self.value[-1] == '?':
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value[-1] == '!':
            return True
        else:
            return False
    
    def count_sentences(self):
        new_string = self.value.replace('!', '.')    
        newer_string = new_string.replace('?', '.')  

        sentence_list = newer_string.split('.') 
        sentence_list = [n for n in sentence_list if n]

        return len(sentence_list)