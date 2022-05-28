class Room:
    def __init__(self, name, entry_fee, max_capacity):
        self.name = name
        self.entry_fee = entry_fee
        self.till = 0
        self.max_capacity = max_capacity
        self.customer = []
        self.song = []
        self.queue = []

    def cst_checks_in(self, customer, room):
        if len(self.customer) < self.max_capacity:
            self.customer.append(customer)
        else:
            self.queue.append(customer)

    def cst_checks_out(self, customer, room):
        self.customer.remove(customer)

    def cst_in_room_count(self):
        return len(self.customer)

    def play_song(self, song):
        room = self.name
        song = song.name
        return f"{room} is now playing '{song}'."

    def add_song(self, song):
        self.song.append(song)

    def song_count(self):
        return len(self.song)

    def add_to_till(self, amount):
        self.till += amount
