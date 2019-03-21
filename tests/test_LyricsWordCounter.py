import unittest
import unittest.mock as mock
import src.LyricsWordCounter as lwc

class MyTestCase(unittest.TestCase):


    def test_check_numbers_of_repeats_0(self):
        lwc.get_word = mock.MagicMock(return_value = "abc")
        self.assert_(lwc.check_numbers_of_repeats('no repeats at all') == 0)


    def test_check_numbers_of_repeats_3(self):
        lwc.get_word = mock.MagicMock(return_value = "abc")
        self.assert_(lwc.check_numbers_of_repeats('3 repeats abc abc abc') == 3)


    def test_calculate_number_of_times_word_occurs_in_the_song_0(self):
        lwc.get_song_artist_and_title = mock.MagicMock(return_value = ('Architects', 'Doomsday'))
        lwc.get_word = mock.MagicMock(return_value = "ban")
        lwc.get_lyrics = mock.Mock(return_value = 'no repeats at all')
        self.assert_(lwc.calculate_number_of_times_word_occurs_in_the_song() == 0)

    def test_calculate_number_of_times_word_occurs_in_the_song_4(self):
        lwc.get_song_artist_and_title = mock.MagicMock(return_value = ('Architects', 'Doomsday'))
        lwc.get_word = mock.MagicMock(return_value = "ban")
        lwc.get_lyrics = mock.Mock(return_value = '4 repeats ban ban ban ban')
        self.assert_(lwc.calculate_number_of_times_word_occurs_in_the_song() == 4)

    def test_calculate_number_of_times_word_occurs_in_the_song_22(self):
        lwc.get_song_artist_and_title = mock.MagicMock(return_value = ('Architects', 'Doomsday'))
        lwc.get_word = mock.MagicMock(return_value = "mass")
        lwc.get_lyrics = mock.Mock(return_value = '22 repeats mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass mass ')
        self.assert_(lwc.calculate_number_of_times_word_occurs_in_the_song() == 22)


if __name__ == "__main__":
    unittest.main()