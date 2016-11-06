# coding: utf8
# Устанавливаем стандартную внешнюю кодировку = utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
import ast
import numpy as np
import matplotlib.pyplot as plt
from array import *
from datetime import datetime
import time

plt.rc('font', family='Verdana')
entime = array('d')
detime = array('d')
x = np.arange(1,100,1)

for i in range(1,100):
	random_generator = Random.new().read
	key = ElGamal.generate(24, Random.new().read) #generate pub and priv key
	
	publickey = key.publickey() # pub key export for exchange
	
	msg = "InternetofThingsIoTis the future"
	first = datetime.now().microsecond
	encrypted = publickey.encrypt(msg, 32)
	delta = (datetime.now().microsecond - first)
	entime.append(delta)
	time.sleep(0.001)
	
	#decrypted code below
	first = datetime.now().microsecond
	decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
	delta = (datetime.now().microsecond - first)
	detime.append(delta)
	print 'decrypted', decrypted
	time.sleep(0.001)

plt.plot(x, entime, 'r^', x, detime, 'bs',)
plt.xlabel('Число испытаний')
plt.ylabel('Время в миллисекундах')
plt.title('Шифрование и расшифрование ElGamal')
plt.legend(['Время шифрования', 'Время расшифрования'])
plt.show()
