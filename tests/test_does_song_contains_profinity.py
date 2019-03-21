import unittest
from src.LyricsProfinity import check_lyrics_for_profinity
import mock


class MyTestCase(unittest.TestCase):

    @mock.patch('get_lyrics', return_value='gun OH NOES A PROFINITY')
    def test_check_lyrics_for_profinity(self, get_lyrics):
        self.assertTrue(check_lyrics_for_profinity('no prof'))


if __name__ == '__main__':
    unittest.main()
