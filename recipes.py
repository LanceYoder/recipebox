import random
from fuzzywuzzy import process
from enum import Enum

RECIPE_FILE = r'data.txt'

INTENSITIES = ['Fifteen minutes', 'Thirty minutes', 'Hour', 'Hour plus']

class recipe:
    def __init__(self, name, intensity=None, rating=0, link=None, recipeText=None, ingredients=None):
        self._name = name
        self._intensity = intensity
        self._rating = float(rating)
        self._ingredients = ingredients
        self._link = link
        self._recipeText = recipeText

    def __str__(self):
        retStr = ""
        retStr += "Recipe: " + self._name + '\n'
        retStr += "Intensity: " + self._intensity + '\n'
        retStr += "Rating: " + str(self._rating) + '\n'
        if self._ingredients:
            retStr += "Main Ingredients: " + ", ".join(self._ingredients) + '\n'
        if self._link:
            retStr += "Link: " + self._link + '\n'
        if self._recipeText:
            retStr += "Recipe Instructions:" + '\n'
            retStr += self._recipeText + '\n'

        return retStr

    def printMini(self):
        print("Recipe Name: " + self._name + ", Intensity: " + self._intensity + ", Rating: " + str(self._rating))

    def getName(self):
        return self._name

    def getRating(self):
        return self._rating

    def getIntensity(self):
        return self._intensity

    def getIngredients(self):
        return self._ingredients

    def getLink(self):
        return self._link

    def getRecipeText(self):
        return self._recipeText

    def setName(self, name):
        self._name = name

    def setRating(self, rating):
        self._rating = rating

    def setIntensity(self, intensity):
        self._intensity = intensity

    def setIngredients(self, ingredients):
        self._ingredients = ingredients

    def setLink(self, link):
        self._link = link

    def setRecipeText(self, recipeText):
        self._recipeText = recipeText

allIngredients = set()

recipes = []

def makeLists():
    with open(RECIPE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            bits = line.split('`')
            ingredients = [b.strip() for b in bits[5].strip().split(",")]
            recipes.append(recipe(bits[0].strip(), bits[1].strip(), bits[2].strip(), bits[3].strip(), bits[4].strip(), ingredients=bits[5].strip().split(',')))
            for b in ingredients:
                allIngredients.add(b)

def compRecipe(val):
    return val._rating

def suggestRecipe():

    print("What main ingredient are you looking for? Available ingredients are:")

    for tag in allIngredients:
        print(tag.strip())
    inputTag = input("Enter an ingredient: ")
    print()

    matches = process.extract(inputTag, allIngredients, limit=3)
    while matches[0][1] < 92:
        print("This ingredient doesn't exist. Did you mean: ")
        for m in matches:
            print(m[0])
        inputTag = input("Enter an ingredient: ")
        matches = process.extract(inputTag, allIngredients, limit=3)
        print()
    
    randRec = []
    for rec in recipes:
        if matches[0][0] in rec._ingredients:
            randRec.append(rec)

    print("Do you want all recipes (1), one random suggestion (2), or top recipes (3)?")
    allRec = ''
    while not (allRec == '1' or allRec == '2' or allRec == '3'):
        allRec = input("Enter a number: ")
    print()

    if (allRec == '1'):
        print(inputTag + " recipes: ")
        for rec in randRec:
            rec.printMini()
    elif (allRec == '2'):
        random.shuffle(randRec)
        print("Suggestion: ")
        randRec[0].printMini()
        print()
        print("Would you like to see the full recipe?")
        seeFull = input("Yes? ")
        print()
        if seeFull.lower() == 'yes':
            print(randRec[0])
    elif (allRec == '3'):
        randRec.sort(key=compRecipe, reverse=True)
        for i, rec in enumerate(randRec[:min(3, len(randRec))]):
            print(str(i+1) + ". ",end="")
            rec.printMini()
        print()
        print("Would you like to see a full recipe?")
        whichRec = input("Enter 1, 2, 3, or no: ")
        print()
        while whichRec.isnumeric():
            if whichRec == '1' and len(randRec) > 0:
                print(randRec[0])
            elif whichRec == '2' and len(randRec) > 1:
                print(randRec[1])
            elif whichRec == '3' and len(randRec) > 2:
                print(randRec[2])
            whichRec = input("Show another? Enter 1, 2, 3, or no: ")
            print()

def showRecipe():
    recipeName = input("Enter a recipe name: ").strip()
    print()

    allNames = [rec._name for rec in recipes]
    matches = process.extract(recipeName, allNames, limit=3)
    while matches[0][1] < 92:
        print("This recipe doesn't exist. Did you mean: ")
        for m in matches:
            print(m[0])
        print()
        recipeName = input("Enter recipe name: ").strip()
        print()
        matches = process.extract(recipeName, allNames, limit=3)

    for rec in recipes:
        if rec._name == matches[0][0]:
            break

    print(rec)

def enterRecipe():
    inputName = input("Enter recipe name: ")
    print("Intensity options: " + ", ".join(INTENSITIES))
    inputIntensity = input("Enter an intensity: ")
    inputIntensity = process.extractOne(inputIntensity, INTENSITIES)[0]
    inputRating = None
    while not inputRating:
        try:
            inputRating = float(input("Enter a rating out of 10: "))
        except:
            print("A number, please! Like 7 or 3.5.")
    inputLink = input("Add a link, or press Enter to skip: ").strip()
    inputText = input("Add the text of the recipe, or press Enter to skip: ").strip()
    print("Add ingredients, or press Enter to skip.")
    print("You can add the following ingredients, or a new one:")
    for tag in allIngredients:
        print(tag)
    print("List ingredients with commas and spaces like so: beef, potato, corn")
    inputTags = input("Enter ingredients: ").strip().replace(" ", "").split(',')
    for tag in inputTags:
        if tag.lower() not in allIngredients:
            allIngredients.add(tag)
    newRecipe = recipe(inputName, intensity=inputIntensity, rating=str(inputRating), link=inputLink, recipeText=inputText, ingredients=[",".join(inputTags)])
    print()
    print("Adding " + str(newRecipe))
    print("Is this ok? Enter \'no' to cancel.")
    if input().lower() == 'no':
        return

    with open(RECIPE_FILE, 'a') as file:
        file.write("`".join([inputName, inputIntensity, str(inputRating), inputLink, inputText, ",".join(inputTags)]) + "\n")
    recipes.append(newRecipe)

def planWeekly():
    numDays = int(input("How many days this week? "))
    weeklyRecipes = [] * numDays
    print("List main ingredients to use on a day like so: beef, beef, pork, vegetable, ...")
    print("Available ingredients are: ")
    for tag in allIngredients:
        print(" - " + tag)
    listMains = input("Enter ingredients: ").strip().replace(" ", "").split(',')
    for i, main in enumerate(listMains):
        listMains[i] = process.extractOne(main, allIngredients)
    intensities = input("List desired intensities like so: fifteen minutes, fifteen minutes, thirty minutes, hour, hour plus: ").strip().split(',')
    for i, intensity in enumerate(intensities):
        intensities[i] = process.extractOne(intensity, INTENSITIES)


    recs = filter(lambda rec: [i for i in rec._ingredients if i in listMains], filter(lambda rec: rec._intensity in intensities, random.shuffle(recipes)))

    for i in range(numDays):
        for rec in recs:
            print("How about " + recs.printMini() + "?")
            reject = input("Press Enter to accept, or enter no: ")
            if reject:
                continue
            else:
                weeklyRecipes[i] = rec
                listMains.remove([i for i in rec._intensity if i in listMains][0])
                intensities.remove(rec._intensity)
                recs.remove(rec)
                recs = filter(lambda rec: [i for i in rec._ingredients if i in listMains], filter(lambda rec: rec._intensity in intensities, random.shuffle(recipes)))
                break

    print("done ===========")
    for i in weeklyRecipes:
        print(i)
        print("  --  --  --")


def begin():
    while True:
        print()
        #print("1: Plan a weekly dinner schedule.")
        print("2: Suggest some recipes.")
        print("3: Show me a specific recipe.")
        print("4: Add a recipe.")
        print("5: Exit program.")
        response = input("Enter a number: ")
        print()
        while True:
            #if response == '1':
            #    planWeekly()
            #    break
            if response == '2':
                suggestRecipe()
                break
            elif response == '3':
                showRecipe()
                break
            elif response == '4':
                enterRecipe()
                break
            elif response == '5':
                return
            else:
                response = input("1, 2, or 3, please! ")

if __name__ == "__main__":
    makeLists()
    begin()