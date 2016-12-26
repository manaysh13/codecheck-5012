import os
import sys

from exam2a_ai import AI
from utils import Vocab


def activate_ai(ai_file):
    cmd_line = [line.strip() for line in open(ai_file) if line.startswith('python')]
    if len(cmd_line) != 1:
        raise IOError("Invalid AI system file format. ")
    pyfilepath = cmd_line[0].split()[1]
    filename = os.path.splitext(os.path.basename(pyfilepath))[0]
    exec("from {} import AI".format(filename))
    return AI()


def parse_args(argv):
    ai_file1, ai_file2 = argv[:2]
    if not os.path.exists(ai_file1) or not os.path.exists(ai_file2):
        raise IOError("No AI system files.")
    player1 = activate_ai(ai_file1)
    player2 = activate_ai(ai_file2)
    cur_word = argv[2]
    words = argv[3:]
    return player1, player2, cur_word, words


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

    # build AI
    # player1 = AI()
    # player2 = AI()

    first_flg = True
    while True:
        if first_flg:
            cur_player = player1
        else:
            cur_player = player2
        next_word = cur_player.answer(cur_word[-1], v)
        # check whether the answer is valid
        if (next_word == '') or (cur_word[-1] != next_word[0]):
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
