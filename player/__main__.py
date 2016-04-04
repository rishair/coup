import logging
import sys
import getopt

sys.path.append('gen-py/')

from coup import *
from player import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

logging.basicConfig()

if __name__ == "__main__":
  port = 3000
  if len(sys.argv) == 1:
    pass
  else:
    port = int(sys.argv[1])

  handler = RandomizedAgentHandler()
  processor = CoupAgent.Processor(handler)
  transport = TSocket.TServerSocket(port=port)
  tfactory = TTransport.TBufferedTransportFactory()
  pfactory = TBinaryProtocol.TBinaryProtocolFactory()

  server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

  print("Starting server on localhost:%d" % port)
  server.serve()
