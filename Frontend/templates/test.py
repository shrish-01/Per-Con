
main={
"q.1":"# Little interest or pleasure in doing things\n    Not at all\n    Several days\n    More than half of the days\n    Nearly every day",
"q.2":"# Feeling down, depressed, or hopeless\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.3":"#Trouble falling or staying asleep, or sleeping too much\n  Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.4":"#Feeling tired or having little energy\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.5":"#Poor appetite or overeating\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.6":"#Feeling bad about yourself - or that you are a failure or have let yourself or your family down\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.7":"#Trouble concentrating on things, such as reading the newspaper or watching television\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.8":"#Moving or speaking so slowly that other people could have noticed\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.9":"Thoughts that you would be better off dead, or of hurting yourself\n    Not at all\n    Several days\n    More than half the days\n    Nearly every day",
"q.10":"If you've had any days with issues above, how difficult have these problems made it for you at work, home, school, or with other people?\n    Not difficult at all\n    Somewhat difficult\n    Very difficult\n    Extremely difficult"

}
m=0
responsemain=[]
answer=[1,2]
for i in range (1,11):
    a="q."+str(i)
    print(main[a])
    response=int(input())
    responsemain.append(response)

n=len(responsemain)
for j in range(n):
    if (responsemain[j]==1):
        m+=0.25
    elif (responsemain[j]==2):
        m+=0.50
    elif (responsemain[j]==3):
        m+=0.75
    elif (responsemain[j]==4):
        m+=1.00
    else:
        pass

score=m*10
print(score)



    




