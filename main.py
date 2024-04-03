from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from logger import LogManagement
import operator
from functools import partial
 
class MeuApp(QMainWindow):
    num1 = 0
    num2 = 0
    numResult = 0
    op = None
    operacoes = {
        "+": operator.add, "-": operator.sub,
        "*": operator.mul, "/": operator.truediv,
    }
 
    def __init__(self):
        super().__init__()
        loadUi('calculadora.ui', self)
 
        for i in range(10):
            btn = getattr(self, f'btn{i}')
            btn.clicked.connect( partial(self.btnClicado, btn) )
 
        self.virgula.clicked.connect(lambda: self.btnClicado(self.virgula))
       
        self.add.clicked.connect(lambda: self.definirOperacao("+"))
        self.subtrair.clicked.connect(lambda: self.definirOperacao("-"))
        self.multi.clicked.connect(lambda: self.definirOperacao("*"))
        self.divisor.clicked.connect(lambda: self.definirOperacao('/'))
 
        self.allClear.clicked.connect(self.limparDisplay)
        self.combo.clicked.connect(self.inverter)
        self.porcentagem.clicked.connect(self.calcPorcentagem)
        self.outputLabel.clicked.connect(self.mostraResultado)
       
   
    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.outputLabel.setText( value )
 
 
    def pegarDisplay(self):
        value = self.outputLabel.text()
        value = value.replace(',', '.')
        try:value = int(value)
        except:value = float(value)
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
                if self.outputLabel.text()[-1] == ",":
                    ultimoValor = self.outputLabel.text()
        self.mostrarDisplay(ultimoValor + btn.text())
 
 
    def calcPorcentagem(self):
        percento = self.pegarDisplay() / 100
        if self.op == operator.add or self.op == operator.sub:
            percento = self.num1 * percento
        self.mostrarDisplay(percento)
 
 
    def inverter(self):
        numAtual = self.pegarDisplay()
        numAtual *= -1
        self.mostrarDisplay(numAtual)
 
 
    def definirOperacao(self, operacao):
        self.op = self.operacoes[operacao]
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)
 
 
    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op(self.num1, self.num2)
        else:
            print('nao tem operacao feita')
   
 
    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()
 
            self.numResult = self.op(self.num1, self.num2)
            self.mostrarDisplay(self.numResult)
            print(f"({self.num1}, {self.num2}): {self.numResult}")
       
 
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
 