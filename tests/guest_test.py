import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Sandy", 30)

    def test_guest_has_name(self):
        self.assertEqual("Sandy", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(30, self.guest.age)
