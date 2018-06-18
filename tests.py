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

    def test_case_1(self):
        song = song_list[1]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)
        
    def test_case_3(self):
        song = song_list[3]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)

    def test_case_4(self):
        song = song_list[4]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)

    def test_case_5(self):
        song = song_list[5]['song']
        true_genre = song.genre
        run_all(rule_list=self.rules,
                defined_variables=SongVariables(song),
                defined_actions=SongActions(song),
                stop_on_first_trigger=False)

    def test_case_6_to_25(self):
        for i in range(6, 26):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)

    def test_case_26_to_50(self):
        for i in range(26, 50):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)


from pandas import DataFrame
from pandas_ml import ConfusionMatrix
import seaborn as sns
import matplotlib.pyplot as plt

class ModelAccuracyTest(unittest.TestCase):
    def setUp(self):
        self.rules = rules_json

    def test_accuracy(self):
        total = 50
        correct = 0
        df = DataFrame(index=range(0,50), columns=['true', 'predict'])
        for i in range(0,50):
            song = song_list[i]['song']
            true_genre = song.genre
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)
            df.loc[i] = [true_genre, song.genre]
            if true_genre == song.genre:
                correct += 1
        print(correct/total)
        cnf_matrix = ConfusionMatrix(df['true'], df['predict'])
        cnf_matrix.plot()
        plt.show()
        self.assertGreater((correct/total), 0.5)

    def confusion_matrix(self):
        df = DataFrame(index=range(0,50), columns=['true', 'predict'])
        for i in range(0, 50):
            song = song_list[i]['song']
            true_genre = str(song.genre)
            run_all(rule_list=self.rules,
                    defined_variables=SongVariables(song),
                    defined_actions=SongActions(song),
                    stop_on_first_trigger=False)
            df.loc[i] = [true_genre, song.genre]
        cnf_matrix = ConfusionMatrix(df['true'], df['predict'])
        cnf_matrix.plot()
        plt.show()
            

if __name__ == '__main__':
    accuracy_tests = unittest.TestLoader().loadTestsFromTestCase(ModelAccuracyTest)
    unittest.TextTestRunner(verbosity=1).run(accuracy_tests)
    song_tests = unittest.TestLoader().loadTestsFromTestCase(SongTests)
    unittest.TextTestRunner(verbosity=1).run(song_tests)