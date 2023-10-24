#Solution of KBC
questions=[["Which is used in artificial intelligence ?","JavaScript","Python","C++","None",2],
["How is the founder of python langauge ?","Jims","Guido van Rossum","Ali","None",2],
["Which one is  best langauge ?","JavaScript","Python","C++","None",1],
["Which one is the oldest language ?","JavaScript","Python","C++","None",3],
["Which is not a programming langauge ?","JavaScript","Python","C++","None",4],]

money=0
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a.{question[1]}         b. {question[2]}")
    print(f"c.{question[3]}         d. {question[4]}")
    reply=int(input("Enter your answer (1-4 ) exit for 0 : "))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, you have won {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==15):
            money=10000000

    else:
        print("Wrong answers !")     
        break
print(f"You take money is {money}")