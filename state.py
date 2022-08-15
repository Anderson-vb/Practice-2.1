class State:

    def __init__(self, regex):
        self.regex = regex
        self.transition = []
        self.name = ''

    def set_regex(self, regex):
        self.regex = regex
    
    def set_transition(self, transition):
        self.transition.append(transition)

    def set_name(self, name):
        self.name = name

    def get_regex(self):
        return self.regex
    
    def get_transition(self):
        return self.transition

    def get_name(self):
        return self.name