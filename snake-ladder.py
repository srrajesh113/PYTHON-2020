#This program is designed to play snake and ladder for more than 1 player
import random;
# Creating the list1 and list2 to insert the players and position
list1=[];
list2=[];
def checkplayer():
    while(True):
        check=int(input("Enter the number of player more than 1:"));
        if(check>1):
            return check
        else:           
            print("invalid input try again\n")
            
#inputing the number of players
nplayer=checkplayer()
for i in range(1,nplayer+1):            #appending the list1 has player1 and 2 so on...
    playername="player"+str(i);         #appending the list2 has position with 0
    list1.append(playername);
    list2.append(95);
print(list1);
print(list2,"\n");

def checkroll():                         #check valid input is given to roll the dice
    while(True):
        check=str(input(i+": press y to roll the dice"));
        if(check=='y'):
            return 1
        else:           
            print("invalid input try again\n")
    
pos=0;
noofplace=1;
count100=0
wloop=1

while(wloop==1):
    for i in list1:                     #getting each player
        if(list2[pos]!=100):            #check player is not equal to 100
            if(count100==len(list2)-1): #check the no of player got 100 position expect the last player 
                print(i," has won the %i place"%(noofplace),"\n");
                print("thank you for playing the game""\n");
                wloop=5;                #make the while loop false and exit using break
                break
            cr=checkroll()

            if(cr==1):
                ra=random.randrange(1,7);        #choose a number from 1 to 6
                print("The dice value is ",ra);
                list2[pos]=list2[pos]+ra;       #add the choosen number to list2 of current player
                print("%s is in the position:%i"%(i,list2[pos]));

            #condition to climb up the ladder
                if(list2[pos]==8):
                    print("you have climb the ladder and got to 37");
                    list2[pos]=37;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==13):
                    print("you have climb the ladder and got to 46");
                    list2[pos]=46;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==34):
                    print("you have climb the ladder and got to 63");
                    list2[pos]=63;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==50):
                    print("you have climb the ladder and got to 88");
                    list2[pos]=88;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==62):
                    print("you have climb the ladder and got to 95");
                    list2[pos]=95;
                    print("now %s in the position %i"%(i,list2[pos]));
            #condition to climb down from snake bite
                if(list2[pos]==23):
                    print("you have bite by snake and got to 4");
                    list2[pos]=4;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==38):
                    print("you have bite by snake and got to 14");
                    list2[pos]=14;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==73):
                    print("you have bite by snake and got to 55");
                    list2[pos]=55;
                    print("now %s in the position %i"%(i,list2[pos]));
                if(list2[pos]==93):
                    print("you have bite by snake and got to 40");
                    list2[pos]=40;
                    print("now %s in the position %i"%(i,list2[pos]));
            #condition to check player position is 100
                if(list2[pos]==100):
                        print("you reach 100 and won the %i place"%(noofplace));
                        count100=count100+1     #add 1 if the player reaches 100
                        noofplace=noofplace+1;  #keep trace on place won by player like 1st place 
                if(list2[pos]>100):             #if position is more than 100, remain in the previous position
                    print("since ur position is more than 100");
                    list2[pos]-=ra;
                    print("your current position is ",list2[pos]);
                print("\n");
            pos=pos+1;                          #go to next player
            if(pos==len(list2)):                #check the no of player is equal to m,so that it begin the first player
                pos=0;
        else:                                   #if player position is equal 100 then move on to next player 
            pos=pos+1;
            if(pos==len(list2)):
                pos=0;
    
