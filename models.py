import datetime
from business_rules.variables import *
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import *

descriptors = ['sharp', 'smooth', 'rough', 'round', 'chaotic', 'simple', 'energetic',
                'patriotic', 'steady', 'hard', 'soft', 'simple', 'honest',
                'complex', 'hurried', 'leisurly', 'slow', 'distorted',
                'edgy', 'grounded', 'grungy', 'upbeat', 'acoustical',
                'homey', 'peppy', 'melodic', 'twangy', 'repetitive', 'bassheavy',
                'awsome', 'epic', 'flowing', 'surprising', 'full', 'beautiful', 'ambient',
                'catchy', 'multilingual', 'deep', 'sophisticated', 'complex', 'fun', 'fulfilling']

emotions = ['amazed', 'angry', 'annoyed', 'anxious', 'bored', 'confused', 'content', 'depressed', 'determined',
            'energetic', 'happy', 'hurt', 'inspired', 'lost', 'loving', 'peaceful', 'proud', 'tense']

instruments = ['piano', 'lead guitar', 'bass guitar', 'rhythm guitar', 'saxophone',
               'drums', 'synthesizer', 'vocals', 'steel guitar', 'horns', 'violin']

genres = ['rock', 'blues', 'country', 'reggae', 'rap', 'electronic', 'world', 'classical', 'folk', 'pop']

class Song():
    def __init__(self, descriptors=[], instruments=[], performers=0, perc_emot=[], felt_emot=[], genre=None):
        self.descriptors    = descriptors
        self.instruments    = instruments
        self.performers     = performers
        self.perc_emot      = perc_emot
        self.felt_emot      = felt_emot
        self.genre          = genre

class SongVariables(BaseVariables):

    def __init__(self, song):
        self.song = song

    # Input information
    @select_multiple_rule_variable(options=descriptors, label='Descriptors')
    def descriptor(self):
        return self.song.descriptors

    @select_multiple_rule_variable(options=instruments, label='Instruments')
    def instruments(self):
        return self.song.instruments

    @numeric_rule_variable(label='Number of Performers')
    def performer_count(self):
        return self.song.performers

    @select_multiple_rule_variable(options=emotions, label='Percieved Emotion')
    def perc_emot(self):
        return self.song.perc_emot

    @select_multiple_rule_variable(options=emotions, label='Felt Emotion')
    def felt_emot(self):
        return self.song.felt_emot

    # Calculated features
    

class SongActions(BaseActions):

    def __init__(self, song):
        self.song = song

    # Intermediate actions
 
    @rule_action(params=[{'fieldType'  : FIELD_SELECT_MULTIPLE,
                          'name'       : 'emotion',
                          'label'      : 'Emotion',
                          'options': [
                              {'label': 'Amazed', 'name': 'amazed'},
                              {'label': 'Angry', 'name': 'angry'},
                              {'label': 'Annoyed', 'name': 'annoyed'},
                              {'label': 'Anxious', 'name': 'anxious'},
                              {'label': 'Bored', 'name': 'bored'},
                              {'label': 'Confused', 'name': 'confused'},
                              {'label': 'Content', 'name': 'content'},
                              {'label': 'Depressed', 'name': 'depressed'},
                              {'label': 'Determined', 'name': 'determined'},
                              {'label': 'Energetic', 'name': 'energetic'},
                              {'label': 'Happy', 'name': 'happy'},
                              {'label': 'Hurt', 'name': 'hurt'},
                              {'label': 'Inspired', 'name': 'inspired'},
                              {'label': 'Lost', 'name': 'lost'},
                              {'label': 'Loving', 'name': 'loving'},
                              {'label': 'Peaceful', 'name': 'peaceful'},
                              {'label': 'Proud', 'name': 'proud'},
                              {'label': 'Tense', 'name': 'tense'}
                          ]}])
    def add_emotion(self, emotion):
        self.song.felt_emot = emotion

    @rule_action(params={"dummy": FIELD_TEXT})
    def dummy(self, dummy):
        return

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
    # @rule_action(params={"genre": FIELD_TEXT})
    def assign_genre(self, genre):
        self.song.genre = genre
