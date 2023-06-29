questions=["how many continents are there?","what is the capital of india","what courses are taught in NG",]
options=[["1.Four","2.Nine","3.Seven","4.Eight"],["1.Chandigarh","2.Bhopal","3.Chennai","4.Delhi"],["1.Software Engineering","2.Counseling","3.Tourism","4.Agriculture"]]
answerkeys=[3,4,1]
lifeline_options=[["3.Seven","4.Eight"],["3.Chennai","4.Delhi"],["1.Software Engineering","2.Counseling"]]

i=0
c=0
amount=0
while i<len(questions):
    print(questions[i])

    j=0
    while j<len(options[i]):
        print(options[i][j])
        j=j+1

    k=c
    while k<1:
        lifeline=input("Do you want lifeline yes or no")
        k=k+1
        if lifeline=="yes":
            s=0
            while s<len(lifeline_options[i]):
                print(lifeline_options[i][s])
                c=c+1
                s=s+1
              

    select=int(input("choose any one options"))
    if select==answerkeys[i]:
        amount=amount+1000
        print("congrats! your answer is correct you win=",amount)
    else:
        print("sadly your name is wrong.Out of the gane now.")
        
    i=i+1