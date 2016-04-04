#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Influence:
  UNKNOWN = 1
  DUKE = 2
  ASSASSIN = 3
  CONTESSA = 4
  CAPTAIN = 5
  AMBASSADOR = 6

  _VALUES_TO_NAMES = {
    1: "UNKNOWN",
    2: "DUKE",
    3: "ASSASSIN",
    4: "CONTESSA",
    5: "CAPTAIN",
    6: "AMBASSADOR",
  }

  _NAMES_TO_VALUES = {
    "UNKNOWN": 1,
    "DUKE": 2,
    "ASSASSIN": 3,
    "CONTESSA": 4,
    "CAPTAIN": 5,
    "AMBASSADOR": 6,
  }

class ActionType:
  INCOME = 1
  FOREIGN_AID = 2
  COUP = 3
  TAX = 4
  ASSASSINATE = 5
  STEAL = 6
  EXCHANGE = 7

  _VALUES_TO_NAMES = {
    1: "INCOME",
    2: "FOREIGN_AID",
    3: "COUP",
    4: "TAX",
    5: "ASSASSINATE",
    6: "STEAL",
    7: "EXCHANGE",
  }

  _NAMES_TO_VALUES = {
    "INCOME": 1,
    "FOREIGN_AID": 2,
    "COUP": 3,
    "TAX": 4,
    "ASSASSINATE": 5,
    "STEAL": 6,
    "EXCHANGE": 7,
  }

class CounterActionType:
  NOTHING = 0
  CALL_BLUFF = 1
  BLOCK_FOREIGN_AID = 2
  BLOCK_ASSASINATION = 3
  BLOCK_STEAL = 4

  _VALUES_TO_NAMES = {
    0: "NOTHING",
    1: "CALL_BLUFF",
    2: "BLOCK_FOREIGN_AID",
    3: "BLOCK_ASSASINATION",
    4: "BLOCK_STEAL",
  }

  _NAMES_TO_VALUES = {
    "NOTHING": 0,
    "CALL_BLUFF": 1,
    "BLOCK_FOREIGN_AID": 2,
    "BLOCK_ASSASINATION": 3,
    "BLOCK_STEAL": 4,
  }


class PlayerInit:
  """
  Attributes:
   - id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
  )

  def __init__(self, id=None,):
    self.id = id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('PlayerInit')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      if self.id is None:
        raise TProtocol.TProtocolException(message='Required field id is unset!')
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Player:
  """
  Attributes:
   - id
   - coins
   - influences
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.I32, 'coins', None, None, ), # 2
    None, # 3
    (4, TType.LIST, 'influences', (TType.I32,None), None, ), # 4
  )

  def __init__(self, id=None, coins=None, influences=None,):
    self.id = id
    self.coins = coins
    self.influences = influences

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.coins = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.influences = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.influences.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Player')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.coins != None:
      oprot.writeFieldBegin('coins', TType.I32, 2)
      oprot.writeI32(self.coins)
      oprot.writeFieldEnd()
    if self.influences != None:
      oprot.writeFieldBegin('influences', TType.LIST, 4)
      oprot.writeListBegin(TType.I32, len(self.influences))
      for iter6 in self.influences:
        oprot.writeI32(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      if self.id is None:
        raise TProtocol.TProtocolException(message='Required field id is unset!')
      if self.coins is None:
        raise TProtocol.TProtocolException(message='Required field coins is unset!')
      if self.influences is None:
        raise TProtocol.TProtocolException(message='Required field influences is unset!')
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class CounterAction:
  """
  Attributes:
   - performer
   - counter_action
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'performer', (PlayerInit, PlayerInit.thrift_spec), None, ), # 1
    (2, TType.I32, 'counter_action', None, None, ), # 2
  )

  def __init__(self, performer=None, counter_action=None,):
    self.performer = performer
    self.counter_action = counter_action

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.performer = PlayerInit()
          self.performer.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.counter_action = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('CounterAction')
    if self.performer != None:
      oprot.writeFieldBegin('performer', TType.STRUCT, 1)
      self.performer.write(oprot)
      oprot.writeFieldEnd()
    if self.counter_action != None:
      oprot.writeFieldBegin('counter_action', TType.I32, 2)
      oprot.writeI32(self.counter_action)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      if self.performer is None:
        raise TProtocol.TProtocolException(message='Required field performer is unset!')
      if self.counter_action is None:
        raise TProtocol.TProtocolException(message='Required field counter_action is unset!')
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Action:
  """
  Attributes:
   - action
   - performer
   - recipient
   - counters
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'action', None, None, ), # 1
    (2, TType.STRING, 'performer', None, None, ), # 2
    (3, TType.STRING, 'recipient', None, None, ), # 3
    (4, TType.LIST, 'counters', (TType.STRUCT,(CounterAction, CounterAction.thrift_spec)), [
    ], ), # 4
  )

  def __init__(self, action=None, performer=None, recipient=None, counters=thrift_spec[4][4],):
    self.action = action
    self.performer = performer
    self.recipient = recipient
    if counters is self.thrift_spec[4][4]:
      counters = [
    ]
    self.counters = counters

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.action = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.performer = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.recipient = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.counters = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = CounterAction()
            _elem12.read(iprot)
            self.counters.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Action')
    if self.action != None:
      oprot.writeFieldBegin('action', TType.I32, 1)
      oprot.writeI32(self.action)
      oprot.writeFieldEnd()
    if self.performer != None:
      oprot.writeFieldBegin('performer', TType.STRING, 2)
      oprot.writeString(self.performer)
      oprot.writeFieldEnd()
    if self.recipient != None:
      oprot.writeFieldBegin('recipient', TType.STRING, 3)
      oprot.writeString(self.recipient)
      oprot.writeFieldEnd()
    if self.counters != None:
      oprot.writeFieldBegin('counters', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.counters))
      for iter13 in self.counters:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      if self.action is None:
        raise TProtocol.TProtocolException(message='Required field action is unset!')
      if self.performer is None:
        raise TProtocol.TProtocolException(message='Required field performer is unset!')
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class CoupGame:
  """
  Attributes:
   - id
   - players
   - actions
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.LIST, 'players', (TType.STRUCT,(Player, Player.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'actions', (TType.STRUCT,(Action, Action.thrift_spec)), None, ), # 3
  )

  def __init__(self, id=None, players=None, actions=None,):
    self.id = id
    self.players = players
    self.actions = actions

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.players = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = Player()
            _elem19.read(iprot)
            self.players.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.actions = []
          (_etype23, _size20) = iprot.readListBegin()
          for _i24 in xrange(_size20):
            _elem25 = Action()
            _elem25.read(iprot)
            self.actions.append(_elem25)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('CoupGame')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.players != None:
      oprot.writeFieldBegin('players', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.players))
      for iter26 in self.players:
        iter26.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.actions != None:
      oprot.writeFieldBegin('actions', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.actions))
      for iter27 in self.actions:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      if self.id is None:
        raise TProtocol.TProtocolException(message='Required field id is unset!')
      if self.players is None:
        raise TProtocol.TProtocolException(message='Required field players is unset!')
      if self.actions is None:
        raise TProtocol.TProtocolException(message='Required field actions is unset!')
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)