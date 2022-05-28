import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Part of Your World")

    def test_song_has_name(self):
        self.assertEqual("Part of Your World", self.song.name)
