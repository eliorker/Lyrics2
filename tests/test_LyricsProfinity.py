import unittest
import unittest.mock as mock
import src.LyricsProfinity as lp

class MyTestCase(unittest.TestCase):

    def test_check_lyrics_for_profinity_true(self):
        self.assertTrue(lp.check_lyrics_for_profinity('gun profinity found'))


    def test_check_lyrics_for_profinity_false(self):
        self.assertFalse(lp.check_lyrics_for_profinity('no profinity here'))

    def test_does_song_contain_profinity_true(self):
        lp.get_song_artist_and_title = mock.MagicMock(return_value = ('Architects', 'Doomsday'))
        lp.get_lyrics = mock.Mock(return_value = "Lyrics with profanity gun")
        self.assertTrue(lp.does_song_contains_profinity())

    def test_does_song_contain_profinity_false(self):
        lp.get_song_artist_and_title = mock.MagicMock(return_value = ('Architects', 'Doomsday'))
        lp.get_lyrics = mock.Mock(return_value = "Lyrics with no profanity")
        self.assertFalse(lp.does_song_contains_profinity())

    def test_add_profinity_sword(self):
        lp.add_profinity('sword')
        self.assertIn('sword', lp.profinity)


if __name__ == "__main__":
    unittest.main()