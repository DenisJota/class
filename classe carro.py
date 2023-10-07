class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def exibirInformacoes(self):
        print(f'------- DADOS DO VEÍCULO ----------\n'
              f'Marca: {self.marca}\n'
              f'Modelo: {self.modelo}\n'
              f'Cor: {self.cor}')


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, portas):
        super().__init__(marca, modelo, cor)
        self.portas = portas

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Numero de portas: {self.portas}\n')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, cilindrada):
        super().__init__(marca, modelo, cor)
        self.cilindrada = cilindrada

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Cilindradas: {self.cilindrada}')

carro1 = Carro('VW', 'Gol', 'Prata', 4)
carro1.exibirInformacoes()

moto1 = Moto('Honda', 'Titan', 'Vermelha', 160)
moto1.exibirInformacoes()
