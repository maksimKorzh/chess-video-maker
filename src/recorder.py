########################################
#
#       PGN to AVI video recorder
#
########################################

import display
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import chess.pgn

fens = []
pgn = open("./games/game.pgn")
first_game = chess.pgn.read_game(pgn)

# Iterate through all moves and play them on a board.
board = first_game.board()
count = 0
for move in first_game.mainline_moves():
    board.push(move)
    fens.append(board.fen())
    count += 1
    #if count == 5: break

# create an output video stream
video = VideoWriter('./videos/game.avi', VideoWriter_fourcc(*'MP42'), 7, (600, 600))


game_board = display.start()

for fen in fens:
    for i in range(10):
        display.update(fen, game_board)
        frame = display.capture(game_board)
        video.write(frame)

display.terminate()
video.release()

