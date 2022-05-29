import unittest
from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Sandy", 30, "Part of Your World")

    def test_guest_has_name(self):
        self.assertEqual("Sandy", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(30, self.guest.wallet)

    def test_remove_cash(self):
        self.guest.remove_cash(5)
        self.assertEqual(25, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Part of Your World", self.guest.fave_song)
