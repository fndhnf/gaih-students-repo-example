#Explain your work

	
#####	
nums = list(range(100)) #a=100 dersek
evenlist = []
oddlist = []

# odds = [i for i in numbers if i%2!=0]  alternatif olabilirdi

for x in nums: 	# bu formatta istendigini dusundugumden, buradan devam ediyorum
	if (x % 2 == 0) : #2ye kalansız bolunuyorsa cıfttir
		evenlist.append(x)	
	if (x % 2 != 0) : #else de kullanılabilirdi
		oddlist.append(x)

print(evenlist)
print(oddlist)

#####
mergedlist2 = [] 
mergedlist = evenlist + oddlist  #listeleri birleştirme aşaması
mergedlist2 = [i*2 for i in mergedlist] #herbir indexi 2 ile carpma
print(mergedlist2)

######
for j in range (0, len(mergedlist2)): 
		print (j, "th item' data type is:", type(mergedlist2[j]))

