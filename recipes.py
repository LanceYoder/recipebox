import random
from fuzzywuzzy import process

RECIPE_FILE = r'data.txt'

class recipe:
    def __init__(self, name, rating=0, link=None, recipeText=None, ingredients=None):
        self._name = name
        self._rating = float(rating)
        self._ingredients = ingredients
        self._link = link
        self._recipeText = recipeText

    def __str__(self):
        retStr = ""
        retStr += "Recipe: " + self._name + '\n'
        retStr += "Rating: " + str(self._rating) + '\n'
        if self._ingredients:
            retStr += "Ingredients: " + ", ".join(self._ingredients) + '\n'
        if self._link:
            retStr += "Link: " + self._link + '\n'
        if self._recipeText:
            retStr += "Recipe Instructions:" + '\n'
            retStr += self._recipeText + '\n'

        return retStr

allIngredients = set()

recipes = []

def makeLists():
    with open(RECIPE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            bits = line.split(',')
            ingredients = [b.strip() for b in bits[2:]]
            recipes.append(recipe(bits[0].strip(), bits[1].strip(), ingredients=ingredients))
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
        inputTag = input("Enter an ingredient:")
        matches = process.extract(inputTag, allIngredients, limit=3)
        print()
    
    randRec = []
    for rec in recipes:
        if matches[0][0] in rec._ingredients:
            randRec.append(rec)

    print("Do you want all recipes (enter 1), one random suggestion (enter 2), or top recipes (enter 3)?")
    allRec = input("Enter a number: ")
    print()

    if (allRec == '1'):
        print(inputTag + " recipes:")
        for rec in randRec:
            print(rec._name + ", rating: " + str(rec._rating))

    elif (allRec == '2'):
        random.shuffle(randRec)
        print("Suggestion:")
        print(randRec[0]._name)
        print("Rating: " + str(randRec[0]._rating))
    elif (allRec == '3'):
        randRec.sort(key=compRecipe, reverse=True)
        for i, rec in enumerate(randRec[:min(3, len(randRec))]):
            print(str(i+1) + ": " + rec._name + ", rating: " + str(rec._rating))

    begin()

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

    begin()

def enterRecipe():
    inputName = input("Enter recipe name: ")
    inputRating = None
    while not inputRating:
        try:
            inputRating = int(input("Enter a rating out of 10: "))
        except:
            print("A number, please! Like 2.")
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
    newRecipe = recipe(inputName, str(inputRating), link=inputLink, recipeText=inputText, ingredients=[",".join(inputTags)])
    print("Adding " + str(newRecipe))
    print("Is this ok? Enter \'no' to cancel.")
    if input().lower() == 'no':
        return

    with open(RECIPE_FILE, 'a') as file:
        file.write(inputName + "," + str(inputRating) + "," + ",".join(inputTags) + "\n")
    recipes.append(newRecipe)

    begin()

def begin():
    print()
    print("1: Suggest some recipes.")
    print("2: Show me a specific recipe.")
    print("3: Add a recipe.")
    print("4: Exit program.")
    response = input("Enter a number: ")
    print()
    if response == '1':
        suggestRecipe()
    elif response == '2':
        showRecipe()
    elif response == '3':
        enterRecipe()
    elif response == '4':
        return
    else:
        print("1, 2, or 3, please!")
        begin()

if __name__ == "__main__":
    makeLists()
    begin()