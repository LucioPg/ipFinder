from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import os
from time import sleep
# from gui import Ui_MainWindow as mainwindow
from gui import Ui_MainWindow as mainwindow
from waitingspinnerwidget import MySp

class IpFinder(mainwindow, QMainWindow):
    """"""

    def __init__(self,nomePc = None):
        super(IpFinder, self).__init__()
        if nomePc is None:
            nomePc = 'PC-DELL'
        self.thread = QtCore.QThread()
        self.nomePc = nomePc
        self.listaNomi = {}
        self.setupUi(self)
        icona = QtGui.QIcon('sunny.ico')
        self.setWindowIcon(icona)
        self.tableWidget.ITEMDOUBLECLICK.connect(self.insertLineEdit)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowFlags(QtCore.Qt.)
        self.oPos = self.pos()
        self.borderRadius = 150
        self.initSpinner()
        self.confFile = "config.ini"
        self.myIpFile = "ip.txt"
        self.myIpLan = None
        self.configurazione = {'intervallo_min':'192.168.1.0', 'intervallo_max':'192.168.1.255', 'nomiPc':[self.nomePc]}
        self.checkConf()
        self.defaultIp = '192.168.1.44'
        self.bot_cerca.clicked.connect(self.cercaPc)
        self.bot_esci.clicked.connect(self.close)
        self.thread.started.connect(self.spinnerStart)

        self.worker = Worker(self.funcCercaPc)
        self.worker.moveToThread(self.thread)
        self.worker.SEGNALE.connect(self.spinnerStop)
        self.worker.SEGNALE.connect(self.riusc)
        self.thread.started.connect(self.worker.run)
        # self.thread.start()
        # self.spinnerStart()

    # def mousePressEvent(self, event):
    #     self.oPos = event.globalPos()
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     delta = QtCore.QPoint(QMouseEvent.globalPos() - self.oPos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.oPos = QMouseEvent.globalPos()



    def cercaPc(self):
        """func che cerca il pc in lan con in nome self.nomePc
            nell'intervallo impostato nella configurazione"""
        self.thread.start()

    def checkConf(self):
        """func per leggere le impostazioni di default
            crea il file nel caso non fosse presente"""
        try:
            with open(self.confFile, 'r') as f:
                dati = f.readlines()
            for d in dati:
                chiave, val = d.split('=')
                if chiave == 'nomiPc':
                    val = val.replace('[', '')
                    val = val.replace(']', '')
                    lista = val.split(';')
                    for n in lista:
                        if n == '':
                            continue
                        if n not in self.configurazione['nomiPc']:
                            self.configurazione['nomiPc'].append(n)
                else:
                    self.configurazione[chiave] = val
            # print('results:')
            # for k, v in self.configurazione.items():
            #     print(k, '   ', v)
        except FileNotFoundError:
            confToWrite = ''
            for k, v in self.configurazione.items():
                if type(self.configurazione[k]) is list:
                    confToWrite += k + '=['
                    for n in v:
                        confToWrite += n + ';'
                    confToWrite += ']'
                else:
                    confToWrite += k + "=" + v + '\n'
            with open(self.confFile, 'w') as f:
                f.write(confToWrite)
        finally:
            for n in self.configurazione['nomiPc']:
                self.setComboNomePc(n)

    def funcCercaPc(self):
        os.system('ipconfig >> {}'.format(self.myIpFile))
        with open(self.myIpFile, 'r') as ipfile:
            result = ipfile.readlines()
        for line in result:
            if "LAN" in line:
                # print(line)
                # print(result.index(line))
                last = result[result.index(line):]
                for l in last:
                    if 'IPv4' in l:
                        self.myIpLan = l.split(' : ')[-1].strip()
                        break
                    else:
                        self.myIpLan = None
        if self.myIpLan is None:
            print(" il computer non è connesso")
            return False

        # print(' il mio ip in lan: ',self.myIpLan)
        maskList = self.myIpLan.split('.')[:3]
        mask = ''
        for n in maskList:
            mask += n + '.'
        # print('my mask: ',mask)
        os.system('arp -a >> arpa.txt')
        print('*'*50)
        dacercare = f'Interfaccia: '
        # print(len(self.myIpLan))
        with open('arpa.txt', 'r') as arpa:
            resultarpaTemp = arpa.readlines()
        # print(type(resultarpaTemp))
        listaIps = []
        for ar in resultarpaTemp:
            if (('Interfaccia: '+self.myIpLan) or ('Interface: '+self.myIpLan)) in ar:
                indice = resultarpaTemp.index(ar)
                # risul = [x.split('\n') for x in resultarpaTemp[indice:] if x.split('\n') != '']
                risultati = [x for x in resultarpaTemp[indice:] if x != '']
                stringa = ''
                # print(risultati[2:])
                for r in risultati[2:]:
                    if 'static' not in r:
                        tempList = [ x for x in r.split('   ') if x != '']
                        ip = tempList[0].strip()
                        listaIps.append(ip)
                #     for c in r:
                #         if c != '':
                #             stringa += c
                for ips in listaIps:
                    if not self.getPcName(ips):
                        break
                # for myarp in resultarpaTemp[indice]:
                #     print(myarp)
                break

        self.tableWidget.setRowCount(0)
        self.riempiTab()
        os.system(f'del {self.myIpFile}')
        os.system(f'del arpa.txt')
        os.system(f'del listaip.txt')
        return True

    def getPcName(self,ips):
        os.system(f'ping -a -n 1 {ips} > listaip.txt')

        with open('listaip.txt', 'r') as ipf:
            # print(ipf.readline(2))
            try:
                lines = ipf.readlines()[1]
                print(lines)
                line = lines.split(' Ping ')[1].split(' ')
                self.listaNomi[ips] = line[0].strip()

            except IndexError:
                return False

            return self.listaNomi
    def initSpinner(self):
        self.spinner = MySp(self.spinnerWidget)
        gridlay = QGridLayout(self.spinnerWidget)
        self.spinner.setRevolutionsPerSecond(1.2)
        gridlay.addWidget(self.spinner)
        self.spinnerWidget.setLayout(gridlay)
        self.spinner.stop()

    def insertLineEdit(self,ip):
        self.lineEdit.setText(ip)
        self.lineEdit.selectAll()

    def riempiTab(self):
        print(self.listaNomi)
        row = 0
        for ip, nome in self.listaNomi.items():
            self.tableWidget.insertRow(row)
            print(ip,' ',nome)
            itemIp = QTableWidgetItem()
            itemIp.setText(ip)
            itemNome = QTableWidgetItem()
            itemNome.setText(nome)
            item = QTableWidgetItem()
            item.setText('ciao')
            # self.tableWidget.setItem(row, 0, item)
            # self.tableWidget.item(itemIp, row, 0)
            # self.tableWidget.item(itemNome, row, 1)
            self.tableWidget.setItem(row,0,itemIp)
            # self.tableWidget.setItem()
            self.tableWidget.setItem(row,1,itemNome)
            row += 1
        # print(self.tableWidget.rowCount())

    def riusc(self,t):
        self.statusbar.showMessage(t)
        if t == 'riuscito':
            self.spinner.setColor(QtCore.Qt.green)
        else:
            self.spinner.setColor(QtCore.Qt.red)
        self.thread.exit()

    def setComboNomePc(self,nome):
        cerca = self.comboBox_nomePc.findText(nome, QtCore.Qt.MatchExactly)
        if cerca == -1:
            self.comboBox_nomePc.addItem(nome)
        print(cerca)

    def spinnerStart(self):
        self.spinner.setColor(QtCore.Qt.black)
        self.spinner.start()

    def spinnerStop(self):
        self.spinner.stop()

class Worker(QtCore.QObject):
    SEGNALE = QtCore.pyqtSignal(str)

    def __init__(self,some=''):
        QtCore.QObject.__init__(self)
        self.some = some

    def run(self):
        print('sono attivo')
        # for i in range(10):
        #     print(i)
        #     sleep(1)
        if callable(self.some):
            if self.some():
                self.SEGNALE.emit('riuscito')
            else:
                self.SEGNALE.emit('fallito')
        else:
            self.SEGNALE.emit('fallito')
# class MyThread(QtCore.QThread):
#     def __init__(self):
#         QtCore.QThread.__init__(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        nomePc = sys.argv
    main = IpFinder()
    main.show()

    sys.exit(app.exec_())