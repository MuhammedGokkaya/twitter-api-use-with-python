#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
import time
import webbrowser
from pyquery import PyQuery
from time import strftime
from pushover import init, Client



CONSUMER_KEY = ' '
CONSUMER_SECRET = ' '
ACCESS_TOKEN = " "
ACCESS_TOKEN_SECRET = " "
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


init(" ")#Pushoher kulanımı için...

print "#".ljust(30,"#")
webbrowser.open_new_tab("https://twitter.com/@...")#webbrowserda hesabınızın otomatik açılması sağlar
k = PyQuery("https://twitter.com/@...") 
print k('title').html()                       
print "#".ljust(30,"#")
                                           
#Takip ettiği kişi sayısını verir                                 
print "Takip ettiği kişi sayısı:"             
user = twitter.get_user_timeline()            
print user[0]['user']['friends_count']        
print "#".ljust(30,"#")
        
##Takipçi sayısını verir                              
print "Takipçi sayısı..........:"             
user = twitter.get_user_timeline()            
print user[0]['user']['followers_count']      
print "#".ljust(30,"#")

##Attığı tweet sayısını verir
print "Attığı tweet sayısı.....:"
user = twitter.get_user_timeline()
print user[0]['user']['statuses_count']
print "#".ljust(30,"#")
print " ".ljust(30," ")

while True:
	print "-".ljust(30,"-")
 
	sec=raw_input("Botu Nasıl Kullanacaksınız?\n1)time fonksiyonu\n2)Fotoğraf gönderen\n3)Txt den yazılı mesaj çekmek\nSeçiminiz:")
	print "-".ljust(30,"-")
	
	if sec=="1":

		while True:
	
	

			if strftime("%M") == "00" or strftime("%M") == "15" or strftime("%M") == "30" or strftime("%M") == "45"  :

				if time.strftime("%A")=="Sunday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Gün:Pazar---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)
				if time.strftime("%A")=="Monday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Day:Pazartesi---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
				if time.strftime("%A")=="Tuesday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Day:Salı---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
				if time.strftime("%A")=="Wednesday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Gün:Çarşamba---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
				if time.strftime("%A")=="Thursday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Gün:Perşembe---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
				if time.strftime("%A")=="Friday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Gün:Cuma---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
				if time.strftime("%A")=="Saturday" :

					print time.strftime("...Mesaj gönderiliyor...")
					twitter.update_status(status=time.strftime("SAAT:%H:%M---Gün:Cumartesi---Tarih:%d/%m/%y")) 
					client = Client("pushover-api key").send_message(strftime("SAAT:%H:%M mesaj gönderildi..."),title="Twitter Botu Hakkında")
					time.sleep(900)	
			else :
				pass
	if sec=="2" :
		while True :
			mesaj=raw_input("Mesajı girin..:")
			twitter.update_status(status=mesaj)
			sec1=raw_input("Fotoğraf göndermek için:1 e,Çıkmak için 0(sıfır)'a; basınız....")
			if sec1=="1" :
				bslik=raw_input=("Başlık girin..:")
				photo = open('/home/muhammed/Desktop/dosya.jpg','rb')		
				twitter.update_status_with_media(status=bslik,media=photo)
			
			if sec1=="0" :
				break
			else :
				pass
	if sec=="3" :
		try:
			message = open('/home/muhammed/Desktop/Twitter-api/file.txt')
			sure=input("Süreyi girin:")
			while  True:
				twitter.update_status(status=message.readline()) 
				print("...Çekilen cümle:",message.readline())
				print("...Mesaj gönderildi...")
				time.sleep(sure)
		except IOError:
			print("bir hata oluştu!")
		finally:
			file.close()
		
	else :
		print("1 , 2  veya 3  tuşuna bas!!!")
		pass
