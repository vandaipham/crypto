# coding: utf8
# Устанавливаем стандартную внешнюю кодировку = utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Crypto.Cipher import ARC2
import time
import os
import numpy as np
import matplotlib.pyplot as plt
from array import *
from datetime import datetime

plt.rc('font', family='Verdana')
entime = array('d')
detime = array('d')
x = np.arange(1,100,1)
#size blok
BLOCK_SIZE = 32

for i in range(1,100):
        #generation key
        secret = os.urandom(BLOCK_SIZE)
        obj = ARC2.new(secret)
        message = "InternetofThingsIoTis the future"
        print(len(message))

        # Encryption
        first = datetime.now().microsecond
        ciphertext = obj.encrypt(message)
        delta = (datetime.now().microsecond - first)
        entime.append(delta)
        print("Encryption time = " + str(delta))
        time.sleep(0.001)

        # Decode
        first = datetime.now().microsecond
        mes = obj.decrypt(ciphertext)
        delta = (datetime.now().microsecond - first)
        detime.append(delta)
        print ("Decryption time = " + str(delta))
        time.sleep(0.001)
        
plt.plot(x, entime, 'r^', x, detime, 'bs',)
plt.xlabel('Число испытаний')
plt.ylabel('Время в миллисекундах')
plt.title('Шифрование и расшифрование ARC2')
plt.legend(['Время шифрования', 'Время расшифрования'])
plt.show()

