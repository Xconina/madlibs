#This is a madlibs generator with a GUI with Tkinter
#I will use dictionaries and lists to store input
#By Ashley Cook

# Set up Tkinter
from tkinter import *
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text = 'Mad Libs Generator \n Have fun!' , font = 'courier 20 bold ', background= 'black', fg = 'white').pack()
Label(root, text = 'Choose a Story : ', font = 'courier 15 bold', background= 'black', fg = 'white').place(x=40, y= 80)
root.configure(background ='black')
#Set up game
import time
#Story 1
def madlib1():
    print("Good choice! Time to add your words to the story!")
    time.sleep(1)
    #make keys for dictionary
    madlib1dict = [
        'an adjective',
        'second adjective',
        'a type of creature',
        'a verb, ending in -ing',
        'an emotion adjective',
        'a name',
        'a fourth adjective',
        'an animal or creature',
        'a past tense verb',
        'a food',
        'a drink',
        'an exclamation',
        'a verb ending in -ing',
        'a weapon',
    ]
    #get values for each key
    madlib1dictinput = {}
    for key in madlib1dict:
        value = input(f'Please enter {key}: ')
        madlib1dictinput[key] = value
    #initiate countdown
    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    #print madlibs story 1 with user input
    print(f"Once upon a time, there was a village. In that village lived a {madlib1dictinput['an adjective']} , {madlib1dictinput['second adjective']} {madlib1dictinput['a type of creature']}.\n \
    They were always {madlib1dictinput['a verb, ending in -ing']} around town, making everyone else {madlib1dictinput['an emotion adjective']}. But one day, someone new came into the village named {madlib1dictinput['a name']}.\n \
    They were a(n) {madlib1dictinput['a fourth adjective']} {madlib1dictinput['an animal or creature']} . They had enough of the  {madlib1dictinput['a type of creature']} and were there to vanquish it. {madlib1dictinput['a name']} took out their {madlib1dictinput['a weapon']}, \n \
    {madlib1dictinput['a past tense verb']} up to the {madlib1dictinput['a type of creature']} and attacked! As soon as the {madlib1dictinput['a type of creature']} was hit, it started bursting from the inside out. \n \
    It was so odd! Chunks of {madlib1dictinput['a food']} were flying out of the body, and instead of blood, {madlib1dictinput['a drink']} was pouring from the wound. The crowd \n \
    that had been gathering gasped. They had never seen such a thing before. Then, the crowd started cheering, saying '{madlib1dictinput['an exclamation']}!' . {madlib1dictinput['a name']} \n \
    bowed, and started {madlib1dictinput['a verb ending in -ing']}away towards the woods. As soon as he was almost out of view, he looked back at the crowd, smiled,\n\
    and turned into a {madlib1dictinput['a type of creature']}.")
#Story 2
def madlib2():
    print("Good choice! Time to add your words to the story!")
    time.sleep(1)
    #dictionary keys
    dict2 = [
        'a name',
        'a second name',
        'a board or card game you like',
        'a food',
        'a drink',
        'an exclamation',
        'another exclamation',
        'an adjective'
    ]
    #get user input for keys
    dict2full = {}
    for key in dict2:
        value = input(f'Please enter {key}: ')
        dict2full[key] = value
    #initiate countdown
    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    #print madlibs2
    print(f"Saturday night meant it was game time! {dict2full['a name']} and {dict2full['a second name']} loved playing board games. Their favorite lately was {dict2full['a board or card game you like']}. \n\
    They decided to order some {dict2full['a food']} and poured some {dict2full['a drink']} and sat down to play. They started taking out all the card and pieces \n\
    to play {dict2full['a board or card game you like']} when they noticed something weird. The {dict2full['a food']} they ordered was in their {dict2full['a board or card game you like']} box! They had just placed the order, \n\
    how could that have happened? '{dict2full['a name']}' called up the {dict2full['a food']} place and asked what the deal was, but they had no idea what she was talking \n\
    about. '{dict2full['an exclamation']}!' They decided to take the food out and start playing their game. They set it up and started playing. They drank some of their \n\
    {dict2full['a drink']} and started feeling woozy and {dict2full['an adjective']}. ' {dict2full['another exclamation']}!' said {dict2full['a second name']} when they looked down, and all of their board game pieces were now \n\
    miniature pieces of {dict2full['a food']}. 'I don't think I ever want to play {dict2full['a board or card game you like']} again', said {dict2full['a name']}, right before they both fell asleep in a pool of {dict2full['a drink']}.")
#Story 3
def madlib3():
    print("Good choice! Time to add your words to the story!")
    time.sleep(1)
    #madlibs3dictionary keys
    libs3keys = [
        'a name',
        'a verb ending in -ing',
        'a vegetable',
        'a household object, plural',
        'another household object, plural',
        'a type of flower, plural',
        'a room in the house',
        'a type of food, plural',
        'an adjective',
        'an object, plural',
    ]
    libs3 = {}
    for key in libs3keys:
        value = input(f"Please enter {key}: ")
        libs3[key] = value

    print("Story time!")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"In a little cottage in the woods, there lived two women and their cute little beagle, {libs3['a name']}. The little doggy was quite rambunctious, \n\
    he was always {libs3['a verb ending in -ing']} through the garden and trampling the {libs3['a vegetable']}. When he was inside and his parents weren't giving them enough attention, \n\
    {libs3['a name']} would eat whatever {libs3['a household object, plural']} he could find, and he would hide all their {libs3['another household object, plural']}. One day, he was just too naughty that he \n\
    got a timeout. Their parents told them he would need to make it up to them. {libs3['a name']} thought about what he could do to make it all better. Finally, he came up \n\
    with a plan. When their parents went to bed, he snuck out of his crate. He went to the garden to pick some {libs3['a type of flower, plural']} and scrambled around the house finding all \n\
    the pillows, blankets, and {libs3['an object, plural']}. He put them all in a pile in the {libs3['a room in the house']} and he put the flowers in the middle. Then he grabbed some {libs3['a type of food, plural']} to put\n\
    on the table. When the parents woke up, they went into the {libs3['a room in the house']} and saw what the pup had done. It was a comfy fort just for them! They ate their {libs3['a type of food, plural']} and \n\
    sat down in the pile of pillows and {libs3['an object, plural']} and had a {libs3['an adjective']} and cozy day with their pup.")

#Buttons
Button(root, text ='Creature Story', font = 'courier 15', command= madlib1, bg = 'green').place(x=60, y=120)
Button(root, text='Game Night', font ='courier 15', command = madlib2, bg = 'pink').place(x=70, y=180)
Button(root, text='Bad Dog', font ='courier 15', command = madlib3, bg = 'light blue').place(x=80, y=240)
root.mainloop()
