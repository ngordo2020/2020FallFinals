
import random 
class PasswordGenerator:
    
    '''
    number=int(input("How many random integers would you like to print out? "))
    for i in range(number):
        print(i)
        password+=str(i)
    print(password)
        '''
    def __init__(self):
        self.password=""
        self.number=3
        self.capLetters=2
        self.lowLetters=3
        self.special=3
        for i in range(self.capLetters):          #range(start,stop,step)
            self.password+=chr(random.randint(65,90))        #pulls a random uppercase letter
        for i in range(self.number):
            self.password+=str(random.randint(0,9))      #pulls a random number 1-9
        for i in range(self.lowLetters):
            self.password+=chr(random.randint(97,122))           #pulls a random lowercase letter
        for i in range(self.special):
            self.password+=chr(random.randint(33,47))           #pulls random special charaters

        self.scramble=""    
        for i in range(len(self.password)):
            r=random.randint(0,len(self.password)-1)
            self.scramble+=self.password[r]       #mixes the password together
            self.password=self.password.replace(self.password[r],"",1)
    
    def __str__(self):
        return(self.scramble)
    #print(password)
    #print(scramble)
