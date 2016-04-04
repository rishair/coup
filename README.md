Battle Coup
==========
A framework to play your artisan hand-crafted Coup strategies against others. Included in this package is a game harness (server) to play players against each other and a player (client). The game harness is responsible for orchestrating the game flow and collecting players while the players are thrift-based servers that are responsible for responding to game events.

### Requirements
```bash
git clone https://github.com/rishair/coup.git
pip install -r requirements.txt`
```
### Generating Thrift Bindings
```bash
thrift -r --gen py coup.thrift
```

### Start Player
```bash
python player
```
### Start Game Harness
```bash
python harness
```