import time
print("Lets play Madlibs!")
print("We have 3 different stories to tell.")
choice = int(input("Would you like story 1 about a weird creature, story 2 about , or story 3 about ? "))

if choice == 1:
    print("Time to add your words to the story!")
    time.sleep(1)
    adj1 = input("Please enter an adjective: ")
    adj2 = input("Please enter an adjective: ")
    creature = input("Please enter a type of animal or creature, real or mystical: ")
    verb1 = input("Please enter a verb ending in -ing: ")
    adj3 = input("Please enter an emotion adjective: ")
    name = input("Please enter a name: ")
    adj4 = input("Please enter an adjective: ")
    noun = input("Please enter a type of animal or creature, real or mystical: ")
    verb2 = input("Please enter a past tense verb: ")
    food = input("Please enter a type of food: ")
    drink = input("Please enter a type of drink: ")
    exclaim = input("Please enter an exclamation: ")
    verb3 = input("Please enter a verb ending in -ing: ")
    weapon = input("Please enter a type of weapon: ")

    story1 = "Once upon a time, there was a village. In that village lived a " + adj1 + ", " + adj2 + " " + creature +  ".\n \
    They were always " + verb1 + " around town, making everyone else " + adj3 + ". But one day, someone new came into the village named " +  name +".\n \
    They were a " + adj4 + " " + noun + " . They had enough of the " + creature + " and were there to vanquish it. " + name + " took out their " +  weapon + ", \n \
    " + verb2 + " up to the " + creature + " and attacked! As soon as the " + creature + " was hit, it started bursting from the inside out. \n \
    It was so odd! Chunks of " + food + " were flying out of the body, and instead of blood, " + drink + " was pouring from the wound. The crowd \n \
    that had been gathering gasped. They had never seen such a thing before. Then, the crowd started cheering, saying " + exclaim + ". " + name + "\n \
    bowed, and started " + verb3 + " away towards the woods. As soon as he was almost out of view, he looked back at the crowd, smiled, \n\
    and turned into a " + creature + "."
    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(story1)

if choice == 2:


if choice == 3:


else:
    print("That wasn't a choice! No stories for you.")