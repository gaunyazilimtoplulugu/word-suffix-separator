import re
sentence = input("give a sentence: ")
sentence = sentence.strip().lower()
sentencelist = sentence.split() # liste haline getirdik
dotless = [] 
for elemanlar in sentencelist: #dotless adında bir liste oluşturduk karakter ifadelerden kurtulduk
    b = elemanlar.strip("!\#$%&'()*+,-./:;<=>?@[\]^`{|}~")
    dotless.append(b)    
# print(dotless)
suffixes = ["acy","ance","ence","dom","er","or","ism","ist","ty",
"ment","ness","ship","sion","tion","ate","esque", "ful", "ic", 
"ous", "ish", "ive", "less", "ed", "ing", "ly", "ward", "wise"]
i = 0
alist = ["ment"]
m =0
kelimelist = [] #bir liste oluşturduk ve sonu eklerler bitenleri aldık
for c in range(0,len(dotless)):
        for i in range(0,len(suffixes)):
            if dotless[c].endswith(f"{suffixes[i]}"):
                kelimelist.append(dotless[c])

while m < len(kelimelist):
    for c in range(0,len(kelimelist)):
        for i in range(0,len(suffixes)):
            if kelimelist[c].endswith(f"{suffixes[i]}"):
                alist.append(suffixes[i])
                a = re.findall("[a-z]",alist[m+1])
                print(kelimelist[m][:len(kelimelist[m])-len(a)] +"_"+ alist[m+1])
                break
            i+=1 
        m +=1

if len(alist) == 1:
    print("aranılan eklerden hiçbiri yok ")