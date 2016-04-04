import sys

sys.path.append('gen-py/')

from coup import *
from coup.ttypes import *
import random

class Deck:
  def __init__(self):
    self.cards = []

  def shuffle(self):
    random.shuffle(self.cards)

  def add(self, card):
    if isinstance(card, list):
      for individual_card in card:
        self.add(individual_card)
    else:
      self.cards.append(card)

  def draw(self, count):
    drawn = []
    for i in range(0, count):
      drawn.append(self.cards.pop())
    return drawn

class CoupDeck(Deck):
  def __init__(self):
    Deck.__init__(self)
    influences = [
      Influence.DUKE,
      Influence.ASSASSIN,
      Influence.CONTESSA,
      Influence.CAPTAIN,
      Influence.AMBASSADOR
    ]

    for influence in influences:
      self.add([influence] * 3)
    self.shuffle()


