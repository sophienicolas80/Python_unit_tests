class Calcul:
    def additionner(self, a, b):
        return a + b

    def soustraire(self, a, b):
        return a - b

    def multiplier(self, a, b):
        return a * b

        def diviser(self, a, b):
            if b == 0:
                raise ZeroDivisionError("Division par zéro impossible")
        return a / b