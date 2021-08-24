from sound.sound import play_sound


def test_play_sound():
    excepted = 'sound/music/sad/sad.wav'
    actual = play_sound('sad')
    assert excepted == actual
