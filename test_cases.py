import numpy as np
from models import Song
from business_rules import run_all

song_list = [
    {
        'title': "I Can't Get No (Satisfaction)",
        'song': Song(
            ['sharp', 'hard', 'simple', 'repetitive', 'upbeat', 'steady'], ['vocals', 'lead guitar', 'rhythm guitar', 'drums', 'bass guitar'],
            5, ['angry'], ['angry', 'energetic', 'determined'],
            'rock')
    }, {
        'title': "Good Times Bad Times",
        'song': Song(
            ['hard', 'hurried', 'distorted'], ['vocals', 'lead guitar', 'bass guitar', 'drums'],
            4, ['determined', 'energetic'], ['determined', 'energetic'],
            'rock')
    }, {
        'title': "All Along the Watch Tower",
        'song': Song(
            ['rough', 'melodic', 'steady'], ['vocals', 'lead guitar', 'bass guitar', 'drums'],
            4, ['angry', 'determined', 'tense', 'depressed'], ['angry', 'determined', 'tense'],
            'rock')
    }, {
        'title': "Monkey Wrench",
        'song': Song(
            ['rough', 'hurried', 'grungy', 'distorted'], ['vocals', 'lead guitar', 'bass guitar', 'drums'],
            4, ['angry', 'depressed'], ['angry', 'energetic'],
            'rock')
    }, {
        'title': "Locomotive Breath",
        'song': Song(
            ['hard', 'steady', 'sharp'], ['vocals', 'piano', 'drums', 'bass guitar', 'lead guitar', 'rhythm guitar'],
            7, ['determined', 'depressed', 'hurt'], ['determined', 'tense'],
            'rock')
    }, {
        'title': "Lucille",
        'song': Song(
            ['sharp', 'steady', 'homey'], ['vocals', 'lead guitar', 'piano', 'bass guitar', 'saxophone', 'drums'],
            5, ['determined', 'depressed', 'lost'], ['determined', 'tense', 'lost'],
            'blues')
    }, {
        'title': "Hoochie Coochie Man",
        'song': Song(
            ['smooth', 'steady'], ['vocals', 'bass guitar', 'drums', 'lead guitar'],
            5, ['depressed', 'hurt'], ['depressed', 'hurt'],
            'blues')
    }, {
        'title': "Texas Flood",
        'song': Song(
            ['sharp', 'steady', 'twangy', 'rough', 'distorted', 'hard'], ['vocals', 'lead guitar', 'bass guitar', 'drums'],
            4, ['depressed', 'proud'], ['depressed', 'determined'],
            'blues')
    }, {
        'title': "Born Under A Bad Sign",
        'song': Song(
            ['steady', 'smooth', 'homey', 'grounded'], ['vocals', 'piano', 'bass guitar', 'drums', 'lead guitar', 'rhythm guitar', 'horns'],
            8, ['depressed', 'hurt'], ['depressed', 'hurt'],
            'blues')
    }, {
        'title': "Statesboro Blues",
        'song': Song(
            ['smooth', 'hard'], ['vocals', 'lead guitar', 'rhythm guitar', 'bass guitar', 'drums'],
            4, ['depressed', 'hurt', 'lost'], ['depressed', 'anxious', 'determined'],
            'blues')
    }, {
        'title': "Straight Outta Compton",
        'song': Song(
            ['edgy', 'rough', 'hard'], ['vocals', 'drums', 'horns', 'rhythm guitar'],
            4, ['angry', 'energetic'], ['angry', 'tense', 'energetic'],
            'rap')
    }, {
        'title': "Gold Digger",
        'song': Song(
            ['steady', 'bassheavy', 'hard'], ['vocals', 'drums', 'horns'],
            2, ['angry', 'determined'], ['angry', 'determined'],
            'rap')
    }, {
        'title': "Rap God",
        'song': Song(
            ['complex', 'hurried', 'upbeat', 'hard', 'chaotic'], ['vocals', 'drums', 'piano', 'synthesizer'],
            1, ['proud', 'determined'], ['angry', 'determined', 'tense', 'energetic'],
            'rap')
    }, {
        'title': "HUMBLE.",
        'song': Song(
            ['hard', 'repetitive', 'steady'], ['vocals', 'drums', 'piano', 'synthesizer'],
            1, ['proud', 'determined'], ['proud', 'determined'],
            'rap')
    }, {
        'title': "Hotline Bling",
        'song': Song(
            ['smooth', 'repetitive', 'hard'], ['vocals', 'drums', 'synthesizer'],
            1, ['hurt', 'depressed', 'lost'], ['hurt', 'determined'],
            'rap')
    }, {
        'title': "Firework",
        'song': Song(
            ['upbeat', 'peppy', 'melodic'], ['vocals', 'drums', 'synthesizer', 'bass guitar', 'violin'],
            1, ['amazed', 'energetic', 'happy'], ['amazed', 'energetic', 'happy'],
            'pop')
    }, {
        'title': "Toxic",
        'song': Song(
            ['upbeat', 'edgy'], ['vocals', 'drums', 'bass guitar', 'rhythm guitar', 'violin'],
            1, ['energetic', 'determined'], ['anxious', 'energetic'],
            'pop')
    }, {
        'title': "Billie Jean",
        'song': Song(
            ['smooth', 'repetitive', 'round'], ['vocals', 'drums', 'bass guitar', 'rhythm guitar', 'synthesizer', 'violin'],
            1, ['determined', 'energetic'], ['energetic', 'tense'],
            'pop')
    }, {
        'title': "Take On Me",
        'song': Song(
            ['upbeat', 'peppy', 'melodic'], ['vocals', 'drums', 'synthesizer', 'bass guitar', 'piano'],
            3, ['happy', 'energetic', 'loving'], ['happy', 'energetic'],
            'pop')
    }, {
        'title': "Marry You",
        'song': Song(
            ['simple', 'peppy', 'melodic', 'upbeat', 'repetitive'], ['vocals', 'drums', 'piano', 'rhythm guitar'],
            4, ['loving', 'happy', 'content'], ['happy', 'content', 'energetic'],
            'pop')
    }, {
        'title': "Wagon Wheel",
        'song': Song(
            ['leisurly', 'soft', 'homey', 'acoustical'], ['vocals', 'violin', 'rhythm guitar', 'bass guitar'],
            6, ['loving', 'content', 'proud'], ['loving', 'content', 'proud'],
            'country')
    }, {
        'title': "Amazed",
        'song': Song(
            ['soft', 'twangy', 'melodic', 'homey', 'smooth'], ['vocals', 'piano', 'drums', 'rhythm guitar', 'violin', 'bass guitar'],
            6, ['amazed', 'inspired', 'proud'], ['amazed', 'inspired', 'proud'],
            'country')
    }, {
        'title': "Wide Open Spaces",
        'song': Song(
            ['smooth', 'homey', 'melodic', 'leisurly'], ['vocals', 'rhythm guitar', 'lead guitar', 'bass guitar', 'drums', 'violin'],
            5, ['proud', 'content'], ['proud', 'content'],
            'country')
    }, {
        'title': "Jesus, Take the Wheel",
        'song': Song(
            ['patriotic', ''], ['vocals', 'violin', 'piano', 'drums', 'bass guitar', 'lead guitar'],
            6, ['amazed', 'inspired', 'proud'], ['inspired', 'proud'],
            'country')
    }, {
        'title': "I Walk the Line",
        'song': Song(
            ['smooth', 'acoustical', 'homey'], ['vocals', 'lead guitar', 'rhythm guitar', 'drums'],
            3, ['proud', 'content'], ['proud', 'content'],
            'country')
    }, {
        'title': "Three Little Birds",
        'song': Song(
            ['smooth', 'leisurly', 'slow'], ['vocals', 'drums', 'rhythm guitar', 'piano', 'bass guitar'],
            8, ['content', 'loving', 'peaceful'], ['content', 'loving', 'peaceful'],
            'reggae')
    }, {
        'title': "Bombastic",
        'song': Song(
            ['leisurly', 'slow', 'repetitive', 'grounded'], ['vocals', 'drums', 'piano', 'synthesizer', 'bass guitar'],
            3, ['content', 'determined'], ['content', 'annoyed'],
            'reggae')
    }, {
        'title': "Welcome to Jamrock",
        'song': Song(
            ['leisurly', 'steady', 'grounded'], ['vocals', 'drums', 'bass guitar', 'rhythm guitar'],
            5, ['content', 'peaceful', 'determined'], ['content', 'determined'],
            'reggae')
    }, {
        'title': "Red Red Wine",
        'song': Song(
            ['leisurly', 'slow', 'smooth'], ['vocals', 'drums', 'bass guitar', 'rhythm guitar'],
            5, ['content', 'loving', 'peaceful'], ['content', 'loving', 'peaceful'],
            'reggae')
    }, {
        'title': "Amber",
        'song': Song(
            ['leisurly', 'smooth', 'melodic', 'steady'], ['vocals', 'drums', 'bass guitar', 'rhythm guitar', 'lead guitar'],
            5, ['peaceful', 'content'], ['peaceful', 'content'],
            'reggae')
    }, {
        'title': "Levels",
        'song': Song(
            ['upbeat', 'peppy', 'bassheavy'], ['vocals', 'drums', 'synthesizer'],
            1, ['amazed', 'inspired', 'energetic', 'happy'], ['energetic', 'amazed', 'happy'],
            'electronic')
    }, {
        'title': "Harder Better Faster Stronger",
        'song': Song(
            ['upbeat', 'repetitive', 'peppy', 'steady'], ['vocals', 'synthesizer', 'drums'],
            2, ['determined', 'energetic'], ['determined', 'energetic'],
            'electronic')
    }, {
        'title': "Strobe",
        'song': Song(
            ['upbeat', 'repetitive', 'steady'], ['drums', 'synthesizer'],
            1, ['determined', 'energetic'], ['determined', 'energetic'],
            'electronic')
    }, {
        'title': "Scary Monsters And Nice Sprites",
        'song': Song(
            ['upbeat', 'hard', 'repetitive', 'bassheavy', 'chaotic'], ['vocals', 'drums', 'synthesizer'],
            1, ['determined', 'energetic'], ['determined', 'energetic', 'tense'],
            'electronic')
    }, {
        'title': "Xenogenesis",
        'song': Song(
            ['chaotic', 'hard', 'steady', 'bassheavy'], ['drums', 'synthesizer'],
            1, ['determined', 'energetic', 'proud'], ['determined', 'energetic', 'proud'],
            'electronic')
    }, {
        'title': "Flight of the Valkyries",
        'song': Song(
            ['complex', 'steady', 'melodic', 'edgy', 'chaotic'], ['piano', 'horns', 'violin', 'drums'],
            60, ['proud', 'amazed', 'inspired', 'determined'], ['inspired', 'determined', 'proud'],
            'classical')
    }, {
        'title': "Symphony No. 5",
        'song': Song(
            ['complex', 'melodic', 'hurried', 'sharp'], ['piano', 'horns', 'violin', 'drums'],
            60, ['anxious', 'tense', 'determined'], ['anxious', 'tense', 'determined'],
            'classical')
    }, {
        'title': "Fanfare For The Common Man",
        'song': Song(
            ['patriotic', 'melodic', 'steady', 'grounded'], ['piano', 'horns', 'violin', 'drums'],
            60, ['proud', 'amazed', 'inspired'], ['proud', 'amazed', 'inspired'],
            'classical')
    }, {
        'title': "The Four Seasons - Spring",
        'song': Song(
            ['soft', 'leisurly', 'complex', 'melodic', 'peppy'], ['violin', 'piano'],
            20, ['happy', 'peaceful', 'energetic'], ['happy', 'peaceful'],
            'classical')
    }, {
        'title': "Nocturne Op. 9 No. 2",
        'song': Song(
            ['steady', 'complex', 'slow', 'smooth'], ['piano'],
            1, ['peaceful', 'content'], ['peaceful', 'content'],
            'classical')
    }, {
        'title': "Cecilia",
        'song': Song(
            ['homey', 'simple', 'acoustical', 'grounded'], ['vocals', 'rhythm guitar', 'drums'],
            3, ['loving', 'happy'], ['loving', 'happy'],
            'folk')
    }, {
        'title': "This Land Is Your Land",
        'song': Song(
            ['patriotic', 'acoustical', 'homey', 'round'], ['vocals', 'rhythm guitar'],
            1, ['proud', 'content', 'peaceful'], ['proud', 'content', 'peaceful'],
            'folk')
    }, {
        'title': "If I Had A Hammer",
        'song': Song(
            ['patriotic', 'acoustical', 'homey', 'round', 'peppy'], ['vocals', 'rhythm guitar'],
            3, ['loving', 'happy', 'proud'], ['loving', 'happy'],
            'folk')
    }, {
        'title': "Blue Moon of Kentucky",
        'song': Song(
            ['patriotic', 'acoustical', 'homey', 'steady', 'melodic'], ['vocals', 'rhythm guitar', 'violin'],
            3, ['proud', 'peaceful', 'content'], ['proud', 'peaceful', 'content'],
            'folk')
    }, {
        'title': "The Last Thing On My Mind",
        'song': Song(
            ['soft', 'homey', 'grounded', 'smooth'], ['vocals', 'rhythm guitar'],
            1, ['proud', 'peaceful', 'content'], ['peaceful', 'content'],
            'folk')
    }, {
        'title': "The Girl From Ipanema",
        'song': Song(
            ['smooth', 'acoustical', 'melodic', 'simple', 'soft'], ['vocals', 'rhythm guitar', 'bass guitar', 'drums', 'saxophone', 'piano'],
            6, ['loving', 'hurt', 'lost', 'peaceful'], ['loving', 'hurt', 'peaceful'],
            'world')
    }, {
        'title': "El Cuarto De Tula",
        'song': Song(
            ['proud', 'steady', 'homey', 'acoustical'], ['vocals', 'drums', 'horns', 'bass guitar', 'rhythm guitar'],
            8, ['determined', 'energetic'], ['happy', 'energetic'],
            'world')
    }, {
        'title': "El Besu",
        'song': Song(
            ['patriotic', 'steady', 'grounded'], ['vocals', 'drums'],
            6, ['proud', 'inspired', 'happy'], ['proud', 'inspired', 'happy'],
            'world')
    }, {
        'title': "Rain, Rain, Beautiful Rain",
        'song': Song(
            ['smooth', 'soft', 'homey'], ['vocals'],
            10, ['amazed', 'content', 'peaceful'], ['amazed', 'peaceful', 'content'],
            'world')
    }, {
        'title': "Dhun",
        'song': Song(
            ['sharp', 'homey', 'chaotic'], ['drums'],
            3, ['peaceful', 'content'], ['peaceful', 'content'],
            'world')
    }
]