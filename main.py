from ui import *

class Calculator(QMainWindow, Ui_MainWindow):
    
    result = ""
    operator = ""
    
    def __init__(self):
        super(Calculator, self).__init__()

        self.setupUi(self)

        # Button presses
        self.btn0.clicked.connect(self.zeroPressed)
        self.btn1.clicked.connect(self.onePressed)
        self.btn2.clicked.connect(self.twoPressed)
        self.btn3.clicked.connect(self.threePressed)
        self.btn4.clicked.connect(self.fourPressed)
        self.btn5.clicked.connect(self.fivePressed)
        self.btn6.clicked.connect(self.sixPressed)
        self.btn7.clicked.connect(self.sevenPressed)
        self.btn8.clicked.connect(self.eightPressed)
        self.btn9.clicked.connect(self.ninePressed)
        
        # clear Button
        self.btnClear.clicked.connect(self.clear)

        # Operators
        self.btnPlus.clicked.connect(self.plus)
        self.btnMinus.clicked.connect(self.minus)
        self.btnMultiply.clicked.connect(self.multiply)
        self.btnDivide.clicked.connect(self.divide)

        # Equal to
        self.btnEqual.clicked.connect(self.calculate)

        # File > Quit
        self.actionQuit.triggered.connect(self.close)


    def zeroPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}0")
        else:
            self.txtResult.setText("0")

    def onePressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}1")
        else:
            self.txtResult.setText("1")
    
    def twoPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}2")
        else:
            self.txtResult.setText("2")

    def threePressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}3")
        else:
            self.txtResult.setText("3")
    
    def fourPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}4")
        else:
            self.txtResult.setText("4")

    def fivePressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}5")
        else:
            self.txtResult.setText("5")

    def sixPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}6")
        else:
            self.txtResult.setText("6")

    def sevenPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}7")
        else:
            self.txtResult.setText("7")

    def eightPressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}8")
        else:
            self.txtResult.setText("8")

    def ninePressed(self):
        val = self.txtResult.text()
        if not val == "0":
            self.txtResult.setText(f"{val}9")
        else:
            self.txtResult.setText("9")

    def clear(self):
        self.txtResult.setText("0")

    def plus(self):
        self.operator = "+"
        self.result = self.txtResult.text()
        self.txtResult.setText("0")

    def minus(self):
        self.operator = "-"
        self.result = self.txtResult.text()
        self.txtResult.setText("0")

    def multiply(self):
        self.operator = "*"
        self.result = self.txtResult.text()
        self.txtResult.setText("0")

    def divide(self):
        self.operator = "/"
        self.result = self.txtResult.text()
        self.txtResult.setText("0")

    def calculate(self):
        if not (self.result == "0" or self.operator == ""):
            val1 = int(self.result)
            val2 = int(self.txtResult.text())

            if self.operator == "+":
             result = val1 + val2

            elif self.operator == "-":
             result = val1 - val2

            elif self.operator == "*":
             result = val1 * val2

            elif self.operator == "/":
             result = val1 / val2

            self.result = "0"
            self.txtResult.setText(str(result))

if __name__  == '__main__':
    import sys
    app = QApplication()

    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())