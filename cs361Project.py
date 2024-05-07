import json

def startScreen():
    print("Welcome, trainer!")
    print("This program will guide you through picking your starter Pokemon.")
    print('When you are ready, enter "start" into the box below')
    print('Entering "start" into the user input will take you to the next part of the program, where you will choose a type')
    getStarted=input('Type "start" here to get started! ->')
    return getStarted

def chooseType():
    print("Here, you will choose the type for your starter Pokemon.")
    print("Your options are grass, fire, or water")
    print('To choose the type for your starter, type "grass", "water", or "fire" into the input box below.')
    print('If you want to go back to the start screen, type "return to start" into the input box.')
    typeChoice=input('Enter your choice of type here! (Your options are "grass", "water", or "fire", or you can type "return to start" to go back to the previous page) ->')
    
def chooseRegion():
    print("Here, you will choose the region for your starter Pokemon")
    print("Your options are Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, Alola, Galar, or Paldea.")
    print('To choose the type for your starter, type "Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos", "Alola", "Galar", or "Paldea" into the input box below.')
    print('If you want to go back to the start screen, type "return to start" into the input box.')
    print('If you want to go back to the type selection screen, type "return to types" into the input box.') 
    regionChoice=input('Enter your choice of region here! (Your options are "Kanto", "Johto", "Hoenn", "Sinnoh", "Unova", "Kalos", "Alola", "Galar", or "Paldea", or you can type "return to start" to return to start again from the beginning or "return to types" to return to the previous page.) ->')
    
def errorMessage():
    print("Sorry! That is not a valid input.")
    
def useProgram():
    While True:
        getStarted=startScreen()
        if getStarted == 'start':
            typeChoice=chooseType()
        
'''Each type will have its own region list, going in chronological order for easy edits and additions'''
        
            #grass type list
            if typeChoice == "grass":
                regionChoice=chooseRegion()
                if regionChoice == "Kanto":
                    print("Bulbasaur")
                elif regionChoice == "Johto":
                    print("Chikorita")
                else:
                    errorMessage()
        
            #water type list
            elif typeChoice == "water":
                if regionChoice == "Kanto":
                    print("Squirtle")
                elif regionChoice == "Johto":
                    print("Totodile")
                else:
                    errorMessage()
        
            #fire type list
            elif typeChoice == "fire":
                if regionChoice == "Kanto":
                    print("Charmander")
                elif regionChoice == "Johto":
                    print("Cyndaquil")
                else:
                    errorMessage()
                    
            elif typeChoice == "return to start":
                #clear data and return to start screen
                
            else:
                errorMessage()
        else:
            errorMessage()
    
