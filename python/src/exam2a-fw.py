from subprocess import Popen, PIPE
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


def gen_command(filepath, cur_word, words):
    return '{} {} {}'.format(filepath, cur_word, ' '.join(words))

def parse_args(argv):
    ai1, ai2 = argv[:2]
    # check whether valid ai

    # check whether valid word ?????
    cur_word = argv[2]
    words = argv[3:]
    return None, None, cur_word, words


def print_result(first_flg, status_flg, word):
    if first_flg:
        player = 'FIRST'
    else:
        player = 'SECOND'
    if status_flg:
        status = 'OK'
    else:
        status = 'NG'
    print('{} ({}): {}'.format(player, status, word))


if __name__ == '__main__':
    argv = sys.argv[1:]
    player1, player2, cur_word, words = parse_args(argv)
    v = Vocab()
    for w in words:
        v.add(w)
    v.sort()
    first_flg = True
    while True:
        cmd = gen_command('./myai.sh', cur_word, v.word_list)
        p = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        next_word = out.decode('utf-8').strip()
        if cur_word[-1] != next_word[0]:
            print_result(first_flg, False, next_word)
            first_flg = not first_flg
            break
        print_result(first_flg, True, next_word)
        first_flg = not first_flg
        cur_word = next_word
    if first_flg:
        winner = 'FIRST'
    else:
        winner = 'SECOND'
    print('WIN - {}'.format(winner))
