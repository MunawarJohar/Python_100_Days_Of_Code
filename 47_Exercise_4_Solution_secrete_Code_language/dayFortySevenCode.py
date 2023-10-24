str=input("Enter Your message ")
words=str.split(" ")
coding=input("1 for coding 2 for deconding")
coding=True if(coding=="1") else False
if(coding):
    newWord=[]
    for word in words:
      if(len(word)>=3):
         random1="mun"
         random2="kam"
         strnew=random1=word[1:]+word[0]+random2




         newWord.append(strnew)
    else:
        newWord.append(word[::-1])         
    print(" ".join(newWord))
         
else:
    newWord=[]
    for word in words:
       if(len(word)>=3):
        strnew=word[3:-3]
        newWord=strnew[-1]+strnew[:-1]
        newWord.append(strnew)
       else:
            newWord.append(word[::-1])
    print(" ".join(newWord))