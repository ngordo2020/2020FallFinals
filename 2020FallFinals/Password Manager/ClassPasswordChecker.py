"""easyPass=123456
medPass="passw0rd"
hardPass="P@$$w0rd"
goodLuckPass="$jDjiklmp)&4nkIZ3xoicuvyb"""

class PasswordChecker:
    specialCharacters=[33,35,36,37,38,40,41,64,94]
    #             length,,upper,numbers,specials
    reqCheckList=[]
    
   

    '''pointSystem=0
    asciiArtList=["-","-","-","-","-"]              #this is the ascii art. Everyone starts out as a dash because the score starts out as 0
    passwordList=[]
    strengthList=[]'''

    def __init__(self,password):
        self.reqCheckList=[False,False,False,False]
        #print(self.reqCheckList)
        strength=" "
        self.passwordToCheck=password
        #passwordToCheck=input("input a password(If you would like to stop just type in 'stop')... ")       #Ask for the users password
        passwordToCheckLIST=[]              # this is the list that is going to check if it meets all the req.
        #. append() adds items to the list

        #while passwordToCheck!="stop":          #iterates through the whole program over and over until they say stop

        for i in range(len(self.passwordToCheck)):       #to iterate through the for statments
            passwordToCheckLIST.append(False)
        #print(passwordToCheckLIST)

        if(len(self.passwordToCheck)>=8):      #if it meets the length requirement it will go on to check the individual characters
            self.reqCheckList[0]=True
            '''
            if(passwordToCheck.isslnum()):     #checks to see if it has letters and numbers
                print("It needs a special character")
                '''
            #iterating through passwordToCheck
            for i in range(len(self.passwordToCheck)):
                #print(passwordToCheck[i])
                #a-z on ASCII is....... range(97-123)
                #convert letters to numbers with ord() ordiance
                #if(ord(self.passwordToCheck[i]) in range(97,124)):
                # passwordToCheckLIST[i]=True
                    #reqCheckList[1]=True
                #A-Z on ASCII is....... range(65-91)
                if(ord(self.passwordToCheck[i]) in range(65,91)):
                    passwordToCheckLIST[i]=True
                    self.reqCheckList[1]=True
                #0-9 on ASCII is ..... range(48-58)
                elif(ord(self.passwordToCheck[i]) in range(48,59)):
                    passwordToCheckLIST[i]=True
                    self.reqCheckList[2]=True
                elif(ord(self.passwordToCheck[i]) in self.specialCharacters):
                    passwordToCheckLIST[i]=True
                    self.reqCheckList[3]=True
        #print(self.reqCheckList)
    def __str__(self):
        #print(str(self.reqCheckList))
        if False in self.reqCheckList:
            
            return str(False)
        else:
            return str(True)

    '''    #these if statements are to check if the certain index of the list is true then it will add 1 to the point system because that means that it passed that requirement
    if reqCheckList[0]==True:
        pointSystem+=1
        asciiArtList[0]="#"             #if this requirment was done it will change the index in the ascii art to a # which is a point
    if reqCheckList[1]==True:
        pointSystem+=1
        asciiArtList[1]="#"
    if reqCheckList[2]==True:
        pointSystem+=1
        asciiArtList[2]="#"
    if reqCheckList[3]==True:
        pointSystem+=1
        asciiArtList[3]="#"
    if reqCheckList[4]==True:
        pointSystem+=1
        asciiArtList[4]="#"'''




    #print(passwordToCheckLIST)
    #print(reqCheckList)
    #print(pointSystem)
    '''
        if((False in passwordToCheckLIST or False in reqCheckList)):     #if there is a false in the list that means it didn't pass a requirement so it will print out that you did not meet all requirements
            print("Your password did not meet the requirements")
        else:
            print("Your password met the requirements")     #if the list has all true's in it then it will print this out

        #the .join prints out the list without the brackets and commas on one line
        print(pointSystem,"out of 5 points  ","(", ( ' '.join(asciiArtList)), ")")      #https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row 

        passwordList.append(passwordToCheck)    #this puts every password they put in no matter if it works or not into the list
        strengthList.append(' '.join(asciiArtList))     #this puts what the ascii art strength was into the list


        passwordToCheck=input("input a password(If you would like to stop just type in 'stop')... ")

    '''    

'''

    #this resets everything back to the beginning 
    reqCheckList=[False,False,False,False,False]
    pointSystem=0
    asciiArtList=["-","-","-","-","-"]
    passwordToCheckLIST=[] 


    
    #once the user types in stop it will print out these things.
    for i in range(len(passwordList)):  #this prints out everything in the length of the list
        print("Password: ",passwordList[i],"Strength ",strengthList[i]) #this wil print each password with its ascii art side by side

    



    if(not(False in passwordToCheckLIST)):
        print("Password met the requirments")
    '''