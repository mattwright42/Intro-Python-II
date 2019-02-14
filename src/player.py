# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, current_room, items=[]):
        self.player_name = player_name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"Greetings {self.player_name}!\n"

    def move(self, direction):
        if direction == 'n':
            self.current_room = self.current_room.n_to
        if direction == 's':
            self.current_room = self.current_room.s_to
        if direction == 'e':
            self.current_room = self.current_room.e_to
        if direction == 'w':
            self.current_room = self.current_room.w_to

    def pickup(self, action):
        if action in self.current_room.items:
            self.items.append(action)
            self.current_room.items.remove(action)

    def drop(self, action):
        if action in self.items:
            self.items.remove(action)
            self.current_room.items.append(action)
