import random
from typing import List, Tuple

NUM_PLAYERS = 6

# -----------------------------
# Game State Representation
# -----------------------------
class GameState:
    def __init__(self, hands, scores, trick, current_player):
        self.hands = hands              # List[List[int]] cards per player
        self.scores = scores            # List[int] score per player
        self.trick = trick              # Cards played in current trick [(player, card)]
        self.current_player = current_player

    def clone(self):
        return GameState(
            [hand[:] for hand in self.hands],
            self.scores[:],
            self.trick[:],
            self.current_player
        )

# -----------------------------
# Helper Functions
# -----------------------------

def next_player(p):
    return (p + 1) % NUM_PLAYERS


def legal_moves(state: GameState, player: int) -> List[int]:
    return state.hands[player]


def result(state: GameState, move: int) -> GameState:
    new_state = state.clone()
    new_state.hands[new_state.current_player].remove(move)
    new_state.trick.append((new_state.current_player, move))

    # If trick complete
    if len(new_state.trick) == NUM_PLAYERS:
        winner = max(new_state.trick, key=lambda x: x[1])[0]
        new_state.scores[winner] += 1
        new_state.trick = []
        new_state.current_player = winner
    else:
        new_state.current_player = next_player(new_state.current_player)

    return new_state


def terminal(state: GameState) -> bool:
    return all(len(hand) == 0 for hand in state.hands)


def evaluate(state: GameState) -> Tuple[int]:
    return tuple(state.scores)

# -----------------------------
# Max-N Algorithm
# -----------------------------

def maxn(state: GameState, depth: int, player: int) -> Tuple[int]:
    if depth == 0 or terminal(state):
        return evaluate(state)

    best_value = tuple([-float('inf')] * NUM_PLAYERS)

    for move in legal_moves(state, player):
        new_state = result(state, move)
        value = maxn(new_state, depth - 1, new_state.current_player)

        if value[player] > best_value[player]:
            best_value = value

    return best_value

# -----------------------------
# Choosing Best Move
# -----------------------------

def choose_best_move(state: GameState, depth: int) -> int:
    player = state.current_player
    best_move = None
    best_score = tuple([-float('inf')] * NUM_PLAYERS)

    for move in legal_moves(state, player):
        new_state = result(state, move)
        score = maxn(new_state, depth - 1, new_state.current_player)

        if score[player] > best_score[player]:
            best_score = score
            best_move = move

    return best_move

# -----------------------------
# Example Setup
# -----------------------------
if __name__ == "__main__":
    deck = list(range(1, 53))
    random.shuffle(deck)

    hands = [deck[i*8:(i+1)*8] for i in range(NUM_PLAYERS)]
    scores = [0] * NUM_PLAYERS
    state = GameState(hands, scores, [], 0)

    move = choose_best_move(state, depth=2)
    print(f"AI selects card: {move}")
