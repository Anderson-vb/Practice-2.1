class Transition:

    def __init__(self, character, state):
        self.character = character
        self.state = state

    def get_character(self):
        return self.character

    def get_state(self):
        return self.state