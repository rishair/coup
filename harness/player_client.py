#!/usr/bin/env python

import logging
import sys
import getopt

sys.path.append('gen-py/')

from coup import *
from coup.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class PlayerClient:
  def __init__(self, path, port):
    self.path = path
    self.port = port
    self.influences = []
    self.coins = 0
    try:
      transport = TSocket.TSocket(path, port)
      self.transport = TTransport.TBufferedTransport(transport)
      protocol = TBinaryProtocol.TBinaryProtocol(transport)
      self.client = CoupAgent.Client(protocol)
      transport.open()
      self.id = self.client.initialize_player().id
    except Thrift.TException, tx:
      print '%s' % (tx.message)

  def filter(self):
    filtered_self = copy.copy(self)
    filtered_self.influences = [Influence.UNKNOWN] * len(self.influences)
    return filtered_self

  def serialize(self):
    return Player(self.id, self.coins, self.influences)

  def add_influence(self, influence):
    self.influences.append(influence)

  def add_influences(self, influences):
    self.influences.extend(influences)

  def set_coins(self, coins):
    self.coins = coins

  def add_coins(self, coins):
    self.coins += coins

  def close(self):
    self.transport.close()

