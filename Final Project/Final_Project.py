# 10 soruluk bilgi yarismasi. 5 ve üzeri dogru basarili.
# cevaplar case sensitive
# her soru 10 puan

# Python strings are case sensitive. 
# Sadece 7,8 ve 9. soruları case INsensitive yapacağım. 

print("10 sorudan oluşan yarışmaya hoşgeldiniz!\n" , 
      "Cevap verirken Büyük-Küçük harf duyarlılığına dikkat ediniz.\n", 
      "Özel isimler için Büyük-Küçük harf duyarlılığı bulunmaktadır.\n", 
      "Kazanmak için en az 50 puan almalısınız.\n", 
      "Başarılar dileriz:)\n")
puan = 0 #global variable

soru1 = str(input("1- Atatürk nerede doğmuştur? "))  #Selanik
soru2 = int(input("2- Çanakkale Zaferi hangi yıl gerçekleşmiştir? "))  # 1915
soru3 = str(input("3- Türkiye yüzölçümü en büyük olan ili hangisidir? "))  #Konya
soru4 = str(input("4- Türkiye'nin kuzeydeki en uç noktası hangi şehire aittir? "))  #Sinop
soru5 = str(input("5- Atatürk'ün Samsun'a çıktığı tarihi '01 Ocak 2001' benzerinde yazınız?  "))  #19 Mayıs 1919
soru6 = str(input("6- 61 hangi ilin plakasıdır? "))  #Trabzon
soru7 = str(input("7- Ton balığının diğer adı nedir? ")) #orkinos
soru8 = str(input("8- Dünyada en hızlı koşan kuş hangisidir? ")) #devekuşu
soru9 = str(input("9- Tüm kan gruplarından kan alabilen, genel alıcı kan grubu hangisidir? "))  #ab
soru10 = str(input("10- Tıp yeminine adı veren, İspanyol bilim insanının adı nedir? "))  #Hipokrat

##1.SORU
if soru1 == "Selanik": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")     
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##2.SORU
if soru2 == 1915: 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##3.SORU
if soru3 == "Konya": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")    
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##4.SORU
if soru4 == "Sinop": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##5.SORU
if soru5 == "19 Mayıs 1919": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")   
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##6.SORU
if soru6 == "Trabzon": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##7.SORU
if soru7.casefold() == "orkinos": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")   
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##8.SORU
if soru8.casefold() == "devekuşu": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##9.SORU
if soru9.casefold() == "ab": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")    
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)

##10.SORU
if soru10 == "Hipokrat": 
    puan += 1
    print("Doğru, 10 Puan!", "Toplam puanınız", puan*10, "a ulaştı\n")
else:
    print("xx Yanlış Cevap!", "Toplam puan:", puan*10)
    
####
if puan >= 5:
    print("\n Tebrikler kazandınız!!")
else:
    print("\n Maalesef kazanamadınız:( ", "Puanınız 50'den az.")
