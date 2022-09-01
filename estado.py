class Estado:

    def __init__(self, regex):
        self.regex = regex
        self.transiciones = []
        self.nombre = ''

    def set_regex(self, regex):
        self.regex = regex
    
    def set_transicion(self, transition):
        self.transiciones.append(transition)

    def set_nombre(self, name):
        self.nombre = name

    def get_regex(self):
        return self.regex
    
    def get_transicion(self):
        return self.transiciones

    def get_nombre(self):
        return self.nombre