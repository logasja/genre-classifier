import numpy as np
import unittest
from business_rules import run_all
from test_cases import song_list
from rules import rules_json
from models import SongVariables, SongActions


class SongTests(unittest.TestCase):
    def setUp(self):
        self.rules = rules_json

    def test_case_0(self):
        song = song_list[0]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
        self.assertEqual(true_genre, song.genre, 
                         song_list[0]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_1(self):
        song = song_list[1]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
        self.assertEqual(true_genre, song.genre, 
                         song_list[1]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_3(self):
        song = song_list[3]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
        self.assertEqual(true_genre, song.genre, 
                         song_list[3]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_4(self):
        song = song_list[4]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
        self.assertEqual(true_genre, song.genre, 
                         song_list[4]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_5(self):
        song = song_list[5]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
        self.assertEqual(true_genre, song.genre, 
                         song_list[5]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_6_to_25(self):
        for i in range(6, 26):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)
            self.assertEqual(true_genre, song.genre, 
                            song_list[i]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")

    def test_case_26_to_50(self):
        for i in range(26, 50):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)
            self.assertEqual(true_genre, song.genre, 
                            song_list[i]['title'] + " misclassified as " + song.genre + " (true: " + true_genre + ")\n")



class ModelAccuracyTest(unittest.TestCase):
    def setUp(self):
        self.rules = rules_json

    def test_accuracy(self):
        total = 50
        correct = 0
        for i in range(0,50):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)
            if true_genre == song.genre:
                correct += 1
        print(correct/total)
        self.assertGreater((correct/total), 0.5)

if __name__ == '__main__':
    song_tests = unittest.TestLoader().loadTestsFromTestCase(SongTests)
    unittest.TextTestRunner(verbosity=1).run(song_tests)
    accuracy_tests = unittest.TestLoader().loadTestsFromTestCase(ModelAccuracyTest)
    unittest.TextTestRunner(verbosity=1).run(accuracy_tests)