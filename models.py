import datetime
from business_rules.variables import *
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import *

descriptors = ['sharp', 'smooth', 'rough', 'round', 'chaotic', 
                'patriotic', 'steady', 'hard', 'soft', 'simple',
                'complex', 'hurried', 'leisurly', 'slow',
                'edgy', 'grounded', 'grungy', 'upbeat', 'acoustical',
                'homey', 'peppy', 'melodic', 'twangy', 'repetitive', 'bassheavy']

emotions = ['amazed', 'angry', 'annoyed', 'anxious', 'bored', 'confused', 'content', 'depressed', 'determined',
            'energetic', 'happy', 'hurt', 'inspired', 'lost', 'loving', 'peaceful', 'proud', 'tense']

instruments = ['piano', 'lead guitar', 'bass guitar', 'rhythm guitar', 'saxophone',
               'drums', 'sythesizer', 'vocals', 'steel guitar', 'horns', 'violin']

genres = ['rock', 'blues', 'country', 'reggae', 'rap', 'electronic', 'world', 'classical', 'folk', 'pop']

class SongVariables(BaseVariables):

    def __init__(self, song):
        self.song = song

    # Input information
    @select_multiple_rule_variable(options=descriptors, label='Descriptors')
    def descriptor(self):
        return self.song['descriptors']

    @select_multiple_rule_variable(options=emotions, label='Emotions')
    def emotion(self):
        return self.song['emotions']

    @select_multiple_rule_variable(options=instruments, label='Instruments')
    def instruments(self):
        return self.song['instruments']

    @boolean_rule_variable(label='Distortion')
    def distorted(self):
        return self.song['distortion']

    @numeric_rule_variable(label='Number of Performers')
    def performer_count(self):
        return self.song['performers']

    @numeric_rule_variable(label='Age')
    def age(self):
        return self.song['age']

    @select_multiple_rule_variable(options=emotions, label='Percieved Emotion')
    def perc_emot(self):
        return self.song['perc_emot']

    @select_multiple_rule_variable(options=emotions, label='Felt Emotion')
    def felt_emot(self):
        return self.song['felt_emot']

    # Calculated features
    

class SongActions(BaseActions):

    def __init__(self, product):
        self.song = song

    # Intermediate actions

    # Final action, setting rule
    @rule_action(params=[{'fieldType'   : FIELD_SELECT,
                          'name'        : 'genre',
                          'label'       : 'Genre',
                          'options': [
                              {'label': 'Rock', 'name': 'rock'},
                              {'label': 'Blues', 'name': 'blues'},
                              {'label': 'Country', 'name': 'country'},
                              {'label': 'Reggae', 'name': 'reggae'},
                              {'label': 'Rap', 'name': 'rap'},
                              {'label': 'Electronic', 'name': 'electronic'},
                              {'label': 'World', 'name': 'world'},
                              {'label': 'Classical', 'name': 'classical'},
                              {'label': 'Folk', 'name': 'folk'},
                              {'label': 'Pop', 'name': 'pop'}
                          ]}])
    def assign_genre(self, genre):
        self.song['genre'] = genre
