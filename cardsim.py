import random
import itertools

BOARD_SIZE = 4
board = []
deck = []
NUM_SIM = 100000
for i in range(1, 13):
    deck+= [i, i, -i, -i];

random.shuffle(deck)

def update_board(board, deck):
    while len(board)<BOARD_SIZE:
        try:
            board.append(deck.pop())
        except IndexError:
            return

def print_board(board):
    print "\t".join([str(i) for i in board])

win = 0
for i in range(NUM_SIM):
    if(i%(NUM_SIM/10.0)==0):
        print str(i) + "\t" + str(win)
    is_done = False
    board = []
    deck = []
    for i in range(1, 13):
        deck+= [i, i, -i, -i];
    random.shuffle(deck)
    while not(is_done):
        if(len(deck)!=0):
            update_board(board, deck)
        if(len(deck)==0 and len(board)==0):
            win += 1
            break
        found = False
        selection = None
        for r in range(2, min(BOARD_SIZE, len(board))+1):
            for perm in itertools.combinations(board, r):
                if sum(perm)==0:
                    found = True
                    selection = perm
                    break
            if(found):
                break
        if(not(found)):
            is_done = True
        else:
            for i in selection:
                board.pop(board.index(i))

print float(win)/NUM_SIM
