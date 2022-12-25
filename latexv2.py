import keyboard as k
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import json
import ctypes
import numpy as np
import time
myappid = 'latenexadentro2'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#region startup
class startup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setGeometry(800,400,321,420)
        self.label = QLabel(self)
        self.pixmap = QPixmap('logotipo.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        text = self.label2 = QLabel(self, alignment=Qt.AlignCenter)
        text.setText("Hola, Para iniciar el programa apreta ""Alt+p"" y para revisar los \n comandos escribí en cualquier lado "".opciones""!\n Cerrame apretando enter.")
        text.move(20,330)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Bienvenido!")
        self.show()
        self.raise_()
        self.activateWindow()

#endregion

#region opciones
class Opciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon('logotipo.png'))

        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        grid = QGridLayout()
#region opsum
        sumatoria = QLineEdit('Sumatoria')
        sumatorian = QLineEdit(funcs['funcs'][0]['sumatoria'][0]['sumatorian'])
        sumatorias = QLineEdit(funcs['funcs'][0]['sumatoria'][0]['sumatorias'])
        grid.addWidget(sumatoria, 0, 0)
        grid.addWidget(sumatorian, 0, 1)
        grid.addWidget(sumatorias, 0, 2)
        sumatoria.setReadOnly(True)
        sumatorian.textChanged.connect(self.editsn)
        sumatorias.textChanged.connect(self.editss)
#endregion
#region opmult
        multiplicatoria = QLineEdit('Multiplicatoria')
        multiplicatorian = QLineEdit(funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorian'])
        multiplicatorias = QLineEdit(funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorias'])
        grid.addWidget(multiplicatoria, 3, 0)
        grid.addWidget(multiplicatorian, 3, 1)
        grid.addWidget(multiplicatorias, 3, 2)
        multiplicatoria.setReadOnly(True)
        multiplicatorian.textChanged.connect(self.editmn)
        multiplicatorias.textChanged.connect(self.editms)
#endregion
#region opint
        integral = QLineEdit('Integral')
        integraln = QLineEdit(funcs['funcs'][0]['integral'][0]['integraln'])
        integrals = QLineEdit(funcs['funcs'][0]['integral'][0]['integrals'])
        grid.addWidget(integral, 1, 0)
        grid.addWidget(integraln, 1, 1)
        grid.addWidget(integrals, 1, 2)
        integral.setReadOnly(True)
        integraln.textChanged.connect(self.editin)
        integrals.textChanged.connect(self.editis)
#endregion
#region opfrac
        fraccion = QLineEdit('Fraccion')
        fraccionn = QLineEdit(funcs['funcs'][0]['fraccion'][0]['fraccionn'])
        fraccions = QLineEdit(funcs['funcs'][0]['fraccion'][0]['fraccions'])
        grid.addWidget(fraccion, 2, 0)
        grid.addWidget(fraccionn, 2, 1)
        grid.addWidget(fraccions, 2, 2)
        fraccion.setReadOnly(True)
        fraccionn.textChanged.connect(self.editfn)
        fraccions.textChanged.connect(self.editfs)
#endregion
#region opmatrx
        matrix = QLineEdit('Matrix')
        matrixn = QLineEdit(funcs['funcs'][0]['matrix'][0]['matrixn'])
        matrixs = QLineEdit(funcs['funcs'][0]['matrix'][0]['matrixs'])
        grid.addWidget(matrix, 4, 0)
        grid.addWidget(matrixn, 4, 1)
        grid.addWidget(matrixs, 4, 2)
        matrix.setReadOnly(True)
        matrixn.textChanged.connect(self.editmtn)
        matrixs.textChanged.connect(self.editmts)
#endregion
#region opder
        derivada = QLineEdit('Derivada')
        derivadan = QLineEdit(funcs['funcs'][0]['derivada'][0]['derivadan'])
        derivadas = QLineEdit(funcs['funcs'][0]['derivada'][0]['derivadas'])
        grid.addWidget(derivada, 6, 0)
        grid.addWidget(derivadan, 6, 1)
        grid.addWidget(derivadas, 6, 2)
        derivada.setReadOnly(True)
        derivadan.textChanged.connect(self.editdn)
        derivadas.textChanged.connect(self.editds)
#endregion
#region oplim
        limite = QLineEdit('Limite')
        limiten = QLineEdit(funcs['funcs'][0]['limite'][0]['limiten'])
        limites = QLineEdit(funcs['funcs'][0]['limite'][0]['limites'])
        grid.addWidget(limite, 5, 0)
        grid.addWidget(limiten, 5, 1)
        grid.addWidget(limites, 5, 2)
        limite.setReadOnly(True)
        limiten.textChanged.connect(self.editln)
        limites.textChanged.connect(self.editls)
#endregion
#region opimg
        imagen = QLineEdit('Imagen')
        imagenn = QLineEdit(funcs['funcs'][0]['imagen'][0]['imagenn'])
        imagens = QLineEdit(funcs['funcs'][0]['imagen'][0]['imagens'])
        grid.addWidget(imagen, 6, 0)
        grid.addWidget(imagenn, 6, 1)
        grid.addWidget(imagens, 6, 2)
        imagen.setReadOnly(True)
        imagenn.textChanged.connect(self.editimgn)
        imagens.textChanged.connect(self.editimgs)
#endregion
        self.setLayout(grid)
        self.setGeometry(800, 400, 200, 200)
        self.setWindowTitle('Opciones')
        self.show()
        self.raise_()
        self.activateWindow()
        self.shortcut_close = QShortcut(QKeySequence('Escape'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
#region opsums
    def editsn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['sumatoria'][0]['sumatorian'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editss(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['sumatoria'][0]['sumatorias'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opmtx
    def editmtn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['matrix'][0]['matrixn'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editmts(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['matrix'][0]['matrixs'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opmults
    def editmn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorian'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editms(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorias'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opint
    def editin(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['integral'][0]['integraln'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editis(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['integral'][0]['integrals'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opfrac
    def editfn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['fraccion'][0]['fraccionn'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editfs(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['fraccion'][0]['fraccions'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region oplim
    def editln(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['limite'][0]['limiten'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editls(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['limite'][0]['limites'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opder
    def editdn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['derivada'][0]['derivadan'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editds(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['derivada'][0]['derivadas'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
#region opimg
    def editimgn(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['imagen'][0]['imagenn'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
    def editimgs(self,text):
        f = open('funcs.json',)
        funcs = json.load(f)
        f.close()
        f = open('funcs.json','w')
        funcs['funcs'][0]['imagen'][0]['imagens'] = text
        json.dump(funcs,f)
        f.close()
        keylogs()
#endregion
    q=2
#endregion

#region matematicas

#region arafue
def listensettings():
    for i in 'opciones.':
        k.send('backspace')
    App = QApplication(sys.argv)
    opciones = Opciones()
    opciones.show()
    App.exec()
#endregion

#region sumatoria
class WindowS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,200)
        self.label = QLabel(self)
        self.pixmap = QPixmap('sigma2.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        top = QtWidgets.QLineEdit(self)
        top.textChanged.connect(self.handleInputtop)
        top.setText('\infty')
        top.move(80,10)
        top.setFixedWidth(40)
        bl = QtWidgets.QLineEdit(self)
        bl.textChanged.connect(self.handleInputbl)
        bl.setText('n')
        bl.move(10,170)
        bl.setFixedWidth(40)
        br = QtWidgets.QLineEdit(self)
        br.textChanged.connect(self.handleInputbr)
        br.setText('1')
        br.move(150,170)
        br.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputtop(self,text):
        global topl
        topl = text
    def handleInputbl(self,text):
        global bll
        bll = text
    def handleInputbr(self,text):
        global brl
        brl = text
def listens():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('sumatoria')>len(funcs['funcs'][0]['sumatoria'][0]['sumatorian']):
        for i in (str(funcs['funcs'][0]['sumatoria'][0]['sumatorian'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['sumatoria'][0]['sumatorian']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowS()
    window.show()
    app.exec()
    k.write('\\displaystyle \\sum_{'+bll+'='+brl+'}^{'+topl+'}')
def listenshts():
    app = QApplication(sys.argv)
    window = WindowS()
    window.show()
    app.exec()
    k.write('\\displaystyle \\sum_{'+bll+'='+brl+'}^{'+topl+'}')
#endregion

#region multiplicatoria
class WindowM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,200)
        self.label = QLabel(self)
        self.pixmap = QPixmap('bigpi.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        top = QtWidgets.QLineEdit(self)
        top.textChanged.connect(self.handleInputtop)
        top.setText('\infty')
        top.move(80,10)
        top.setFixedWidth(40)
        bl = QtWidgets.QLineEdit(self)
        bl.textChanged.connect(self.handleInputbl)
        bl.setText('n')
        bl.move(10,170)
        bl.setFixedWidth(40)
        br = QtWidgets.QLineEdit(self)
        br.textChanged.connect(self.handleInputbr)
        br.setText('1')
        br.move(150,170)
        br.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputtop(self,text):
        global topl
        topl = text
    def handleInputbl(self,text):
        global bll
        bll = text
    def handleInputbr(self,text):
        global brl
        brl = text
def listenm():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('multiplicatoria')>len(funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorian']):
        for i in (str(funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorian'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['multiplicatoria'][0]['multiplicatorian']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowM()
    window.show()
    app.exec()
    k.write('\\displaystyle \\prod_{'+bll+'='+brl+'}^{'+topl+'}')
def listenshtm():
    app = QApplication(sys.argv)
    window = WindowM()
    window.show()
    app.exec()
    k.write('\\displaystyle \\prod_{'+bll+'='+brl+'}^{'+topl+'}')
#endregion

#region integral
class WindowI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,200)
        self.label = QLabel(self)
        self.pixmap = QPixmap('integral1.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        top = QtWidgets.QLineEdit(self)
        top.textChanged.connect(self.handleInputtop)
        top.setText('\infty')
        top.move(80,10)
        top.setFixedWidth(40)
        bot = QtWidgets.QLineEdit(self)
        bot.textChanged.connect(self.handleInputbot)
        bot.setText('-\infty')
        bot.move(80,170)
        bot.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputtop(self,text):
        global topi
        topi = text
    def handleInputbot(self,text):
        global boti
        boti = text
def listeni():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('integral')>len(funcs['funcs'][0]['integral'][0]['integraln']):
        for i in (str(funcs['funcs'][0]['integral'][0]['integraln'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['integral'][0]['integraln']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowI()
    window.show()
    app.exec()
    k.write('\\displaystyle \\int{'+boti+'}^{'+topi+'}')
def listenshti():
    app = QApplication(sys.argv)
    window = WindowI()
    window.show()
    app.exec()
    k.write('\\displaystyle \\int{'+boti+'}^{'+topi+'}')
#endregion

#region matrix
class WindowMx(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,60)
        self.label = QLabel(self)
        global tipo
        tipo ='pmatrix'
        n = QtWidgets.QLineEdit(self)
        n.textChanged.connect(self.handleInputn)
        n.setText('1')
        n.move(10,10)
        n.setFixedWidth(40)
        m = QtWidgets.QLineEdit(self)
        m.textChanged.connect(self.handleInputm)
        m.setText('1')
        m.move(150,10)
        m.setFixedWidth(40)
        cb = QComboBox(self)
        cb.addItems(["Parentesis", "Nada", "Corchetes", "Llaves", "Verticales", "Dos Verticales"])
        cb.currentIndexChanged.connect(self.onChanged)
        cb.move(55,40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def onChanged(self, text):
        global tipo
        if int(text) == 0:
            tipo = 'pmatrix'
        elif int(text) == 1:
            tipo = 'matrix'
        elif int(text) == 2:
            tipo = 'bmatrix'
        elif int(text) == 3:
            tipo = 'Bmatrix'
        elif int(text) == 4:
            tipo = 'vmatrix'
        elif int(text) == 5:
            tipo = 'Vmatrix'
    def handleInputn(self,text):
        global nmx
        nmx = text
    def handleInputm(self,text):
        global mmx
        mmx = text
def listenmx():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('fraccion')>len(funcs['funcs'][0]['matrix'][0]['matrixn']):
        for i in (str(funcs['funcs'][0]['matrix'][0]['matrixn'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['matrix'][0]['matrixn']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowMx()
    window.show()
    app.exec()
    inside = ''
    for j in np.arange(1,int(nmx)+1,1):
        for i in np.arange(1,int(mmx)+1,1):
            inside += '0'
            inside += '&'
        inside = inside[:-1]
        inside += '\\\\ \n'
    try:
        k.write('\\begin{'+tipo+'}'+'\n'+inside+'\end{'+tipo+'}')
    except NameError:
        k.write('\\begin{'+'pmatrix'+'}'+'\n'+inside+'\end{'+'pmatrix'+'}')
def listenshtmx():
    app = QApplication(sys.argv)
    window = WindowMx()
    window.show()
    app.exec()
    inside = ''
    for j in np.arange(1,int(nmx)+1,1):
        for i in np.arange(1,int(mmx)+1,1):
            inside += ' '
            inside += '&'
        inside = inside[:-1]
        inside += '\\\\ \n'
    try:
        k.write('\\begin{'+tipo+'}'+'\n'+inside+'\end{'+tipo+'}')
    except NameError:
        k.write('\\begin{'+'pmatrix'+'}'+'\n'+inside+'\end{'+'pmatrix'+'}')
#endregion

#region fraccion
class WindowF(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,200)
        self.label = QLabel(self)
        self.pixmap = QPixmap('fraccion.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        topf = QtWidgets.QLineEdit(self)
        topf.textChanged.connect(self.handleInputtop)
        topf.setText(' ')
        topf.move(80,10)
        topf.setFixedWidth(40)
        botf = QtWidgets.QLineEdit(self)
        botf.textChanged.connect(self.handleInputbot)
        botf.setText(' ')
        botf.move(80,170)
        botf.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputtop(self,text):
        global tpf
        tpf = text
        print('acatmb')
    def handleInputbot(self,text):
        global btf
        btf = text
        print('llegue')
def listenf():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('fraccion')>len(funcs['funcs'][0]['fraccion'][0]['fraccionn']):
        for i in (str(funcs['funcs'][0]['fraccion'][0]['fraccionn'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['fraccion'][0]['fraccionn']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowF()
    window.show()
    app.exec()
    k.write('\\frac{'+tpf+'}{'+btf+'}')
def listenshtf():
    app = QApplication(sys.argv)
    window = WindowF()
    window.show()
    app.exec()
    k.write('\\frac{'+tpf+'}{'+btf+'}')
#endregion

#region derivada
class WindowDx(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,40)
        self.label = QLabel(self)
        global modo
        modo = 'd'
        tot = QRadioButton(self)
        tot.setChecked(True)
        tot.setText('Total')
        tot.mode = "d"
        tot.toggled.connect(self.onClicked)
        tot.move(0,0)
        ptl = QRadioButton(self)
        ptl.mode = "\partial"
        ptl.setText('Parcial')
        ptl.toggled.connect(self.onClicked)
        ptl.move(0,20)
        vard = QtWidgets.QLineEdit(self)
        vard.textChanged.connect(self.handleInputvar)
        vard.setText('x')
        vard.move(80,10)
        vard.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def onClicked(self):
        radioButton = self.sender()
        global modo
        print(radioButton.mode)
        modo = radioButton.mode
    def handleInputvar(self,text):
        global vars
        vars = text
def listendx():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('derivada')>len(funcs['funcs'][0]['derivada'][0]['derivadan']):
        for i in (str(funcs['funcs'][0]['derivada'][0]['derivadan'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['derivada'][0]['derivadan']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowDx()
    window.show()
    app.exec()
    k.write('\\frac{'+modo+ '}{'+modo+' '+vars+'}')
def listenshtdx():
    app = QApplication(sys.argv)
    window = WindowDx()
    window.show()
    app.exec()
    k.write('\\frac{'+modo+ '}{'+modo+' '+vars+'}')
#endregion

#region limite
class WindowL(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,200)
        self.label = QLabel(self)
        self.pixmap = QPixmap('fraccion.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.resize(self.pixmap.width(),self.pixmap.height())
        llm = QtWidgets.QLineEdit(self)
        llm.textChanged.connect(self.handleInputll)
        llm.setText(' ')
        llm.move(80,10)
        llm.setFixedWidth(40)
        rrm = QtWidgets.QLineEdit(self)
        rrm.textChanged.connect(self.handleInputrr)
        rrm.setText(' ')
        rrm.move(80,170)
        rrm.setFixedWidth(40)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputll(self,text):
        global ll
        ll = text
    def handleInputrr(self,text):
        global rr
        rr = text
def listenl():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('limite')>len(funcs['funcs'][0]['limite'][0]['limiten']):
        for i in (str(funcs['funcs'][0]['limite'][0]['limiten'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['limite'][0]['limiten']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowL()
    window.show()
    app.exec()
    k.write('\\displaystyle{\\lim_{'+ll+' \\to '+rr+'}}')
def listenshtl():
    app = QApplication(sys.argv)
    window = WindowL()
    window.show()
    app.exec()
    k.write('\\displaystyle{\\lim_{'+ll+' \\to '+rr+'}}')
#endregion

#endregion

#region latex

#region imagen
class WindowImg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logotipo.png'))
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(800,400,200,310)
        self.label = QLabel(self)
        global alg
        alg = 'empty'
        global lug
        lug = 'empty'
        global capq
        capq = 0
        global ttlq
        ttlq = 0
        lbllabel = QLabel(self)
        lbllabel.setText("Label")
        lbllabel.adjustSize()
        lbllabel.move(10,5)
        lbl = QtWidgets.QLineEdit(self)
        lbl.textChanged.connect(self.handleInputlbl)
        lbl.setText('fig')
        lbl.move(10,20)
        lbl.setFixedWidth(175)
        caplabel = QLabel(self)
        caplabel.setText("Caption")
        caplabel.adjustSize()
        caplabel.move(10,250)
        boton_cap = QButtonGroup(self)
        cpon = QRadioButton(self)
        cpon.setText('Caption')
        cpon.mode = 1
        cpon.toggled.connect(self.onClicked)
        cpon.move(10,285)
        boton_cap.addButton(cpon)
        cpoff = QRadioButton(self)
        cpoff.setChecked(True)
        cpoff.mode = 0
        cpoff.setText('No caption')
        cpoff.toggled.connect(self.onClicked)
        cpoff.move(10,265)
        boton_cap.addButton(cpoff)
        ttllabel = QLabel(self)
        ttllabel.setText("Titulo")
        ttllabel.adjustSize()
        ttllabel.move(10,75)
        boton_ttl = QButtonGroup(self)
        ttlon = QRadioButton(self)
        ttlon.setText('Titulo')
        ttlon.mode = 1
        ttlon.toggled.connect(self.onClicked2)
        ttlon.move(10,110)
        boton_ttl.addButton(ttlon)
        ttloff = QRadioButton(self)
        ttloff.mode = 0
        ttloff.setChecked(True)
        ttloff.setText('No titulo')
        ttloff.toggled.connect(self.onClicked2)
        ttloff.move(10,90)
        boton_ttl.addButton(ttloff)
        flllabel = QLabel(self)
        flllabel.setText("Archivo")
        flllabel.adjustSize()
        flllabel.move(10,40)
        fll = QtWidgets.QLineEdit(self)
        fll.textChanged.connect(self.handleInputfll)
        fll.setText('')
        fll.move(10,55)
        fll.setFixedWidth(175)
        fll.setText('frog.jpg')
        szlabel = QLabel(self)
        szlabel.setText("Tamaño de figura")
        szlabel.adjustSize()
        szlabel.move(10,130)
        sz = QtWidgets.QLineEdit(self)
        sz.textChanged.connect(self.handleInputsz)
        sz.setText('1')
        sz.move(10,145)
        sz.setFixedWidth(30)
        alglabel = QLabel(self)
        alglabel.setText("Alineado")
        alglabel.adjustSize()
        alglabel.move(10,170)
        align = QComboBox(self)
        align.addItems(["Default", "Centrado", "Derecha", "Izquierda"])
        align.currentIndexChanged.connect(self.onChanged1)
        align.move(10,185)
        psslabel = QLabel(self)
        psslabel.setText("Posición")
        psslabel.adjustSize()
        psslabel.move(10,210)
        poser = QComboBox(self)
        poser.addItems(["Default", "Arriba", "Acá", "Abajo"])
        poser.currentIndexChanged.connect(self.onChanged2)
        poser.move(10,225)
        self.shortcut_close = QShortcut(QKeySequence('Return'), self)
        self.shortcut_close.activated.connect(lambda : self.close())
        self.setWindowTitle("Parametros")
        self.show()
        self.raise_()
        self.activateWindow()
    def handleInputfll(self,text):
        global file
        file = text
    def handleInputttl(self,text):
        global title
        title = text
    def handleInputlbl(self,text):
        global label
        label = text
    def onClicked(self):
        radioButton = self.sender()
        global capq
        print(radioButton.mode)
        capq = radioButton.mode
    def onClicked2(self):
        radioButton = self.sender()
        global ttlq
        print(radioButton.mode)
        ttlq = radioButton.mode
    def handleInputsz(self,text):
        global szz
        szz = text
    def onChanged1(self, text):
        global alg
        if int(text) == 0:
            alg = ''
        elif int(text) == 1:
            alg = '\\centering'
        elif int(text) == 2:
            alg = '\\raggedright'
        elif int(text) == 3:
            alg = '\\raggedleft'
    def onChanged2(self, text):
        global lug
        if int(text) == 0:
            lug = ''
        elif int(text) == 1:
            lug = 't'
        elif int(text) == 2:
            lug = 't'
        elif int(text) == 3:
            lug = 'b'
def listenimg():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if len('imagen')>len(funcs['funcs'][0]['imagen'][0]['imagenn']):
        for i in (str(funcs['funcs'][0]['imagen'][0]['imagenn'])+'.'):
            k.send('backspace')
    else:
        for i in (funcs['funcs'][0]['imagen'][0]['imagenn']+'.'):
            k.send('backspace')
    app = QApplication(sys.argv)
    window = WindowImg()
    window.show()
    app.exec()
    printer = '\\begin'+'{'+'figure'+'}'
    if lug != 'empty':
        printer = printer+'['+lug+']'+'\n  '
    else:
        printer = printer+'\n  '
    print(printer)
    if alg != 'empty':
        printer = printer+alg+'\n'
    print(printer)
    if ttlq ==1:
        printer = printer+'\\textbf{}\par\medskip'+'\n'
    print(printer)
    printer = printer+'\includegraphics[scale='+szz+']{'+file+'}'+'\n'
    print(printer)
    if capq == 1:
        printer = printer+'\\caption{}\n'
    printer = printer+'\label{fig:'+label+'}'+'\n'+'\end{figure}'
    print(printer)
    time.sleep(0.001)
    k.write(printer)
def listenshtimg():
    app = QApplication(sys.argv)
    window = WindowImg()
    window.show()
    app.exec()
    printer = '\\begin'+'{'+'figure'+'}'
    if lug != 'empty':
        printer = printer+'['+lug+']'+'\n  '
    else:
        printer = printer+'\n  '
    print(printer)
    if alg != 'empty':
        printer = printer+alg+'\n'
    print(printer)
    if ttlq ==1:
        printer = printer+'\\textbf{}\par\medskip'+'\n'
    print(printer)
    printer = printer+'\includegraphics[scale='+szz+']{'+file+'}'+'\n'
    print(printer)
    if capq == 1:
        printer = printer+'\\caption{}\n'
    printer = printer+'\label{fig:'+label+'}'+'\n'+'\end{figure}'
    print(printer)
    time.sleep(0.001)
    k.write(printer)
#endregion

#endregion

#region keylog
funciones = {'sumatoria':[listens,listenshts],
'integral':[listeni,listenshti],
'fraccion':[listenf,listenshtf],
'multiplicatoria':[listenm,listenshtm],
'matrix':[listenmx,listenshtmx],
'limite':[listenl,listenshtl],
'derivada':[listendx,listenshtdx],
'imagen':[listenimg,listenshtimg]}

def keylogs():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    for fct in list((funcs['funcs'][0]).keys()):
        fct = str(fct)
        try:
            k.remove_hotkey(funcs['funcs'][0][fct][0][fct+'s'])
            k.remove_word_listener(funcs['funcs'][0][fct][0][fct+'n'])
        except KeyError:
           pass
        try:
            k.add_hotkey(funcs['funcs'][0][fct][0][fct+'s'], callback=funciones[fct][1], suppress=False)
            k.add_word_listener(funcs['funcs'][0][fct][0][fct+'n'], triggers='.', callback=funciones[fct][0])
        except ValueError:
            pass
    try:
        k.remove_word_listener('opciones')
    except:
        pass
    k.add_word_listener('opciones', triggers='.', callback=listensettings)

pimba = [0]

print(pimba)
def booteo():
    f = open('funcs.json',)
    funcs = json.load(f)
    f.close()
    if pimba[-1] == 0:
        keylogs()
        pimba.append(1)
        print(pimba)
    else:
        for fct in list((funcs['funcs'][0]).keys()):
            fct = str(fct)
            try:
                k.remove_hotkey(funcs['funcs'][0][fct][0][fct+'s'])
                k.remove_word_listener(funcs['funcs'][0][fct][0][fct+'n'])
            except KeyError:
                pass
        pimba.append(0)
        print(pimba)

k.add_hotkey('alt+p', callback=booteo)
app = QApplication(sys.argv)
window = startup()
window.show()
app.exec()
k.wait()
#endregion