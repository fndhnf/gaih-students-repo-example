
####### herbir ogrenci bilgisini ve notlarını kullanıcıdan alıyorum
# a1..a5 öğrencilerin 2dictionary' si


a1 = {"student name":"name",	"student number": 1,	"midterm grade": 0,	"project grade": 0,	"final grade": 0,	"passing grade": 0}

name = str(input("Please enter you name and surname: "))
nr = int(input("Please enter you student number: "))
mg1 = int(input("Please enter you midterm grade: "))
pg1 = int(input("Please enter you project grade: "))
fg1 = int(input("Please enter you final grade: "))

passg1 = mg1*0.3 + pg1*0.3 + fg1*0.4       # gecme notunu hesaplıyorum

a1["student name"] = name   # user'dan aldığım bilgileri dictionary içinde index'e kaydediyorum
a1["student number"] = nr
a1["midterm grade"] = mg1
a1["project grade"] = pg1
a1["final  grade"] = fg1
a1["passing  grade"] = passg1

print (a1)    # kullanıcıya ait tüm alınan değerler ekrana yazdırıldı

#######

a2 = {"student name":"name",	"student number": 1,	"midterm grade": 0,	"project grade": 0,	"final grade": 0,	"passing grade": 0}

name = str(input("Please enter you name and surname: "))
nr = int(input("Please enter you student number: "))
mg2 = int(input("Please enter you midterm grade: "))
pg2 = int(input("Please enter you project grade: "))
fg2 = int(input("Please enter you final grade: "))

passg2 = mg2*0.3 + pg2*0.3 + fg2*0.4

a2["student name"] = name
a2["student number"] = nr
a2["midterm grade"] = mg2
a2["project grade"] = pg2
a2["final  grade"] = fg2
a2["passing  grade"] = passg2

print (a2)


#######

a3 = {"student name":"name",	"student number": 1,	"midterm grade": 0,	"project grade": 0,	"final grade": 0,	"passing grade": 0}

name = str(input("Please enter you name and surname: "))
nr = int(input("Please enter you student number: "))
mg3 = int(input("Please enter you midterm grade: "))
pg3 = int(input("Please enter you project grade: "))
fg3 = int(input("Please enter you final grade: "))

passg3 = mg3*0.3 + pg3*0.3 + fg3*0.4

a3["student name"] = name
a3["student number"] = nr
a3["midterm grade"] = mg3
a3["project grade"] = pg3
a3["final  grade"] = fg3
a3["passing  grade"] = passg3

print (a3)


#######


a4 = {"student name":"name",	"student number": 1,	"midterm grade": 0,	"project grade": 0,	"final grade": 0,	"passing grade": 0}

name = str(input("Please enter you name and surname: "))
nr = int(input("Please enter you student number: "))
mg4 = int(input("Please enter you midterm grade: "))
pg4 = int(input("Please enter you project grade: "))
fg4 = int(input("Please enter you final grade: "))

passg4 = mg4*0.3 + pg4*0.3 + fg4*0.4

a4["student name"] = name
a4["student number"] = nr
a4["midterm grade"] = mg4
a4["project grade"] = pg4
a4["final  grade"] = fg4
a4["passing  grade"] = passg4

print (a4)

#######

a5 = {"student name":"name",	"student number": 1,	"midterm grade": 0,	"project grade": 0,	"final grade": 0,	"passing grade": 0}

name = str(input("Please enter you name and surname: "))
nr = int(input("Please enter you student number: "))
mg5 = int(input("Please enter you midterm grade: "))
pg5 = int(input("Please enter you project grade: "))
fg5 = int(input("Please enter you final grade: "))

passg5 = mg5*0.3 + pg5*0.3 + fg5*0.4

a5["student name"] = name
a5["student number"] = nr
a5["midterm grade"] = mg5
a5["project grade"] = pg5
a5["final  grade"] = fg5
a5["passing  grade"] = passg5

print (a5)


#######

listPG = [passg1, passg2, passg3, passg4, passg5]       # geçme notları bir listeye kaydediliyor

print (sorted(listPG, reverse=True))    # liste degerlerinde sıralama ve sonrasında listeyi ters çevirme yapılıyor.
