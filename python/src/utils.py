
import re
import sys


ENG_WORD_MATCHR = r'^[a-z]+$'


# assuming English word
class Vocab(object):
    def __init__(self):
        self.word_list = []

    def __len__(self):
        return len(self.word_list)

    def __iter__(self):
        for i in range(len(self)):
            yield self.word_list[i]

    def add(self, word):
        word = word.lower()  # not concern about whether uppercase or lowercase
        if is_validword(word):
            self.word_list.append(word)
        else:
            sys.stderr.write("Skipping invald word : {}\n".format(word))

    def pop(self, word):
        return self.word_list.pop(self.word_list.index(word))

    def sort(self):
        self.word_list = sorted(self.word_list)


def is_validword(word):
    return re.match(ENG_WORD_MATCHR, word)
