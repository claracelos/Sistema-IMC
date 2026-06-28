class Pessoa:
    def __inicio__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura
    
    def calcular_imc(self): 
        return self.peso / (self.altura ** 2) 
    
    def classificar_imc(self):
        imc = self.calcular_imc() 

        if imc < 18.5:
            return "abaixo do peso"
        elif imc < 25:
            return "peso normal"
        elif imc < 30:
            return "sobrepeso"
        elif imc < 35:
            return "obesidade grau 1"
        elif imc < 40:
            return "obesidade grau 2"
        else:
            return "obesidade grau 3"
        
