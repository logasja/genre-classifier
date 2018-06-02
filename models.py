import datetime
from business_rules.variables import *
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import *

descriptors = ['sharp', 'smooth', 'rough', 'round', 'chaotic', 
                'patriotic', 'steady', 'hard', 'soft', 'simple',
                'complex', 'hurried', 'leisurly', 'slow', 'anarchist',
                'edgy', 'grounded', 'natural', 'grungy', 'upbeat', 'acoustical',
                'homey', 'peppy', 'melodic', 'twangy', 'repetitive', 'bassheavy']

emotions = ['amazed', 'angry', 'annoyed', 'anxious', 'ashamed', 'bitter',
            'bored', 'comfortable', 'confused', 'content', 'depressed', 'determined',
            'disdain', 'disgusted', 'eager', 'embarrassed', 'energetic', 'envious',
            'excited', 'foolish', 'frustrated', 'furious', 'grieving', 'happy', 'hopeful',
            'hurt', 'inadequate', 'insecure', 'inspired', 'irritated', 'jealous', 'joy', 'lonely',
            'lost', 'loving', 'miserable', 'motivated', 'nervous', 'overwhelmed', 'peaceful', 'proud',
            'relieved', 'resentful', 'sad', 'satisfied', 'scared', 'self-conscious', 'shocked', 'silly',
            'stupid', 'suspicious', 'tense', 'terrified', 'trapped', 'uncomfortable', 'worried', 'worthless']

instruments = ['piano', 'lead guitar', 'bass', 'melody guitar', 'saxophone',
               'drums', 'sythesizer', 'vocals', 'steel guitar', 'fiddle']

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

    # Calculated features

    @select_rule_variable(options=['slow', 'medium', 'fast'], label='Approximate Tempo')
    def tempo(self):
        return self.song['tempo']

    @boolean_rule_variable(label='Energetic')
    def energetic(self):
        return self.song['energetic']

    

class SongActions(BaseActions):

    def __init__(self, product):
        self.song = song

    # Intermediate actions
    @rule_action(params=[{'fieldType': FIELD_SELECT,
                         'name' : 'tempo',
                         'label': 'Approximate Tempo',
                         'options': [
                             {'label': 'Slow', 'name': 'slow'},
                             {'label': 'Medium', 'name': 'medium'},
                             {'label': 'Fast', 'name': 'fast'}
                         ]}])
    def assign_tempo(self, tempo):
        self.song['tempo'] = tempo

    @rule_action(params={"energetic": FIELD_NUMERIC})
    def assign_energetic(self, energetic):
        self.song['energetic'] = bool(energetic)

    # Final action, setting rule
    @rule_action(params=[{'fieldType'   : FIELD_SELECT,
                          'name'        : 'genre',
                          'label'       : 'Approximate Tempo',
                          'options': [
                              {'label': 'Rock', 'name': 'rock'},
                              {'label': 'Blues', 'name': 'blues'},
                              {'label': 'Country', 'name': 'country'},
                              {'label': 'Reggae', 'name': 'reggae'},
                              {'label': 'Rap', 'name': 'rap'},
                              {'label': 'Electronic', 'name': 'electronic'},
                              {'label': 'World', 'name': 'world'},
                              {'label': 'Classical', 'name': 'classical'},
                              {'label': 'Folk', 'name': 'folk'}
                          ]}])
    def assign_genre(self, genre):
        self.song['genre'] = genre
