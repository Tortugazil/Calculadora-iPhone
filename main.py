from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from logger import LogManagement

class MeuApp(QMainWindow):
    log = LogManagement(__file__)
    num1 = 0
    num2 = 0
    numResult = 0
    op = None

    def __init__(self):
        super().__init__()
        loadUi('calculadora.ui', self)
        self.log.info('Iniciando a interface')
        self.Botao_0.clicked.connect(lambda: self.btnClicado(self.Botao_0))
        self.Botao_1.clicked.connect(lambda: self.btnClicado(self.Botao_1))
        self.Botao_2.clicked.connect(lambda: self.btnClicado(self.Botao_2))
        self.Botao_3.clicked.connect(lambda: self.btnClicado(self.Botao_3))
        self.Botao_4.clicked.connect(lambda: self.btnClicado(self.Botao_4))
        self.Botao_5.clicked.connect(lambda: self.btnClicado(self.Botao_5))
        self.Botao_6.clicked.connect(lambda: self.btnClicado(self.Botao_6))
        self.Botao_7.clicked.connect(lambda: self.btnClicado(self.Botao_7))
        self.Botao_8.clicked.connect(lambda: self.btnClicado(self.Botao_8))
        self.Botao_9.clicked.connect(lambda: self.btnClicado(self.Botao_9))
        
        self.add.clicked.connect(lambda: self.definirOperacao(self.add))
        self.subtrair.clicked.connect(lambda: self.definirOperacao(self.subtrair))
        self.multi.clicked.connect(lambda: self.definirOperacao(self.multi))
        self.divisor.clicked.connect(lambda: self.definirOperacao(self.divisor))
        self.porcentagem.clicked.connect(lambda: self.porcentagem)
        self.valor.clicked.connect(self.mostraResultado)
        self.allClear.clicked.connect(self.limparDisplay)


    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.outputLabel.setText(value)

    def pegarDisplay(self):
        value = self.outputLabel.text()
        value = value.replace('.', '.')
        try:
            value = int(value)
        except:
            value = float(value)
        return value


    def btnClicado(self, btn):
        if self.pegarDisplay() == 0:
            self.mostrarDisplay(btn.text())
        else:
            ultimoValor = str(self.pegarDisplay())
            self.mostrarDisplay(ultimoValor + btn.text())

    def add(self):
        print(f'{self.num1} + {self.num2}')
        return self.num1 + self.num2
    
    def subtrair(self):
        print(f'{self.num1} - {self.num2}')
        return self.num1 - self.num2
    
    def multi(self):
        print(f'{self.num1} * {self.num2}')
        return self.num1 * self.num2
    
    def divisor(self):
        print(f'{self.num1} / {self.num2}')
        return self.num1 / self.num2
    
    def porcentagem(self):
        porcento = self.pegarDisplay() / 100
        if self.op == self.add or self.op == self.subtrair:
            porcento = self.num1 * porcento
        self.mostrarDisplay(porcento)
        
        
    
    def limparDisplay(self):
        self.num1 = 0
        self.num2 = 0
        self.numResult = 0
        self.op = None
        self.mostrarDisplay(0)

    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = int(self.pegarDisplay())
        self.num2 = 0
        self.mostrarDisplay(0)

    

    def resultado(self):
        if self.op:
            self.num2 = int(self.pegarDisplay())
            return self.op()
        else:
            print("não tem operação")

    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()
        if self.op:
            self.numResult = self.op
        else:
            self.mostrarDisplay(self.numResult)

        
if __name__ == '__main__':
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()