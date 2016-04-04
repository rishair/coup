namespace py coup

typedef string PlayerId
typedef string GameId

struct PlayerInit {
  1: required PlayerId id
}

enum Influence {
  UNKNOWN       = 1
  DUKE          = 2
  ASSASSIN      = 3
  CONTESSA      = 4
  CAPTAIN       = 5
  AMBASSADOR    = 6
}

struct Player {
  1: required PlayerId id
  2: required i32 coins
  4: required list<Influence> influences
}

enum ActionType {
  INCOME        = 1
  FOREIGN_AID   = 2
  COUP          = 3
  TAX           = 4
  ASSASSINATE   = 5
  STEAL         = 6
  EXCHANGE      = 7
}

enum CounterActionType {
  NOTHING             = 0
  CALL_BLUFF          = 1
  BLOCK_FOREIGN_AID   = 2
  BLOCK_ASSASINATION  = 3
  BLOCK_STEAL         = 4
}

struct CounterAction {
  1: required PlayerInit performer
  2: required CounterActionType counter_action
}

struct Action {
  1: required ActionType action
  2: required PlayerId performer
  3: optional PlayerId recipient
  4: optional list<CounterAction> counters = []
}

struct CoupGame {
  1: required GameId id
  2: required list<Player> players
  3: required list<Action> actions
}

service CoupAgent {
  PlayerInit initialize_player()

  void game_begin(
    1: CoupGame game,
    2: Player player
  )

  CounterAction respond_to_action(
    1: CoupGame game,
    2: Action action
  )

  Action take_turn(
    1: CoupGame game
  )

  list<Influence> select_influences(
    1: CoupGame game,
    2: list<Influence> influences,
    3: i32 count
  )
}

