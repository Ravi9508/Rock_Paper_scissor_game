user1 =input("Enter Your name: \n")
user2=input("you to enter your name: \n")
u1= input("%s,You Want To Play Rock Paper scissor game : "%  user1)
u2= input("%s,You Want To Play Rock Paper scissor game : "%  user2)
def compare(u1,u2):
    if(u1==u2):
        return("tie")
    elif u1=='rock':
        if u2=='scissor':
            return('rock win!')
        else:
            return('paper win')
    elif u1=="scissor":
        if u2=='paper':
            return("scissor win!")
        else:
            return("rock win!")
    elif u1=='paper':
        if u2=='rock':
            return('paper win')
        else:
            return("sceissor win!")
    else:
       return('You Write a Invaid Code And You Not Enter Rock Paper Scissor,try again')
       sys.exit()     

print(compare(u1,u2))


