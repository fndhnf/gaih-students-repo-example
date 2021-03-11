#Explain your work



d1 = {}	
d2 = {}
d3 = {}
d4 = {}
d5 = {}

d1 = {"isim":"Funda", "soyisim":"Cetin", "yas":38, "meslek":"muhendis", "sehir":"ankara", "telefon":5554443322, "aranan pozisyon":"danismanlik"}  	#1.cv
d2 = {"isim":"Caner", "soyisim":"Kir", "yas":18, "meslek":"ogrenci", "sehir":"izmir", "telefon":5553331122, "aranan pozisyon":"stajyerlik" }	 #2.cv
d3 = {"isim":"Sevgi", "soyisim":"Torun", "yas":33, "meslek":"bankaci", "sehir":"konya", "telefon":5554443311, "aranan pozisyon":"bankaci" }	 #3.cv
d4 = {"isim":"Umut", "soyisim":"Yilmaz", "yas":21, "meslek":"cevirmen", "sehir":"ankara", "telefon":5554441122, "aranan pozisyon":"tercümanlik" }	 #4.cv
d5 = {"isim":"Zafer", "soyisim":"Aksu", "yas":27, "meslek":"muhasebeci", "sehir":"trabzon", "telefon":5551113322, "aranan pozisyon":"muhasebeyetkilisi" } 	#5.cv

########
d1_copy = d1.copy()  	#data kaybı olmaması icin kopyalama onemli denmisti
d2_copy = d2.copy()
d3_copy = d3.copy()
d4_copy = d4.copy()
d5_copy = d5.copy()

d = {}  	 # containing the inf of the 5 created CV/people
d["CV1"] = d1_copy 	#bos olan d sozlugune cv1 key ataması yapıyorum, value olarak da d1 sozlugunun kopyasını kaydediyorum
d["CV2"] = d2_copy
d["CV3"] = d3_copy
d["CV4"] = d4_copy
d["CV5"] = d5_copy

print (d1) 
print (d2)
print (d3)
print (d4)
print (d5)
print (d)

 
