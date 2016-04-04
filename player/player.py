import sys

sys.path.append('gen-py/')

from coup import *
from coup.ttypes import *

class RandomizedAgentHandler:
  def __init__(self):
    pass

  def initialize_player(self):
    print "Initialize Player"
    return PlayerInit("Rishi")

  def game_begin(self, game, player):
    print "GameBegin(%s, %s)" % (game, player)
    pass

  def respond_to_action(self, action):
    print "RespondToAction(%s)" % action
    return CounterAction(CounterActionType.NOTHING)

  def take_turn(self, game):
    print "TakeTurn(%s)" % game
    return Action(ActionType.INCOME)

  def select_influences(self, game, influences, count):
    print "SelectInfluences(%s, %s, %s)" % (game, influences, count)
    return influences[0:count]
