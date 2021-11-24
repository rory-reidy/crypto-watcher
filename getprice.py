from coinbase.wallet.client import Client
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
api_key='1234' #replace with actual key and secret
api_secret='1234'
while True:
    client = Client(api_key, api_secret)
    accounts = client.get_accounts()
    filt = []
   # print(client.get_transactions())
    for i in accounts.data: 
        if float(i.balance.amount)>0:
            filt.append(i)
            print(i)
            
    #print(client.get_exchange_rates())
    print('Balances: ')
    for i in filt:
        print(i.currency, ": ", i.balance.amount, "(", i.native_balance.amount, i.native_balance.currency, ")")
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowFlags(Qt.WindowStaysOnTopHint)

    window.setGeometry(0, 0, 500, 100)
    window.setWindowTitle('Coinbase Updates')
    layout = QHBoxLayout()
    label1 = QLabel("My Balances: \n")
    label1.move(20, 0)
    label1.setFont(QFont('Arial', 14))
    layout.addWidget(label1)
    ypos = 20
    for i in filt:
        str = i.currency + ": " + i.balance.amount + " (" + i.native_balance.amount + i.native_balance.currency + ")<br/><br/>"
        label2 = QLabel(str)
        label2.setFont(QFont('Times New Roman', 14))
        label2.move(ypos, ypos)
        layout.addWidget(label2)
        ypos += 20
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
    time.sleep(3)