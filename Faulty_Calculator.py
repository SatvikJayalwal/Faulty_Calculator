import os
os.system("cls")
num1 = int(float(input(" ENTER FIRST NUMBER : ")))
num2 = int(float(input(" ENTER SECOND NUMBER : ")))
ans_inp = input(" ENTER YOUR OPERATION : \n"
                        " A - ADDITION\n"
                        " S - SUBTRACTION\n"
                        " M - MULTIPLICATION\n"
                        " D - DIVISION\n : ")
if (ans_inp == 'a'):
    if(num1== 4 and num2== 6):
        print(" YOUR ANSWER IS : ",12)
    elif(num1!=4 and num2!=6):
        print(" YOUR ANSWER IS : " ,num1+num2)
elif (ans_inp == 's'):
    if(num1== 20 and num2== 10):
        print(" YOUR ANSWER IS : ",7)
    elif(num1!=20 and num2!=10):
        print(" YOUR ANSWER IS : " ,num1-num2)
elif (ans_inp == 'm'):    
    if(num1== 3 and num2== 2):
        print(" YOUR ANSWER IS : ",5)
    elif(num1!=3 and num2!=2):
        print(" YOUR ANSWER IS : " ,num1*num2)
elif (ans_inp == 'd'):
    if(num1== 6 and num2== 2):
        print(" YOUR ANSWER IS : ",5)
    elif(num1!=6 and num2!=2):
        print(" YOUR ANSWER IS : " ,num1/num2)
elif (ans_inp != 'a' or ans_inp != 's' or ans_inp != 'm' or ans_inp != 'd'):
    print("Pls choose from a s m d")
                       