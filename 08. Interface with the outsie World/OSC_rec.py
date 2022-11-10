from dis import dis
from pythonosc.dispatcher import Dispatcher
from typing import List, Any
from pythonosc.osc_server import BlockingOSCUDPServer, OSCUDPServer

dispatcher = Dispatcher()

def do_something(address: str, *args: List[Any]) -> None:
    print(f'Adress {address}')

    if not len(args) == 6:
        return

    val0, val1, val2, val3, val4, val5=args
    print(val0, val1, val2, val3, val4, val5)

dispatcher.map('/hao/value', do_something)
server = BlockingOSCUDPServer(('localhost', 3000), dispatcher)

while True:
    server.handle_request()