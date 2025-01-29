#Add csv
import csv

#add the items of the csv file into a list

def fileLister(file):
    with open(file) as f:
        r=csv.reader(f)
        l=[]
        for i in r:
            l.append(i)
            
    return l


def ingredientInv():
    while True:    
        #Declare the stockList to have all the values of stock.csv file
        stockList=fileLister("stock.csv")
        
        
        #Menu to select what happens with the inventory of ingredients by the user
        print("1‣ View Ingredients\n2‣ Add New Ingredients\n3‣ Edit Ingredients\n4‣ Buy Shopping List\n5‣ Exit")
        try:
            choice=int(input(">>> "))
        except:
            print("Enter a number..")
        
        #Show the user the ingredients and their amounts
        if choice==1:
            for i in stockList:
                print(i[0]," : ",i[1])
                
            #Ask whether the user wants to view the menu again so the menu doesn't block
            #the ingredients list, it's value doesn't matter
            btMenu=input("Back to Menu?")
            
        #Add a new ingredient that is not on the list already
        if choice==2:
            ingredient=input("Enter the new ingredient⥽ ")
            ingredient=ingredient.lower()
            #check whether the ingredient exists within the csv file
            ingExist=False
            
            for i in stockList:
                if ingredient == i[0]:
                    ingExist=True
            
            #only allow the entry of new ingredients if the ingredient doesn't already exist
            if ingExist==False:
                amount=int(input("Enter the amount⥽ "))
                
                #append the ingredient to the csv file
                with open("stock.csv","a",newline="\n") as stockCsv:
                    stockWriter=csv.writer(stockCsv)
                    stockWriter.writerow([ingredient,amount])
            else:
                print("Ingredient already exists!")
        
        #Edit a pre-existing ingredient to change its amount
        if choice==3:
            ingredient=input("Enter ingredient name⥽ ")
            ingredient=ingredient.lower()
            #check whether the ingredient exists within the csv file
            ingExist=False
            for i in stockList:
                if ingredient == i[0]:
                    ingExist=True
                    print(i[0]," : ",i[1])
                    amount=int(i[1])
                    
            if ingExist==False:
                print("Ingredient doesn't exist!")
            else:
                #check whether the user wants to add/subtract/set the value of the amount
                newAmount=input("Enter an amount to incemenet\n(+Number) to add\n(-Number) to subtract\n(no sign) to set its value\n-->")
                
                with open("stock.csv","w",newline="") as stockCsv:
                    stockWriter=csv.writer(stockCsv)
                    
                    #check if the user wants to add
                    if newAmount[0] == "+":   
                        for i in range(len(stockList)):
                            if ingredient == stockList[i][0]:
                                addAmount=int(newAmount[1:])
                                stockList[i]=[ingredient,amount+addAmount]
                    #check if the user wants to subtract
                    elif newAmount[0] == "-":   
                        for i in range(len(stockList)):
                            if ingredient == stockList[i][0]:
                                addAmount=int(newAmount[1:])
                                
                                #prevents the ingredients to be negative
                                if addAmount>amount:
                                    addAmount=amount
                                stockList[i]=[ingredient,amount-addAmount]
                    #check if the user wants to set
                    else: 
                        for i in range(len(stockList)):
                            if ingredient == stockList[i][0]:
                                #prevents the ingredients to be negative
                                if newAmount<0:
                                    newAmount=0
                                stockList[i]=[ingredient,newAmount]
                                
                                
                    #overwrite the csv file to edit the value(if it works, it works)
                    stockWriter.writerows(stockList)
        
        #If user selected to buy the shopping list from the shoppingList file
        if choice==4:
            
            #make the list of a shopping list from the csv file
            shlList=fileLister("shoppingList.csv")
                        
            newStockList=[]
            for i in stockList:
                newStockList.append(i)
            
            #used to add pre-existing items into the stock
            for i in range(len(stockList)):
                for j in shlList:
                    if stockList[i][0]==j[0]:
                        newStockItem=int(newStockList[i][1])
                        newStockItem+=int(j[1])
                        newStockList[i][1]=newStockItem
            
            #used to add new items if they don't exist in the stock
            
            ingiNames=[]
            
            for i in stockList:
                ingiNames.append(i[0])
            
            for i in shlList:
                if i[0] not in ingiNames:
                    newStockList.append([i[0],i[1]])
            
                
            #update the stock to add the new items
            with open("stock.csv","w",newline="") as stockCsv:
                writer=csv.writer(stockCsv)
                writer.writerows(newStockList)
            
            #delete the shopping list once everything has been bought
            with open("shoppingList.csv","w",newline="") as shlCsv:
                print("Added new Items to Shopping List!")
                
                
        ret=0
                        
        #exit the menu   
        if choice==5:
            print("⥏ Exited Ingredients Menu ⥑")
            return ret

def dishesMenu():
    while True:
        
        #Store the data of the stock of ingredients
        stockList=fileLister("stock.csv")
        #Store data of recipe of dishes
        dishesList=fileLister("dishes.csv")
        
        #Let user select the option they want to make
        print("1‣ View All Dishes\n2‣ Make Dish\n3‣ Add New Dish\n4‣ View Shopping List\n5‣ Exit")
        
        try:
            choice=int(input(">>> "))
        except:
            print("Enter a number..")

        
        if choice==1:
            
            #choose a dish from the catalogue for the recipe
            print("Choose A Dish > ")
            dishNameList=[]
            for i in dishesList:
                print("‣",i[0])
                dishNameList.append(i[0])
            
            selectDish=input("Enter the name of the dish⥽ ")
            selectDish=selectDish.lower()
            
            #display list of all the dishes for the user to choose from
            if selectDish in dishNameList:
                for i in range(len(dishesList)):
                    if selectDish==dishesList[i][0]:
                        print(selectDish,"⭆ ")
                        for j in eval(dishesList[i][1]):
                            print("  ",j[0]," : ",j[1])
            else:
                print("Dish does not exist")
            

            btMenu=input("Back to Menu?")
            
        #select a dish for the user to make to reduce the ingredients in the stock
        if choice==2:
            print("Choose A Dish > ")
            dishNameList=[]
            for i in dishesList:
                print("‣",i[0])
                dishNameList.append(i[0])
            dishName=input("Enter the name of the dish⥽ ")
            dishName=dishName.lower()
            ingredientList=[]
            if dishName in dishNameList:
                #check the availability of the ingredients
                
                #get list of available ingredients
                stockList=fileLister("stock.csv")
                
                #make a list of all ingredients in the dish
                for i in range(len(dishesList)):
                    if dishName == dishesList[i][0]:
                        for j in eval(dishesList[i][1]):
                            ingredientList.append(j)
                
                #make list of missing ingredients
                ingCheckList=[]
                for i in ingredientList:
                    ingCheckList.append(i)
                    
                moreCheckList=[]
                
                #flag var to check if dish is possible
                possible=True
                
                #check for ingredients that exist but is not enough
                for i in ingredientList:
                    for j in stockList:
                        if i[0] == j[0]:
                            if int(i[1]) > int(j[1]):
                                print("Not enough", j[0], "need", int(i[1]) - int(j[1]), "more!")
                                moreCheckList.append([i[0], int(i[1]) - int(j[1])])
                                possible = False
                            if i in ingCheckList:
                                ingCheckList.remove(i)
                            
                #check for ingredient that don't exist in stock
                for i in ingCheckList:
                    print("There is no", i[0], "in the stock!")
                    possible = False
                
                if possible == False:
                    #ask whether these items need to be added a shopping list or not
                    sListBool = input("Add These Items to Shopping List?(y/n)⥽ ")
                    sList=[]
                
                #adds missing items in the dish to the shopping list
                    if sListBool=="y":
                        for i in ingCheckList:
                            sList.append(i)
                        for i in moreCheckList:
                            sList.append(i)
                #write the shopping list to a csv file for later access
                        with open("shoppingList.csv","a",newline="\n") as shListFile:
                            writer=csv.writer(shListFile)
                            writer.writerows(sList)
                            print("Added items to shopping List")
                        
                    

                    
                #IF the dish is possible to create
                if possible==True:
                    
                    for i in range(len(stockList)):
                        for j in ingredientList:
                            if stockList[i][0]==j[0]:
                                stockList[i]=[stockList[i][0],int(stockList[i][1])-j[1]]
                            
                    
                    print("Dish Successfully created!")
                    with open("stock.csv","w",newline="") as stockCsv:
                        writer=csv.writer(stockCsv)
                        writer.writerows(stockList)
                        
                        
        #Allows users to add a new dish with its ingredients
        if choice==3:
            try:
                ingAmount=int(input("Enter amount of ingredients⥽ "))
            except:
                print("Enter a number..")
                continue
            ingredientList=[]
            for i in range(ingAmount):
                ingredient=input("Enter an ingredient⥽ ")
                ingredient=ingredient.lower()
                amount=int(input("Enter ingredient amount⥽ "))
                #prevent amount of an ingredient to be 0 or negative
                if amount<1:
                    amount=1
                ingredientList.append([ingredient,amount])
            dishName=input("Enter name of dish⥽ ")
            dishName=dishName.lower()
                
            with open("dishes.csv","a",newline="\n") as dishesCsv:
                writer=csv.writer(dishesCsv)
                writer.writerow([dishName,ingredientList])
                print("Dish Successfully Added!")
            
        #if the user has selected to view the shopping list
        if choice==4:
            with open("shoppingList.csv") as slCsv:
                reader=csv.reader(slCsv)
                for i in reader:
                    print(i[0]," : ",i[1])
                    
            #btmenu to show the list of items properly without the menu
            btMenu=input("Back To Menu?")
        
        ret=0
        #exit to main menu
        if choice==5:
            print("⥏ Exited Dishes Menu ⥑")
            return ret
        
        #add shameless self-insertion to let others know that you wrote this code.
        '''I understand that using dict is better than lists but I figured that out
            when I had already started working on this project and I am not changing
            it to dict'''
        if choice==26:
            print("by Akj.")

while True:
    #Main Menu
    print("Choose a menu⭆\n1‣ Ingredients Menu\n2‣ Dishes Menu\n3‣ Exit")
    
    try:
        mode=int(input(">>> "))
        
    except:
        print("Enter a valid no.")
        mode=0
#If user has selected to view ingredients
    if mode==1:
        ingredientInv()
        
#If user has selected to make a dish
    if mode==2:
        dishesMenu()
        
    #If user has selected to leave
    if mode==3:
        print("Shutting Down..")
        break
