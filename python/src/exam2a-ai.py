import sys


class Vocab(object):
    def __init__(self):
        self.word_list = []

    def add(self, word):
        self.word_list.append(word.lower())

    def sort(self):
        self.word_list = sorted(self.word_list)

    def search(self, char):
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
        sys.exit(1)
    cur_word, words = parse_args(argv)
    v = Vocab()
    for w in words:
        v.add(w)
    v.sort()
    next_word = v.search(cur_word[-1])
    print(next_word)