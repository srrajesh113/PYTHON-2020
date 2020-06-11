# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:17:36 2020

@author: RAJESH KUMAR N
"""

def playgame():
    lists=["player1 for (x)","player2 for (o)"]
    line1=[".",".","."]
    line2=[".",".","."]
    line3=[".",".","."]
    
    print('\t',line1[0],'\t',line1[1],'\t',line1[2],'\n')
    print('\t',line2[0],'\t',line2[1],'\t',line2[2],'\n')
    print('\t',line3[0],'\t',line3[1],'\t',line3[2],'\n')
    
    count=0
    game=1
    while(game==1):
        for i in lists:
            count=count+1;
            if(count==10):
                print("GAME OVER")
                game=0
                break
              
            checkpos=1
            while(checkpos==1):
                pos=input("enter the position from(1-9) %s:"%(i))
                print("\n")
                p=int(pos)
                if(p<1 or p>9):
                    print("invaild position")
                    checkpos=1
                elif(p>=1 and p<=3 and line1[p-1]!="." or p>=4 and p<=6 and line2[p-4]!="." or p>=7 and p<=9 and line3[p-7]!="."):
                    print("you can't add")
                    checkpos=1
                else:
                    checkpos=0
            
            
            p=p-1
            if(i=="player1 for (x)"):
                if(p>=0 and p<=2):
                    line1[p]="x"
                if(p>=3 and p<=5):
                    p=p-3
                    line2[p]="x"
                if(p>=6 and p<=8):
                    p=p-6
                    line3[p]="x"
                if(line1[0]=="x" and line1[1]=="x" and line1[2]=="x" or
                   line2[0]=="x" and line2[1]=="x" and line2[2]=="x" or
                   line3[0]=="x" and line3[1]=="x" and line3[2]=="x" or
                   line1[0]=="x" and line2[0]=="x" and line3[0]=="x" or
                   line1[1]=="x" and line2[1]=="x" and line3[1]=="x" or
                   line1[2]=="x" and line2[2]=="x" and line3[2]=="x" or
                   line1[0]=="x" and line2[1]=="x" and line3[2]=="x" or
                   line3[0]=="x" and line2[1]=="x" and line1[2]=="x"
                   ):
                    print('\t',line1[0],'\t',line1[1],'\t',line1[2],'\n')
                    print('\t',line2[0],'\t',line2[1],'\t',line2[2],'\n')
                    print('\t',line3[0],'\t',line3[1],'\t',line3[2],'\n')
                    print("player1 won the game")
                    game=0
                    break
                 
            elif(i=="player2 for (o)"):
                if(p>=0 and p<=2):
                    line1[p]="o"
                if(p>=3 and p<=5):
                    p=p-3
                    line2[p]="o"
                if(p>=6 and p<=8):
                    p=p-6
                    line3[p]="o"
                if(line1[0]=="o" and line1[1]=="o" and line1[2]=="o" or
                   line2[0]=="o" and line2[1]=="o" and line2[2]=="o" or
                   line3[0]=="o" and line3[1]=="o" and line3[2]=="o" or
                   line1[0]=="o" and line2[0]=="o" and line3[0]=="o" or
                   line1[1]=="o" and line2[1]=="o" and line3[1]=="o" or
                   line1[2]=="o" and line2[2]=="o" and line3[2]=="o" or
                   line1[0]=="o" and line2[1]=="o" and line3[2]=="o" or
                   line3[0]=="o" and line2[1]=="o" and line1[2]=="o"
                   ):
                    print('\t',line1[0],'\t',line1[1],'\t',line1[2],'\n')
                    print('\t',line2[0],'\t',line2[1],'\t',line2[2],'\n')
                    print('\t',line3[0],'\t',line3[1],'\t',line3[2],'\n')
                    print("player2 won the game")
                    game=0
                    break
                
                 
                
            print('\t',line1[0],'\t',line1[1],'\t',line1[2],'\n')
            print('\t',line2[0],'\t',line2[1],'\t',line2[2],'\n')
            print('\t',line3[0],'\t',line3[1],'\t',line3[2],'\n')
          
playgame()
