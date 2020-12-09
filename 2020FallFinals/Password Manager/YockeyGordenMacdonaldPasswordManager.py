from ClassPasswordChecker import PasswordChecker
from PasswordGenerator import PasswordGenerator



password=input("Please enter the master password then if you don't know a password then type 'create' ")
if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
    while password!="create":
        pc=PasswordChecker(password)
        if "False" in str(pc):
            print("That password does not meet the requirements")
            password=input("Please enter the password then if you don't know a password then type 'create' ")
        else:       #if the password meets the requirements then it will append it to the list
            password=password
            break
userName=input("Enter your username ")
passWordUI=input("Enter the password ")
passwordTries=0
            #[[what it's for][username][password]]
homePasswords=[[],[],[]]
workPasswords=[[],[],[]]
entertainmentPasswords=[[],[],[]]
billsPasswords=[[],[],[]]
randomPasswords=[[],[],[]]
userCata=[[],[],[]]     #this is the catagory that the user makes
masterPasswords=[homePasswords,workPasswords,entertainmentPasswords,billsPasswords,randomPasswords]
#bander said to have 3 lists inside the home, work, etc ones. Example: homePasswords=[[what the password is for],[usernames],[passwords]]

#make the password generator a function     possibly a class but ask bander 

#make the password checker a class too 



PasswordChecker(password)               #this is the password checker as a class 




while passwordTries!=5:     #will let the user enter the password 5 times. if they don't get it in 5 the file will stop. If they enter the right password it will start the program
    if passWordUI!=password:
        passwordTries+=1
        passWordUI=input("Enter the password\n")
    else:       #if password is right then it will start the program
        cata=input("The preset catagories are home, work, entertainment, bills, and random. What catagory would you like to add?\n")
        ui=input(f"What kind of password do you want to store: home, work, entertainment, bills, random, or {cata}. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit'. If you would like to delete type 'delete'\n").lower()
        
        while ui!="done":       #this keeps the program running until the user types done
            if ui==cata:        #if the user wants to put passwords in the home section it will ask for what the password is for, the username,and the password and append that all to the home list
                reason=input("What is this password for? \n")
                userCata[0].append(reason)
                username=input("What is the user name for it?\n")
                userCata[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:               #if the password meets the requirements then it will append it to the list
                            userCata[2].append(password)
                            print(homePasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    userCata[2].append(pg.__str__())
                    print(userCata)
                

            if ui==("home"):        #if the user wants to put passwords in the home section it will ask for what the password is for, the username,and the password and append that all to the home list
                reason=input("What is this password for?\n")
                homePasswords[0].append(reason)
                username=input("What is the user name for it?\n")
                homePasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:               #if the password meets the requirements then it will append it to the list
                            homePasswords[2].append(password)
                            print(homePasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    homePasswords[2].append(pg.__str__())
                    print(homePasswords)
                #it will then ask where they want to store another password to keep the program running until they say done
                
            elif ui=="work":            #if the user wants to put passwords in the work section it will ask for what the password is for, the username,and the password and append that all to the work list
                reason=input("What is this password for?\n")
                workPasswords[0].append(reason)
                username=input("What is the user name for it? \n")
                workPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:       #if the password meets the requirements then it will append it to the list
                            workPasswords[2].append(password)
                            print(workPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    workPasswords[2].append(pg.__str__())
                    print(workPasswords)
                
            elif ui=="entertainment":       #if the user wants to put passwords in the entertainment section it will ask for what the password is for, the username,and the password and append that all to the entertainment list
                reason=input("What is this password for? \n")
                entertainmentPasswords[0].append(reason)
                username=input("What is the user name for it? \n")
                entertainmentPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:       #if the password meets the requirements then it will append it to the list
                            entertainmentPasswords[2].append(password)
                            print(entertainmentPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    entertainmentPasswords[2].append(pg.__str__())
                    print(entertainmentPasswords)
                
            elif ui=="bills":               #if the user wants to put passwords in the bills section it will ask for what the password is for, the username,and the password and append that all to the bills list
                reason=input("What is this password for?\n")
                billsPasswords[0].append(reason)
                username=input("What is the user name for it?\n")
                billsPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                    while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:       #if the password meets the requirements then it will append it to the list
                            billsPasswords[2].append(password)
                            print(billsPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    billsPasswords[2].append(pg.__str__())
                    print(billsPasswords)
                
            elif ui=="random":              #if the user wants to put passwords in the random section it will ask for what the password is for, the username,and the password and append that all to the random list
                reason=input("What is this password for?\n")
                randomPasswords[0].append(reason)
                username=input("What is the user name for it?\n")
                randomPasswords[1].append(username)
                password=input("Please enter the password then if you don't know a password then type 'create'\n")
                if password!="create":      #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                     while password!="create":
                        pc=PasswordChecker(password)
                        if "False" in str(pc):
                            print("That password does not meet the requirements\n")
                            password=input("Please enter the password then if you don't know a password then type 'create'\n")
                        else:       #if the password meets the requirements then it will append it to the list
                            randomPasswords[2].append(password)
                            print(randomPasswords)
                            break
                else:       #if the user puts create then it will call the password generator class and append the random password to the list
                    pg=PasswordGenerator()
                    randomPasswords[2].append(pg.__str__())
                    print(randomPasswords)
                
            elif ui=="print":
                print("\t Username:",userName)
                print("\t Home Passwords:")
                print("For What:\t Username:\t Password:")
                for i in range(len(homePasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(homePasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(homePasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Work Passwords:")
                for i in range(len(workPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(workPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(workPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Entertainment Passwords:")
                for i in range(len(entertainmentPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(entertainmentPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(entertainmentPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Bills Passwords:")
                for i in range(len(billsPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(billsPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(billsPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\t Random Passwords:")
                for i in range(len(randomPasswords[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(randomPasswords)):    #this will grab 3 because there is 3 lists in each one
                        print(randomPasswords[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print(f"\t {cata} Passwords:")
                for i in range(len(userCata[0])):      #this will grab the length of the first list in the home passwords list and see how many there are 
                    for j in range (len(userCata)):    #this will grab 3 because there is 3 lists in each one
                        print(userCata[j][i],end="\t\t") #this will print the first item in every list and then print a new line and go through this cycle for as many items are in the list
                    print()
                print("\n")
    
            elif ui=="edit":
                editUI=input("What is the password for that you would like to change? If you are done editing type 'n'\n")
                while editUI!="n":
                    if editUI in homePasswords[0]:
                        ind=homePasswords[0].index(editUI)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    homePasswords[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            homePasswords[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    elif editUI in workPasswords[0]:
                        ind=workPasswords[0].index(editUI)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    workPasswords[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            workPasswords[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    elif editUI in entertainmentPasswords[0]:
                        ind=entertainmentPasswords[0].index(editUI)
                        print(ind)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    entertainmentPasswords[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            entertainmentPasswords[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    elif editUI in billsPasswords[0]:
                        ind=billsPasswords[0].index(editUI)
                        print(ind)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    billsPasswords[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            billsPasswords[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    elif editUI in randomPasswords[0]:
                        ind=randomPasswords[0].index(editUI)
                        print(ind)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    randomPasswords[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            randomPasswords[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    elif editUI in userCata[0]:
                        ind=userCata[0].index(editUI)
                        print(ind)
                        newPass=input("What would you like to change the password to...If you want another random one type 'create'\n")      
                        while newPass!="create":    #if the user has their own password it will go through the password checker and if it doesn't meet the requirements then it will ask for a password again or they have the option of doing a random password
                                pc=PasswordChecker(newPass)
                                if "False" in str(pc):
                                    print("That password does not meet the requirements\n")
                                    newPass=input("Please enter the password then if you don't know a password then type 'create'\n")
                                else:       #if the password meets the requirements then it will append it to the list
                                    userCata[2][ind]=newPass
                                    break
                        if newPass=="create":       #if the user puts create then it will call the password generator class and append the random password to the list
                            pg=PasswordGenerator()
                            userCata[2][ind]=(pg.__str__())
                        print(f"Your {editUI} password has been changed\n")
                    else:
                        print("You do not have a password for that account\n")
                    editUI=input("What is the password for that you would like to change? If you are done editing type 'n'\n")
            elif ui=="delete":
                deleteUI=input("What is the password for that you would like to delete? If you don't want to delete anything else type 'n'\n")
                while deleteUI!="n":
                    if deleteUI in homePasswords[0]:
                        ind=homePasswords[0].index(deleteUI)
                        del homePasswords[0][ind]
                        del homePasswords[1][ind]
                        del homePasswords[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    elif deleteUI in workPasswords[0]:
                        ind=workPasswords[0].index(deleteUI)
                        del workPasswords[0][ind]
                        del workPasswords[1][ind]
                        del workPasswords[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    elif deleteUI in entertainmentPasswords[0]:
                        ind=entertainmentPasswords[0].index(deleteUI)
                        del entertainmentPasswords[0][ind]
                        del entertainmentPasswords[1][ind]
                        del entertainmentPasswords[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    elif deleteUI in billsPasswords[0]:
                        ind=billsPasswords[0].index(deleteUI)
                        del billsPasswords[0][ind]
                        del billsPasswords[1][ind]
                        del billsPasswords[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    elif deleteUI in randomPasswords[0]:
                        ind=randomPasswords[0].index(deleteUI)
                        del randomPasswords[0][ind]
                        del randomPasswords[1][ind]
                        del randomPasswords[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    elif deleteUI in userCata[0]:
                        ind=userCata[0].index(deleteUI)
                        del userCata[0][ind]
                        del userCata[1][ind]
                        del userCata[2][ind]
                        print(f"Your {deleteUI} has been deleted along with its username and password\n")
                        
                    else:
                        print("You do not have a password for that account\n") 

                    deleteUI=input("What is the password for that you would like to delete? If you don't want to delete anything else type 'n'\n")                
                        
                


                    #homePasswords[2][ind]=newPass 
                    #print(homePasswords[2][ind])
                    #print(homePasswords)
                


            else:       #if they didn't type in one of the categories then it will tell them that and ask again
                print("That wasn't one of the choices\n")
                
            ui=input(f"What kind of password do you want to store: home, work, entertainment, bills, random, or {cata}. If you are done type 'done'. If you would like to print out your passwords type 'print'. If you would like to edit type 'edit'. If you would like to delete type 'delete'\n").lower()
        if ui=="done":          #if the user is done it will break the loop and set the passwordTries to 5 which will break the first while loop and end the whole program
            passwordTries=5        



