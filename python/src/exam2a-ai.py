import sys

from base_ai import ShiritoriAI

EMPTY_STRING = ''


class AI(ShiritoriAI):
    def __init__(self):
        raise NotImplementedError

    def answer(self, char, vocab):
        if len(vocab) == 0: return EMPTY_STRING
        






class Vocab(object):
    def __init__(self):
        self.word_list = []

    def __len__(self):
        return len(self.word_list)

    def add(self, word):
        self.word_list.append(word.lower())

    def sort(self):
        self.word_list = sorted(self.word_list)

    def search(self, char):
        if len(self.word_list) == 0: return EMPTY_STRING
        for i, w in enumerate(self.word_list):
            if w[0] >= char:
                break
        return self.word_list.pop(i)


def parse_args(argv):
    cur_word = argv[0]
    words = argv[1:]
    return cur_word, words


if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) == 0:
        raise ValueError("Invalid Argument. Please indicate current word.")
    cur_word, words = parse_args(argv)
    v = Vocab()
    for w in words:
        v.add(w)
    v.sort()
    next_word = v.search(cur_word[-1])
    print(next_word)
