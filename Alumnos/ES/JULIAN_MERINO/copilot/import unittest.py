import unittest
from unittest.mock import patch
from io import StringIO
from rock_paper_scissors import game

class GameTestCase(unittest.TestCase):
    @patch('random.choice')
    def test_game(self, mock_choice):
        mock_choice.side_effect = ['rock', 'paper', 'scissors', 'rock', 'scissors']
        expected_output = "rock: 2\npaper: 1\nscissors: 2\nlizard: 0\nspock: 0\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()