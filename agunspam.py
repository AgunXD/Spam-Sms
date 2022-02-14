import requests
import time,os,sys

# clear
os.system('clear')
# logo
print ('------------------')
print ('[+] Author by AgunXd')
print ('[+] channel Agunmyyouz')
print ('------------------')
print ('\n[+] nomor Diawali 8xxxx')

# Run nomor
nomor = input('[+] Nomor Target : ')
req=requests.get('https://ainxbot-sms.herokuapp.com/api/spamsms',params={'phone' : nomor}).text
if  'terkirim' in req:
     print ('\n[+]Spam Berhasil Gun')
else:
     print ('\n[!]Spam nya gagal Gun')
