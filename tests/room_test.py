import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Treble in Paradise", 5)
        self.room2 = Room("Songs of Pitch", 10)
        self.customer1 = Guest("Sandy", 30)
        self.customer2 = Guest("Chris", 40)
        self.customer3 = Guest("Simon", 20)

    def test_room_has_name(self):
        self.assertEqual("Treble in Paradise", self.room1.name)
        self.assertEqual("Songs of Pitch", self.room2.name)

    def test_cst_in_room_count(self):
        self.assertEqual(0, self.room1.cst_in_room_count())

    def test_guests_checks_in(self):
        self.room1.cst_checks_in(self.customer1, self.room1)
        self.room1.cst_checks_in(self.customer2, self.room1)
        self.assertEqual(2, self.room1.cst_in_room_count())

    def test_guests_checks_out(self):

        self.room2.cst_checks_in(self.customer1, self.room2)
        self.room2.cst_checks_in(self.customer2, self.room2)
        self.room2.cst_checks_in(self.customer3, self.room2)
        self.room2.cst_checks_out(self.customer1, self.room2)
        self.room2.cst_checks_out(self.customer2, self.room2)
        self.assertEqual(1, self.room2.cst_in_room_count())

    def test_room_plays_song(self):
        song = Song("Part of Your World")
        self.assertEqual(
            "Treble in Paradise is now playing 'Part of Your World'.",
            self.room1.play_song(song),
        )

    def test_add_song_request(self):
        song1 = Song("Let It Go")
        song2 = Song("Be My Guest")
        song3 = Song("I'll Make a Man Out of You")
        self.room1.add_song(song1)
        self.room1.add_song(song2)
        self.room2.add_song(song3)
        self.assertEqual(2, self.room1.song_count())
        self.assertEqual(1, self.room2.song_count())

    def test_room_has_fee(self):
        self.assertEqual(5, self.room1.entry_fee)
        self.assertEqual(10, self.room2.entry_fee)

    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)

    def test_cst_paid_entry_fee(self):
        self.room1.add_to_till(self.room1.entry_fee)
        self.customer1.remove_cash(self.room1.entry_fee)
        self.assertEqual(5, self.room1.till)
        self.assertEqual(25, self.customer1.wallet)
