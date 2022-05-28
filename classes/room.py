class Room:
    def __init__(self, name):
        self.name = name
        self.customer = []
        self.song = []

    def cst_checks_in(self, customer, room):
        self.customer.append(customer)

    def cst_checks_out(self, customer, room):
        self.customer.remove(customer)

    def cst_in_room_count(self):
        return len(self.customer)

    def play_song(self, song):
        room = self.name
        song = song.name
        return f"Room {room} is now playing '{song}'."

    def add_song(self, song):
        self.song.append(song)

    def song_count(self):
        return len(self.song)
