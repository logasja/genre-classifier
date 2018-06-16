import numpy as np
import unittest
from models import Song
from business_rules import run_all


run_all(rule_list=self.rules,
            defined_variables=SongVariables(self.song),
            defined_actions=SongActions(self.song),
            stop_on_first_trigger=False
            )

class SongTests(unittest.TestCase):
   def setUp(self):
        self.widget = Widget('The widget')

   def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')


if __name__ == '__main__':
    song_tests = unittest.TestLoader().loadTestsFromTestCase(SongTests)
    unittest.TextTestRunner(verbosity=1).run(song_tests)