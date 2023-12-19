import random

RECIPE_FILE = r'data.txt'

class recipe:
    def __init__(self, name, rating, tags):
        self._name = name
        self._rating = rating
        self._tags = tags

allTags = set()

recipes = []

def makeLists():
    with open(RECIPE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            bits = line.split(',')
            ingredients = [b.strip() for b in bits[2:]]
            recipes.append(recipe(bits[0].strip(), bits[1].strip(), ingredients))
            for b in ingredients:
                allTags.add(b)

def generateRecipes():
    makeLists()

    print("What ingredient are you looking for?")

    for tag in allTags:
        print(tag.strip())

    inputTag = input()
    while inputTag.lower() not in allTags:
        print("Not an existing tag.")
        print("Enter an ingredient:")
        inputTag = input()
    
    randRec = []
    for rec in recipes:
        if inputTag in rec._tags:
            randRec.append(rec)
    
    random.shuffle(randRec)
    print()
    print("Suggestion:")
    print(randRec[0]._name)
    print("Rating: " + randRec[0]._rating)

def enterRecipe():
    print("Enter recipe name: ")
    inputName = input()
    print("Enter a rating out of 10: ")
    inputRating = None
    while not inputRating:
        try:
            inputRating = int(input())
        except:
            print("A number, please! Like 2.")
    print("Which ingredients would you like to add?")
    print("You can add the following ingredients:")
    for tag in allTags:
        print(tag)
    print("List ingredients with commas and spaces like so: beef, potato, corn")
    inputTags = input().strip().replace(" ", "").split(',')
    for tag in inputTags:
        if tag.lower() not in allTags:
            allTags.add(tag.lower())
    print("Adding " + inputName + " with rating " + str(inputRating) + " and ingredients " + " ".join(inputTags))
    print("Is this ok? Yes or No?")
    ok = input()
    if ok.lower() == 'no':
        return

    with open(RECIPE_FILE, 'a') as file:
        file.write(inputName + "," + str(inputRating) + "," + ",".join(inputTags) + "\n")

def begin():
    print("Enter a number:")
    print("1: Show me some recipes!")
    print("2: Add a recipe.")
    response = input()
    if response == '1':
         generateRecipes()
    elif response == '2':
         enterRecipe()
    else:
        print("1 or 2, please!")
        begin()

if __name__ == "__main__":
    begin()