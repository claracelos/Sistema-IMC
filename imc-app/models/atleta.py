from models.pessoa import Pessoa 

class Atleta(Pessoa):

    def classificar_imc(self):
        imc = self.calcular_imc()

        if imc < 20:
            return "atleta abaixo do ideal"

        elif imc <= 27:
            return "exelente condição física"

        return "avaliação específica para atleta recomendada"
        
