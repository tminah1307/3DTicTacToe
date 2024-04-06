import unittest
from GameState import GameState
class TestGameState(unittest.TestCase):
    def test_initialisation_self(self):
        game_state = GameState()
        self.assertEqual(game_state.current_player, 'X')