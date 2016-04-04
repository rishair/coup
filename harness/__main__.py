import logging
import sys
import getopt

sys.path.append('gen-py/')

logging.basicConfig()

from game import Game
from player_client import PlayerClient

if __name__ == "__main__":
  game = Game()
  game.add_player(PlayerClient("localhost", 3000))
  game.begin()
  while not game.winner() == None:
    game.take_turn()
  game.end()
