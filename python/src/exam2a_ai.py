import sys

from base_ai import BaseAI
from utils import Vocab

EMPTY_STRING = ''


class AI(BaseAI):
    def __init__(self):
        pass

    def answer(self, char, vocab):
        if len(vocab) == 0: return EMPTY_STRING
        for w in vocab:
            if w[0] >= char:
                break
        return vocab.pop(w)


def parse_args(argv):
    cur_word = argv[0]
    words = argv[1:]
    return cur_word, words


if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) == 0:
        raise ValueError("Invalid Argument. Please input current word.")
    cur_word, words = parse_args(argv)
    v = Vocab()
    for w in words:
        v.add(w)
    v.sort()
    ai = AI()
    ans = ai.answer(cur_word[-1], v)
    print(ans)
