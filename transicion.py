class Transicion:

    def __init__(self, caracter, estado):
        self.caracter = caracter
        self.estado = estado

    def get_caracter(self):
        return self.caracter

    def get_estado(self):
        return self.estado