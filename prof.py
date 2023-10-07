class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibirInformacoes(self):
        print(f'----- DADOS DE FUNCIONÁRIOS ------\n\n'
              f'Matricula:{self.matricula} \n'
              f'Nome:{self.nome} \n'
              f'Salário:{self.salario} ')

class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        super().__init__(matricula, nome, salario)
        self.turma = turma

    def exibirInformaçoes(self):
        super().exibirInformacoes()
        print(f'Turma: {self.turma}\n ')

class Monitor(Funcionario):
    def __init__(self, matricula, nome, salario, cargaHoraria):
        super().__init__(matricula, nome, salario)
        self.cargaHoraria = cargaHoraria

    def exibirInformaçoes(self):
        super().exibirInformacoes()
        print(f'Carga Horaria: {self.cargaHoraria}\n')

class Coordenador(Funcionario):
    def __init__(self, matricula, nome, salario, area):
        super().__init__(matricula, nome, salario)
        self.area = area

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Área de atuação: {self.area}\n ')

p1 = Professor(1, 'Luana', 3500, 'Python123')
p1.exibirInformaçoes()
m1 = Monitor(3, 'Antonio', 700, 20)
m1.exibirInformaçoes()
c1 = Coordenador(2, 'Marcos', 5000, 'Programação')
c1.exibirInformaçoes()