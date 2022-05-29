class Room:
    def __init__(self, name, entry_fee, max_capacity):
        self.name = name
        self.entry_fee = entry_fee
        self.till = 0
        self.max_capacity = max_capacity
        self.occupant = []
        self.playlist = ["We Don't Talk About Bruno", "Friend Like Me"]
        self.queue = []

    def cst_checks_in(self, customer, room):
        if len(self.occupant) < self.max_capacity:
            self.occupant.append(customer)
        else:
            self.queue.append(customer)
            return "Sorry, rooms are full. Please wait."

    def cst_checks_out(self, customer, room):
        self.occupant.remove(customer)

    def cst_in_room_count(self):
        return len(self.occupant)

    def play_song(self, song):
        room = self.name
        song = song.name
        return f"{room} is now playing '{song}'."

    def add_song(self, song):
        self.playlist.append(song)

    def song_count(self):
        return len(self.playlist)

    def add_to_till(self, amount):
        self.till += amount

    def play_fave_song(self, customer):
        for song in self.playlist:
            if song == customer.fave_song:
                return "Woohoo!"
        return False
