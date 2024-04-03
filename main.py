from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from os import path
 
class MeuApp(QMainWindow):
    num1 = 0
    num2 = 0
    numResult = 0
    op = None
 
    def __init__(self):
        super().__init__()
        loadUi( self.localPath('calculadora.ui'), self)
        self.setAcoes()
 
    def localPath(self, relativo):
        return f'{path.dirname(path.realpath(__file__))}\\{relativo}'
 
    def setAcoes(self):
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
        self.Virgula.clicked.connect(lambda: self.btnClicado(self.Virgula))
       
        self.Add.clicked.connect(lambda: self.definirOperacao(self.adicao))
        self.Subtrair.clicked.connect(lambda: self.definirOperacao(self.subtracao))
        self.Multi.clicked.connect(lambda: self.definirOperacao(self.multiplicacao))
        self.Divisor.clicked.connect(lambda: self.definirOperacao(self.divisao))
 
        self.Porcentagem.clicked.connect(self.porcentagem)
        self.Combo.clicked.connect(self.inverter)
 
        self.Valor.clicked.connect(self.mostraResultado)
        self.AllClear.clicked.connect(self.limparDisplay)
       
   
    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.OutputLabel.setText( value )
 
 
    def pegarDisplay(self):
        value = self.OutputLabel.text()
        value = value.replace(',', '.')
        try:
            value = int(value)
        except:
            value = float(value)
        return value
 
 
    def btnClicado(self, btn):
        ultimoValor = str( self.pegarDisplay() )
        #Digitando virgula
        if btn.text() == ',':
            if isinstance(self.pegarDisplay(), float):
                return
        #Digitando numeros
        else:
            # Se for numero inteiros
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    ultimoValor = ''
            # Se for numero float
            else:
                if self.Valor.text()[-1] == ",":
                    ultimoValor = self.Valor.text()
        self.mostrarDisplay(ultimoValor + btn.text())
 
 
    def adicao(self):
        print(f'Soma({self.num1}+{self.num2}) = ', end='')
        return self.num1 + self.num2
 
 
    def subtracao(self):
        print(f'Sub({self.num1} - {self.num2})= ', end='')
        return self.num1 - self.num2
 
 
    def multiplicacao(self):
        print(f'Mult({self.num1} * {self.num2})= ', end='')
        return self.num1 * self.num2
 
 
    def divisao(self):
        print(f'Div({self.num1} / {self.num2})= ', end='')
        return self.num1 / self.num2
   
 
    def porcentagem(self):
        percento = self.pegarDisplay() / 100
        if self.op == self.adicao or self.op == self.subtracao:
            percento = self.num1 * percento
        self.mostrarDisplay(percento)
 
 
    def inverter(self):
        numAtual = self.pegarDisplay()
        numAtual *= -1
        self.mostrarDisplay(numAtual)
 
 
    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)
 
 
    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()
        else:
            print('nao tem operacao feita')
   
 
    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()
 
            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)
            print(self.numResult)
       
 
    def limparDisplay(self):
        self.num1 = 0
        self.num2 = 0
        self.numResult = 0
        self.op = None
        self.mostrarDisplay(0)
 
if __name__ == '__main__':
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()
 