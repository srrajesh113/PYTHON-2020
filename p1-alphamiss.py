# Forward search ex: --c- and output will be abc- .
def forwardsearch(me,le,co):
    mp=-1;
    c=0;
    while(c<co):
        if(me[c]=="-"):
            mp=mp+1;
        elif(me[c] in le):
            break;
        c=c+1;
    
    while(mp>=0):
        if(me[mp]=="-"):
            if(me[mp+1] in le):
                pos=le.find(me[mp+1]);
                if(pos==0):
                    me[mp]="@";
                elif(pos>0):
                    me[mp]=le[pos-1];
            elif(me[mp+1]=="@"):
                me[mp]="@";
        mp=mp-1;
    
    return me;
'''backwardsearch for ex: ab--e output is abcde'''
def backwardsearch(f,l):
    m=0;
    pos=0;
    while(m<len(f)):
        if(f[m] =="-"):
            if(f[m-1]!="@"):
                pos=l.find(f[m-1]);
                if(pos<25):
                    f[m]= l[pos+1];
                elif(pos>=25):
                    f[m]= "@";
            elif(f[m-1]=="@"):
                    f[m]="@";
        m+=1;
    return f;

# It display will convert tuple to a string and return.
def display(t):
    trans="";
    for i in t:
        trans+=i;
    return trans;

# Here the main program  input the string,checking for vaildation of string.
k=1;
while(k==1):
    print("This program will find a missing alphabet in a sequence.\n"+
          "The missing alphabet can be represented by '-'.\n");
    message=input("Enter the string:");
    mess=list(message);   # Convert string to list.
    letter="abcdefghijklmnopqrstuvwxyz";
    countms=0;
    for i in mess:   #Count the number of missing letter.
        if(i=="-"):
            countms+=1;
    print("The input string is ",message,"\n");
    print("The number of missing letter is ",countms,"\n");
    if(countms==0):
        print("There is no missing letter\n");
    elif(countms==len(message)):
        print("Missing letter can't be determined\n");
    else:
        fs=forwardsearch(mess,letter,countms);
        ts=backwardsearch(fs,letter);
        final=display(ts);
        state=1;
        lf=len(final);
        for z in range(1,lf-1):  #Check for invaild string like z--abc.
            if(final[0]!="@"and final[z]=="@"):
                if(final[z+1] in letter):
                    state=0;
        for x in range(len(final)):  #Check for invalid string like a--b.
            for y in range(len(final)):
                if(x!=y and final[x]==final[y] and final[x]!="@"):
                    state=0;
        if(state==1):
            print("The final output is ",final+"\n");
        else:
            print("The input string is invalid");
    k=int(input("press 1 to input string \npress 0 to exit :"));
    print("\n");
        
        

