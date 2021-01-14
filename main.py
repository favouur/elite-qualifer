from textblob import Textblob

file=open ("1.txt,r+")
a= file 1.read()

print("original text : ",+str(a))

b=Textblob(a)

print("corrected text : "+str(b.correct()) )
file1.close()

d=open ("1.txt","w")
d.write(str(b.correct()))
d.close()
