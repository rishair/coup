import logging
import sys
import getopt
import copy

sys.path.append('gen-py/')

from coup import *
from coup.ttypes import *
from deck import CoupDeck
from player_client import PlayerClient

class Game:
  def __init__(self):
    self.id = "test"
    self.game_in_progress = False
    self.players = {}
    self.deck = CoupDeck()
    self.actions = []
    self.game = self.__gen_game(self)

  def add_player(self, player_client):
    if not self.game_in_progress:
      self.players[player_client.id] = player_client
    else:
      raise Exception("Game already in progress")

  def get_player(self, player_id):
    if isinstance(player_id, Player) or isinstance(player_id, PlayerClient):
      player_id = player_id.id
    if player_id in self.players:
      return self.players[player_id]
    else:
      raise Exception("Player '%s' isn't part of this game" % player_id)

  def __gen_player(self, player, perspective_player = None):
    player = self.get_player(player)
    perspective_player = self.get_player(perspective_player)

    if perspective_player != None and perspective_player.id == player.id:
      return player
    else:
      return player.filter()

  def __gen_game(self, perspective = None):
    game_players = []
    for player in self.players.values():
      game_players.append(self.__gen_player(player, perspective).serialize())
    self.game = CoupGame(self.id, game_players, self.actions)
    return self.game

  def begin(self):
    if not self.game_in_progress:
      self.game_in_progress = True
      for player in self.players.values():
        player.set_coins(2)
        player.add_influences(self.deck.draw(2))

      for player in self.players.values():
        player.client.game_begin(self.__gen_game(player), player.serialize())
    else:
      raise Exception("Game already in progress")

  def winner(self):
    winner = None
    for player in self.players.values():
      if len(player.influences) > 0:
        if winner == None:
          winner = player
        else:
          return None
    return winner

  def take_turn(self):
    pass

  def end(self):
    winner = self.winner()
    if winner == None:
      for player in self.players.values():
        player.client.game_end(self.__gen_game(player), player.serialize())



