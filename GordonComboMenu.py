global totalCost
global subtotal
global taxAmount
#the tip function multiplies the subtotal by the tax percentage(%7)
def tax(taxAmount,totalCost):
  taxAmount=.07
  totalCost = totalCost*(1+taxAmount)
  return totalCost
#the tip function allows the user to input a numeric value after the total.   
def tip(totalCost):
    tipAmount=float(input("How much will you tip?: "))
    totalCost = (totalCost+tipAmount)
    return totalCost

#this function triggers when ordering a sandwhich, and asks the user if they want cheese on their sandwhich
def cheeseyn():
  userinput=input("with or Without cheese?")
  print (userinput)
  if userinput=="with":
    print("You ordered the sandwhich with cheese")
    return 0.25
  elif userinput=="without":
    print("You did not order any cheese")
    return 0


def SandwhichCost():
  sandwhichtype=input("What type of sandwhich would you like? ")
  print(sandwhichtype)
  sandwhichtypeList=["kp","ssd","dkp","ftl","gl","tkp","sas","km","dkm","tkm","gl + s"]#list of possible sandwhich types the user could choose
  sandwhichCostList=[1.25,1.25,2,2,2,3,3,3.50,3.75,4,2.50]#the 
  if sandwhichtype in sandwhichtypeList:
      i=sandwhichtypeList.index(sandwhichtype)
      burgertotal=0 #another valid method for the discount
      #total+=sandwhichCostList[i]
      if sandwhichtype not in sandwhichtypeList:
        print("That's not a sandwhich, please look at the menu and try again.")
      if sandwhichtype=="kp":
        pattysize=input("Would you like that in a single,double,or triple size?")
        if pattysize=="single":
            burgertotal+=1.25
        elif pattysize=="double":
            burgertotal+=2.00
        elif pattysize=="triple":
            burgertotal+=3.00
        burgertotal+=cheeseyn()
              
        
      elif sandwhichtype=="km":
        mealsize=input("Would you like that in a single,double,or triple size?")#asks the user what size their sandwhich is
        if mealsize=="single":
            burgertotal+=3.50
        elif mealsize=="double":
          burgertotal+=3.75
        elif mealsize=="triple":
          burgertotal+=4.00
      elif sandwhichtype=="gl":
        sauceyn=input("With or Without Sauce? ")
        if sauceyn=="with":
          burgertotal+=2.50
      else:
        burgertotal+=sandwhichCostList[i]
      print("Your sandwhich costs", burgertotal)
  return burgertotal
#determining the cost of the users drink, if necessary
def beverageCost():
  drinktotal=0
  beverage=0 #######
  if beverage=="yes" or "y":
        beverage=input(" You can choose from a small seafoam soda(sss) for $1.00, a medium seafoam soda(mss) for $1.25, a large seaform soda(lss) for $1.50,or a kelpshake(ks) for $2.00:   " )
        print(beverage)  #print(string,string,string,string)
        beverageList = ["sss","mss","lss","ks"]#list of possible beverage options
        beverageCostList = [1, 1.25, 1.50, 2]#list of possible beverage costs

        drinktotal=0
        if beverage in beverageList:
            i=beverageList.index(beverage)
            drinktotal+=beverageCostList[i]
            print("Your beverage costs",drinktotal)
  elif beverage=="no":
    print("You ordered no beverage")
  return drinktotal

#function determining the cost of the users fries, if they want them
def fryCost():
  frytotal=0
  fries=0
  fries = input("Would you like some small(s) coral bits for $1, medium(m) coral bits for $1.25, or large(l) coral bits for $1.50, or would you like kelp rings(kr) for $1.50, with sauce for $2.00 ")
  if fries=="yes": #size determines cost
      if (fries == "s"):
            frytotal = frytotal + 1
      elif (fries == "m"):
            frytotal = frytotal + 1.25
      elif (fries == "l"):
            frytotal = frytotal + 1.50
      if (fries == "kr"):
        ssauce=input("With or without sauce?") #if an item has a sauce option, ask them yes or no on sauce
      else:
        print("Please input the correct abbreviation.")
        if ssauce=="with":
          frytotal+=2.00
        elif ssauce=="Without":
          print("You did not order sauce")
          frytotal+=1.50
  friesList=["s","m","l","kr"] #list of possible fry sizes
  fryCostList=[1,1.25,1.50,1.50] #list of fry costs
  if fries in friesList:
    i=friesList.index(fries)
    frytotal+=fryCostList[i]
  print("Your side costs",frytotal)
  return frytotal

#the main function that runs through our three order parts and adds them together to form our final cost,subtotal,tax ETC.
def mealorder():
  orderlist=[]
  totalCost=0
  burger=input("Would you like a sandwhich?") 
  if burger=="yes":
    #SandwhichCost()
    sc=SandwhichCost()
    orderlist.append(sc) #adding the selected item to the orderlist
    totalCost+=sc
  drink=input("Would you like a drink?")
  if drink=="yes":
    #beverageCost()
    bc=beverageCost()
    orderlist.append(bc)
    totalCost+=bc
  side=input("Would you like fries with that?") 
  if side=="yes":
    #fryCost()
    fc=fryCost()
    orderlist.append(fc)
    totalCost+=fc
  else:
    print("You did not order anything.")
 
  print("Your subtotal is:",totalCost)
  #totalcost= frycost+beverageCost+fryCost+tax+tip
  taxtotal=tax(.07,totalCost)
  print("Your total after tax is",round(taxtotal,2))
  tiptotal=tip(taxtotal)
  print("Your total after tipping is",round(tiptotal,2))
  print("Your final total is: ",round(tiptotal,2))

  return totalCost
  print(orderlist)
#multiple order option
mealorder()

multipleorder=input("Order again? ")
if multipleorder == "yes" or "y":
    mealorder()
elif mealorder == "no" or "n":
    print("Thanks for visiting the krabby patty!")