#This is a madlibs generator with a GUI with Tkinter
#Using a tkinter tutorial
#By Ashley Cook

# Set up Tkinter
from tkinter import *
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text = 'Mad Libs Generator \n Have fun!' , font = 'arial 20 bold ', background= 'black', fg = 'white').pack()
Label(root, text = 'Choose a Story : ', font = 'arial 15 bold', background= 'black', fg = 'white').place(x=40, y= 80)
root.configure(background ='black')
#Set up game
import time
#Story 1
def madlib1():
    print("Good choice! Time to add your words to the story!")
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
#Story 2
def madlib2():
    print("Good choice! Time to add your words to the story!")
    time.sleep(1)

    name1 = input("Please enter a person's name: ")
    name2 = input("Please enter a second person's name: ")
    bg1 = input("Please enter the name of a board game you like: ")
    food1 = input("Please enter a type of food: ")
    drink1 = input("Please enter a type of drink: ")
    exclamation =  input("Please enter an exclamation: ")
    exclamation2 =  input("Please enter an exclamation: ")
    adjj= input("Please enter an adjective: ")
    
    story2 = "Saturday night meant it was game time!" + name1 + " and " + name2 + " loved playing board games. Their favorite lately was " + bg1 + ". \n\
    They decided to order some " + food1 + " and poured some " + drink1 + " and sat down to play. They started taking out all the card and pieces \n\
    to play  " + bg1 + " when they noticed something weird. The " + food1 + " they ordered was in their " + bg1 + " box! They had just placed the order, \n\
    how could that have happened? " + name1 + " called up the " + food1 + " place and asked what the deal was, but they had no idea what she was talking \n\
    about. '" + exclamation + "!' They decided to take the food out and start playing their game. They set it up and started playing. They drank some of their \n\
     " + drink1 + " and started feeling woozy and " + adjj + ". '" + exclamation2 + "' said " + name2 + " when they looked down, and all of their board game pieces were now \n\
    miniature pieces of " + food1 + ". 'I don't think I ever want to play " + bg1 + " again', said " + name1 + ", right before they both fell asleep in a pool of " + drink1 + "."
    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(story2)
#Story 3
def madlib3():
    print("Good choice! Time to add your words to the story!")
    time.sleep(1)
    dogname = input("Please enter a name: ")
    ingverb = input("Please enter a verb ending in -ing: ")
    veggie = input("Please enter a vegetable: ")
    pluralnoun = input("Please enter a plural household object: ")
    pluralnoun2 = input("Please enter a plural household object: ")
    flowers = input("Please enter a type of flower, plural: ")
    room = input("Please enter a room in the house: ")
    foodnow = input("Please enter a type of food, plural: ")
    goodadj = input("Please enter a adjective: ") 
    nouns = input("Please enter a plural onject: ")
    story3 = "In a little cottage in the woods, there lived two women and their cute little beagle, " + dogname + ". The little doggy was quite rambunctious, \n\
    he was always " + ingverb + " through the garden and trampling the " + veggie +". When he was inside and his parents weren't giving him enough attention, \n\
    " + dogname + " would eat whatever "+ pluralnoun + " he could find, and he would hide all their " + pluralnoun2 + ". One day, he was just too naughty that he \n\
    got a timeout. His parents told him he would need to make it up to them. " + dogname + " thought about what he could do to make it all better. Finally, he came up \n\
    with a plan. When his parents went to bed, he snuck out of his crate. He went to the garden to pick some " + flowers + " and scrambled around the house finding all \n\
    the pillows, blankets, and " + nouns + ". He put them all in a pile in the " + room + " and he put the flowers in the middle. Then he grabbed some " + foodnow + " to put\n \
    on the table. When the parents woke up, they went into the " + room + " and saw what he had done. It was a comfy fort just for them! They ate their " + foodnow + " and \n\
    sat down in the pile of pillows and " + nouns + " and had a " + goodadj + " and cozy day with their pup."
    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(story3)

#Buttons
Button(root, text ='Creature Story', font = 'arial 15', command= madlib1, bg = 'green').place(x=60, y=120)
Button(root, text='Game Night', font ='arial 15', command = madlib2, bg = 'pink').place(x=70, y=180)
Button(root, text='Bad Dog', font ='arial 15', command = madlib3, bg = 'light blue').place(x=80, y=240)
root.mainloop()
