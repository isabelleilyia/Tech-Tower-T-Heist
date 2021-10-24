import time
import random
import sys


i=True


#Classes
class Map:
    locations_east = []
    locations_west = []
    locations_mid = []
    
    def __init__(self):
        self.locations_east= ["Bobby Dodd", "Sorority House", "Towers", "Tech Green"]
        self.locations_west= ["Burger Bowl", "Flag Building", "CRC", "Tech Green"]
        self.locations_mid = ["Klaus", "CULC", "Tech Green"]
        

    def determineNextMove(self,location):
        printLine("Thank you for visiting " + location + "!")
        character.new_locs.remove(location)
        if location=="Bobby Dodd" or location=="Sorority House" or location=="Towers":
            self.east()
        elif location=="Burger Bowl" or location=="CRC" or location=="Flag Building":
            self.west()
        elif location=="Klaus" or location=="CULC":
            self.techGreen()

    def east(self):
        printLine("Welcome to East campus! You can go to one of the following locations. \
Type the location you would like to visit next.")
        for item in self.locations_east:
            if item in character.new_locs:
                printLine(item)
        choice = input("")
        choice=choice.lower()
        if choice=="bobby dodd":
            bobbyDodd()
        elif choice=="sorority house":
            sororityHouse()
        elif choice=="towers":
            towers()
        elif choice=="tech green":
            self.techGreen()
        else:
            printLine("Invalid location!")
            self.east()

    def west(self):
        printLine("Welcome to West campus! You can go to one of the following locations. \
Type the location you would like to visit next.")
        for item in self.locations_west:
            if item in character.new_locs:
                printLine(item)
        choice = input("")
        choice = choice.lower()
        if choice=="burger bowl":
            burgerBowl()
        elif choice=="crc":
            crc()
        elif choice=="flag building":
            flagBuilding()
        elif choice=="tech green":
            self.techGreen()
        else:
            printLine("Invalid location!")
            self.west()

    def mid(self):
        printLine("You can go to one of the following locations. Type the location you would like to visit next.")
        for item in self.locations_mid:
            if item in character.new_locs:
                printLine(item)
        choice = input("")
        choice = choice.lower()
        if choice=="klaus":
            klaus()
        elif choice=="culc":
            culc()
        elif choice=="tech green":
            self.techGreen()
        else:
            printLine("Invalid location!")
            self.mid()
        
    def techGreen(self):
        global i
        printLine("You have been brought to Tech Green.")
        if not i:
            check()
        if i:
            instructions()
            i=False
        printLine("You can now choose to go to east campus, west campus, or stay on mid-campus")
        printLine("Enter 'East', 'West', or 'Mid' to make your choice.")
        decision = input("")
        decision = decision.lower()
        if decision == "east":
            self.east()
        elif decision == "west":
            self.west()
        elif decision == "mid":
            self.mid()
        else:
            printLine("Invalid location!")
            self.techGreen()

    def telephone(self):
        printLine("You awaken to the ring of the telephone.")
        printLine("Do you pick up or ignore?")
        choice = input("Type 'pick up' or 'ignore'\n")
        if choice.lower() == "pick up":
            self.techGreen()
        else:
            self.telephone()

class Character:
    energy_points = 8
    dining_dollars = 15
    objects = []
    new_locs = []

    def __init__(self):
        self.objects=[]
        self.new_locs=["Klaus","CULC","Burger Bowl","CRC","Flag Building","Sorority House","Towers", \
                  "Bobby Dodd","Tech Green"]


#Overhead functions
def printLine(line):
    for letter in line:
        print(letter,end="")
        time.sleep(0.04)
    print()
    time.sleep(1)
    return ""
    
def instructions():
    printLine("Your goal is to steal the 'T' from Tech Tower. To accomplish this, you must gather items you need from locations around campus by completing challenges.")
    printLine("Enter 'Y' if you understand")
    understand = input("")
    understand = understand.lower()
    if not understand=='y':
        instructions()
    printLine("Here are some things to keep in mind:")
    printLine("You begin with 8 energy points. Each time you fail a challenge, you lose an energy point.")
    printLine("You can gain more energy points by getting coffee and food at the many locations available around campus.")
    printLine("Be careful! If you ever run out of energy points, the game is over.")
    printLine("You also begin with 15 dining dollars. Each time you buy food or drinks, you spend a certain amount. Make sure you keep track of how much you have left!")
    printLine("When you arrive at a new location, you will be able to type 'menu' to eat, see your energy points, see your dining dollar balance, or review these instructions again. If you think you have enough items to complete the heist, you can type 'Tech Tower' and you will be taken there to attempt it.")
    printLine("Enter 'Y' if you are ready to proceed:")
    understand = input("")
    understand = understand.lower()
    if not understand=="y":
        instructions()
    
def menu():
    printLine("Please choose an option: '0' for instructions, '1' for food, '2' to view your energy points, or '3' to view your dining dollar balance.")
    user_in = input('')
    if user_in=="1":
        food()
    elif user_in=="2":
        printLine("You have " + str(character.energy_points) + " energy points.")
    elif user_in=="3":
        printLine("You have " + str(character.dining_dollars) + " dining dollars.")
    elif user_in=="0":
        instructions()
    else:
        printLine("Invalid choice!")
        menu()

def check():
    global character
    global map1
    global i
    if character.energy_points<=0:
        printLine("You have run out of energy points! However, you are perseverent.\nYou attempt the heist with the objects you currently have.")
        techTower()
        printLine("Type 'Y' to play again and 'N' to end the game.")
        ans = input("").lower()
        if ans=='y':
            i=True
            map1 = Map()
            character = Character()
            map1.telephone()
        else:
            sys.exit()
    printLine("Type 'menu' to view the menu, 'Tech Tower' to attempt the heist, or press Enter to proceed at this location.")
    decision = input("").lower()
    if decision == 'menu':
        menu()
    elif decision == "Tech Tower":
        techTower()
    else:
        return

#Location functions
def klaus():
    printLine("Welcome to the Klaus Center for Advanced Computing!")
    check()
    points=0
    printLine("If you want to succeed at Georgia Tech, you must be able to code (even if you're a business major).")
    printLine("Here's a short three question quiz to test your knowledge of Python.")
    printLine("Question 1: Write a line of code that prints 'Yellow Jackets' to the console, without the apostrophes.")
    answer = input("")
    printLine("Your code's output is:")
    try:
        exec(answer)
        printLine("Your code works!")
        points+=1
    except Exception as error:
        print(error)
        printLine("Your code didn't work!")
    printLine('''Question 2: Type the output of the following code \nfor i in range(10,0,-2):\n\tprint(i,end="")''')
    answer = input("")
    if answer == "108642":
        printLine("Correct!")
        points+=1
    else:
        printLine("Incorrect answer.")
    print('''Question 3: What is printed by the following code?\na=True\nb=False\nc=False\nif a or b and c:\n\tprint("GEORGIA TECH")\nelse:\n\tprint("Georgia Tech")''')
    answer = input("")
    if answer=="GEORGIA TECH":
        printLine("Correct!")
        points+=1
    else:
        printLine("Incorrect answer.")
    print('''Question 4: Write a line of code that creates a variable called 'a' with a value of 5.''')
    answer = input("")
    try:
        a = answer.split('=')[1].strip()
        printLine("Your value of a is: " + a)
        if a == '5':
            printLine("Correct!")
            points+=1
        else:
            printLine("Incorrect answer.")
    except:
        printLine('Incorrect answer.')
    printLine("Your score is: " + str(points) + "/4")
    if points>=3:
        printLine("Congratulations! You passed. You won a pair of night vision goggles!")
        character.objects.append('Goggles')
    else:
        printLine("Sorry, you didn't pass. Hopefully you weren't considering a computer science major at GT...")
        character.enegery_points-=1
        klaus()

    map1.determineNextMove("Klaus")
    
    
    
def crc():
    printLine("Welcome to the Campus Recreation Center,the home of the gym bros. We hope you're ready to workout!")
    check()
    printLine("You scan your buzzcard and enter the weights area. It is now time to build your workout. Choose three exercises from the following options. But choose wisely! If your workout is not feasible at the CRC, you won't be able to complete it!")
    chosen = []
    workouts = ("1: Chest Press", "2: Hip Abductions", "3: Hip Thrusts", "4: Bulgarian Split Squats", "5: Lat Pulldowns", "6: Tricep Push-ups", "7: Stairmaster Machine")
    for exercise in workouts:
        print(exercise)
    selection(chosen)
    completed = 0
    for i in range(0,len(chosen)):
        if not chosen[i]==6 and not chosen[i]==7:
            weight = input("Pick a weight to complete exercise " + str(workouts[chosen[i]-1]) + ". Your weight should be a multiple of 5 in the range 10lbs-70lbs\n")
            try:
                int(weight)
            except:
                printLine("Invalid weight entered.")
                continue
        elif chosen[i]==7:
            time = input("Pick a length of time to spend completing exercise " + str(workouts[chosen[i]-1]) + ". Please enter a number in minutes.\n")
        if not chosen[i]==6 and not chosen[i]==7 and (weight=="25" or weight=="20" or weight=="15"):
            printLine("Yikes! There are no dumbbells of weight " + weight + ". You cannot complete this exercise.")
            continue
        if chosen[i]==1:
            printLine("You arrive at the bench press area, but one of the gym bros tells you there's a line. You look back, and the line goes all the way out to the waiting area. Alas, you decide that you cannot complete this exercise. You turn up your Drake music and walk away sadly.")
        elif chosen[i]==2:
            printLine("You arrive at the hip abduction machine, but of course, it is taken. You ask the girl using it how many sets she has left, and she says 4. You don't have time to wait, so you crank up your Drake music and walk away sadly.")
        elif chosen[i]==3:
            printLine("You set up your hip thrust station, and you complete three sets of 12. Good job! You completed the exercise.")
            completed+=1
        elif chosen[i]==4:
            printLine("Yikes! You picked the hardest exercise. But you decide to take on the challenge anyways. After loads of blood, sweat, and tears, you complete the exercise! Congratulations!")
            completed+=1
        elif chosen[i]==5:
            printLine("You picked the busiest machine in the gym. You're not even going to try... You are unable to complete this exercise.")
        elif chosen[i]==6:
            printLine("You completed the pushups! You picked the best exercise! They need no equipment. Good job!")
            completed+=1
        elif chosen[i]==7:
            printLine("Wow! You are bold for choosing a cardio machine! You complete " + str(time) + " minutes on the Stairmaster.")
            completed+=1
    printLine("You were able to complete " + str(completed) + "/3 exercises.")
    if completed>=2:
        printLine("Congratulations! Your workout was a success! The CRC staff is super impressed. They gave you a free set of exercise ropes.")
        character.objects.append('Ropes')
    else:
        printLine("Sorry! Your workout was not successful.")
        character.energy_points-=1
        crc()
    map1.determineNextMove("CRC")


def bobbyDodd():
    correct=0
    printLine("Welcome to Bobby Dodd!")
    check()
    printLine("On game days, all Georgia Tech students and alumni come to cheer on our Yellow Jackets football team! There are some crowd cheers that you must know to participate. \
Once you arrive to the stadium, you meet a football player named Kyle. Kyle wants to see how well you know your cheers. Let's see how well you do!")
    printLine("Fill in the blanks in the following tech mottos and cheers:")
    printLine("Question 1. Fill in the blank: To hell with _______!")
    answer = input("")
    printLine("You said: To hell with {}!".format(answer))
    answer = answer.lower()
    if answer == "georgia":
        printLine("Correct answer!")
        correct+=1
    else:
        printLine('''Incorrect answer! The correct saying is "To hell with Georgia!"\nWe do not support UGA!''')
    printLine("Question 2. Fill in the blank: One of the mascots of Georgia Tech is the Ramblin' _____.")
    answer = input("")
    printLine("You said: One of the mascots of Georgia Tech is the Ramblin' {}.".format(answer))
    answer = answer.lower()
    if answer == "wreck":
        printLine("Correct answer!")
        correct+=1
    else:
        printLine('''Incorrect answer! The correct answer is "One of the mascots of Georgia Tech is the Ramblin' Wreck."''')
    printLine("Question 3. Fill in the blank: I'm a _______ engineer!")
    answer = input("")
    printLine("You said: I'm a {} engineer!".format(answer))
    answer = answer.lower()
    if answer == "helluva":
        printLine("Correct answer!")
        correct+=1
    else:
        printLine('''Incorrect answer! The correct answer is "I'm a helluva engineer!"''')
    printLine("Your score is {}/3".format(correct))
    if correct==3:
        printLine("You passed! You know your Tech stuff! You receive a football from Kyle!")
        character.objects.append('Football')
    else:
        printLine("Yikes! Kyle tells you you need to study your Tech stuff if you come.")
        character.energy_points-=1
        bobbyDodd()
    map1.determineNextMove("Bobby Dodd")

def sororityHouse():
    printLine("Welcome to one of the sorority houses on campus!")
    check()
    printLine("Georgia Tech has chapters of 8 sororities and 30 fraternities. You're in luck! There's a party happening tonight. You walk inside, \
and you run into one of your best friends! However, she seems to be under the influence... what do you do next?")
    printLine("Choose one of the following options, and enter the corresponding number: \n1. Leave\n2. Get her another drink\n3. Help her get home safely.")
    answer = input("")
    if answer=="1":
        printLine("Incorrect answer! Your friend could get seriously hurt!")
        printLine("You failed the test!")
        character.energy_points-=1
        sororityHouse()
    elif answer=="2":
        printLine("Incorrect answer! Your friend is already clearly drunk. Another drink sounds like a bad idea!")
        printLine("You failed the test!")
        character.energy_points-=1
        sororityHouse()
    elif answer=="3":
        printLine("Correct answer! Your friend arrived home safely.")
        printLine("You passed the test! The sorority girls loved you so much that they gave you a free wig!")
        character.objects.append('Wig')
    else:
        printLine("Invalid answer choice. Please try again.")
        sororityHouse()
    map1.determineNextMove("Sorority House")


def towers():
    wrong_answer = 0
    printLine("Welcome to Towers Residence Hall!")
    check()
    printLine('You remember that your friend Isabelle works at the registration office at Tech Tower.\nShe must have the key!\nYou decide to visit her at her dorm in towers\nYou knock...No answer.\nYou knock again..."WHAT?!"\n')
    printLine("Isabelle is not very nice today and she decides to put you to the test!\nShe proceeds to ask:\'Feed me anything and I'll grow but give me water and I'll die.\'\nWho am I?")
    printLine('Beware, you only get three tries before you start losing points!')
    answer = input('')
    while wrong_answer<2:
        if answer.lower() == 'fire':
            printLine('WOW! You guessed it! Isabelle gives you the key, grunts and slams the door! At least you got the key!')
            character.objects.append('Key')
            break
        else:
            printLine('No, Try again!')
            wrong_answer += 1
            answer = input('')
            continue
    if wrong_answer == 2:
        character.energy_points -= 1
        towers()
    map1.determineNextMove("Towers")

def culc():
    gtid = 903123633
    printLine("You get to the most famous place on campus! The CULC.")
    check()
    printLine("However, it's 7pm and you need your buzzcard to get in! Bummer! You don't have it on you!\nYou approach a security guard and express your concern")
    printLine('"I can help you!" She says, "I just need your GTID #:"')
    printLine('You forgot your number so you try to guess it. Luckily you remember some of it! GTID# starts with 9031236! You just have to guess the last two digits')
    guess()
    map1.determineNextMove("CULC")


def flagBuilding():
    location = "Flag Building"
    points = 0
    printLine('Welcome to the famous Flag Building!')
    check()
    printLine("Did you know that Georgia Tech hangs a flag for the home countries of every student!\nIn order to access the valuable item you need,\nyou must make the international community proud!")
    printLine('I will describe a flag and you will have to guess the country it relates to!\nGood Luck!')
    printLine("First flag:\nThis flag has a green background, a yellow diamond in the middle containing a blue circle!")
    brazil()
    canada()
    france()
    printLine("You're a true georgraphy expert!\nYou run into the building.\nAfter looking at all the diverse flags hung up on the ceiling,\nyou pickup a flag pole and go on to your next stop...")
    character.objects.append('Pole')
    map1.determineNextMove("Flag Building")
    
     
def burgerBowl():
    printLine("You hear the peaceful sound of harmonizing ohms emerging from Couch Burger Bowl Field. Curious, you get a little closer to discover eight or so people stretching on an array of yoga mats.")
    check()
    printLine("The instructor notices you and smiles. She tells you that there is one spot left in the class and asks if you would like to join. She also says there is a prize for best yogi of the day.")
    yoga = input(printLine("Would you like to join?")).lower()
    while yoga != "yes":
        yoga = input(printLine("Would you like to join?")).lower()
    printLine("'Perfect', she exclaims, 'I am Sarra by the way. Is this your first class?'")
    firstclass = input(printLine("")).lower()
    if firstclass == "yes":
        printLine("'Do not worry, everyone has to start somewhere.' She shoots you a wink.")
    elif firstclass == "no":
        printLine("Sarra smiles ear to ear. 'OH MY GOSH! Namaste fellow yogi. My style of yoga is different than most so let me explain.'")
    else:
        printLine("'The class is starting soon so let me explain how my style of yoga works.'")
    printLine("'This yoga class will consist of a sequence of poses. I will say it once and you must do the poses in that order.'")
    sounds_good = input(printLine("Sounds good?")).lower()
    printLine("'If you do the poses correctly and in the right order, I have a very special prize for you. If not, I am teaching a class right after this so you can try again.'")
    printLine("'We are wasting precious time, let us begin...")
    sequence_one()
    map1.determineNextMove("Burger Bowl")

def techTower():
    if not len(character.objects)==8:
        printLine("Attempting heist...")
        time.sleep(3)
        printLine("You did not have enough objects to complete the heist! Cabrera caught you :(")
        printLine("You will now be redirected to Tech Green to continue.")
        if character.energy_points<=0:
            return
        map1.techGreen()
        return
    printLine("After spending several hours collecting the necessary supplies to complete the heist you think you are finally ready.")
    printLine("You near Tech Tower, trying to be as stealth as possible.")
    printLine("'This is going to be harder that I thought', you think to yourself.")
    time.sleep(1)
    printLine("The first obstacle you face is getting over the electric fence...")
    printLine("You use the yoga mat that Sarra gave you to climb over without getting electrocuted.")
    printLine("At this point you are surrounded by guards on all sides. You need to think of a disguise quickly.")
    printLine("You realize that you recognize these girls: They are sorority girls, but what are they doing guarding Tech Tower?")
    printLine("You put on the wig you got from the sorority house and walk past the guards unscathed.")
    time.sleep(1)
    printLine("Before you stands a building that looks inpenetrable.")
    printLine("Before entering the building you need to make sure there are no guards on the other side of the door.")
    printLine("Even though you are disguised, guards on outdoor duty are not allowed inside Tech Tower during surveillance hours")
    printLine("You put on your new pair of x-ray glasses and the coast is clear.")
    printLine("You take the key to Tech Towers that Isabelle gave you and enter the building.")
    time.sleep(1)
    printLine("You have done your Tech Tower research, so you know that the interior of the building is heavily surveillanced by cameras.")
    printLine("Careful not to reveal your identity, you tear out pages from the book you got from the Culc and cover every camera you see.")
    printLine("At this point you do not recognize any of the guards. They are no longer sorority girls, your disguise will not work.")
    printLine("You need to distract the guards so you can sneak up to the roof of the building and, at last, steal the T.")
    printLine("Staying hidden, you throw the football in the opposite direction of the guards to create some noise.")
    printLine("Fortunately, your plan works-- the guards hurry towards the commotion to investigate...")
    printLine("Like a ninja, you slip through the stairway entrance and head to the rooftop.")
    time.sleep(1.5)
    printLine("...")
    time.sleep(1.5)
    printLine("You've almost done it...")
    time.sleep(1)
    printLine("The T shimmers in the night...")
    time.sleep(1)
    printLine("Tears fill your eyes... it's magnificent...")
    time.sleep(1)
    printLine("You secure the rope from the CRC around the T and start to head your way back.")
    printLine("Suddenly, you hear a guard shout behind you, 'Stop!'")
    printLine("You need to improvise... you take your flag pole and slide down the side of Tech Tower before dissapearing into the night...")
    printLine("The guards barely know what hit them.")
    printLine("The next morning, you get a call from Georgia Tech...")
    time.sleep(1)
    printLine("You've been accepted!\n")
    sys.exit()

    
#Helper Functions
def brazil():
    brazil = input('')
    while brazil.lower() != 'brazil':
        printLine("That is disappointing!Try again!")
        character.energy_points -= 1
        brazil = input('')
    if brazil.lower() == 'brazil':
        printLine('Bom Trabalho!')
def canada():
    printLine("Next Flag:\nThis flag is red and white and contains a red maple leaf in the center!")
    canada = input('')
    while canada.lower() != 'canada':
        printLine("Mmhmm, Not quite! Guess again!")
        character.energy_points -= 1
        canada = input('')
    if canada.lower() == 'canada':
        printLine('Good Job!')
def france():
    printLine("Last Flag:\nThis flag has 3 vertical stripes: Blue, White and Red!")
    france = input('')
    while france.lower() != 'france':
        printLine("Incorrect! What else?")
        character.energy_points -= 1
        france = input('')
    if france.lower() == 'france':
        printLine('Bravo!')
def guess():
        printLine('What is your full GTID #?')
        gtid=903123633
        try:
            trial = int(input(''))
            character.energy_points -= 0.1
            while trial != gtid:
                if trial< 903123600:
                    printLine('Your GTID consists of 9 digits!')
                elif trial>gtid:
                    printLine("Your Number is Lower than that!")
                elif trial<gtid:
                    printLine('Your Number is Higher than that!')
                printLine('What is your full GTID#\n')
                trial = int(input(''))
            if trial == gtid:
                printLine("Cool! That's a Valid GTID! Welcome to the CULC!\nYou enter the building, retrieve the book you need and run out without anyone noticing you...")
                character.objects.append('Book')
        except:
            printLine('Not Valid!')
            guess()

def sequence_one():
    printLine("Sarra walks to the center of her mat,'For this class, we will be doing a circular flow.'")
    printLine("rise, forward fold, crow, warrior one, vinyasa!")
    printLine("Now its your turn yogis!")
    pose1 = input(printLine("You think to yourself... 'What pose came first?'")).lower()
    if pose1 == "rise":
        pose2 = input(printLine("Sarra smiles,'Very good, whats next?'")).lower()
        if pose2 == "forward fold":
            pose3 = input(printLine("Incredible! 'And then?'")).lower()
            if pose3 == "crow":
                pose4 = input(printLine("'AMAZING! SHOW ME MORE?'")).lower()
                if pose4 == "warrior one":
                    pose5 = input(printLine("Sarra erupts with laughter, 'ONE MORE POSE!'")).lower()
                    if pose5 == "vinyasa":
                        printLine("You have never seen someone so happy. Sarra congratulates you on completing her challenging class then hands you a yoga mat.")
                        character.objects.append('Mat')
                    else:
                        printLine("Sarra's eyes fill with tears,'You were SO CLOSE! STAY FOR MY NEXT CLASS!!'")
                        printLine("You realize you don't have much choice.")
                        character.energy_points-=1
                        sequence_one()
                else:
                    printLine("'So close yet so far', says Sarra. You can tell she is dissapointed.")
                    printLine("You feel guilty for letting Sarra down so you decide to take the class again.")
                    character.energy_points-=1
                    sequence_one()

            else:
                printLine("Sarra shakes her head, 'Incorrect, let's try again!'")
                printLine("You want the prize for completing the class... whatever it is, so you decide to take the class again.")
                character.energy_points-=1
                sequence_one()
        else:
            printLine("'Better luck next time', says Sarra")
            printLine("You decide to stay for the next class.")
            character.energy_points-=1
            sequence_one()
    else:
        printLine("'Your performance was embarassing', screams Sarra")
        printLine("Wanting to change Sarra's perception of you, you decide to sign up for the next class.")
        character.energy_points-=1
        sequence_one()

def selection(chosen):
        try:
            printLine("Enter the number of your first workout selection:")
            workout1 = input("")
            chosen.append(int(workout1))
            printLine("Enter the number of your second workout selection:")
            workout2 = input("")
            chosen.append(int(workout2))
            printLine("Enter the number of your third workout selection:")
            workout3 = input("")
            chosen.append(int(workout3))
        except:
            printLine("Invalid selection. Please try again.")
            selection()
            
#Food functions
def food():
    if character.dining_dollars>0:
        place = input('''Feeling tired? Where do you want to eat now? Enter 'C' for Chic Fil A, 'B' for Blue Donkey, or 'D' for a dining hall.''')
        if place == 'C':
            chick_fila()
        elif place == 'B':
            blue_donkey()
        elif place == 'D':
            halls = ['W','N','B']
            randhall = halls[random.randrange(len(halls))]
            if randhall == 'W':
                willage()
            elif randhall == 'N':
                north_ave()
            elif randhall == 'B':
                brittain()
        else:
            printLine('Not an option! Read the instructions carefully.')
            food()
    else:
        printLine("Sorry you've run out of money! Use your remaining energy points wisely.")
        


def blue_donkey():
    printLine("You are now at blue donkey, the perfect place for sleep deprived students\nYou think to yourself: hot coffee would be perfect to keep you up!\nThe lady at the desk asks")
    printLine('A hot coffee or a muffin?')
    coffee = input("")
    if coffee == 'hot coffee':
        character.energy_points += 1
        character.dining_dollars-=3
    else:
        printLine('Caffeine is more efficient when it comes to energy!')
        blue_donkey()
    printLine("Yum! You are now ready to go back to work.")



def chick_fila():
    printLine('You arrived to the most famous food truck at Georgia Tech!\nThe line is long but their famous spicy chicken will give you the right amount \nof spice to continue your arduous journey!')
    printLine('After your long wait, you aproach the cashier and you order a')
    sandwich = input('')
    if sandwich == 'spicy chicken':
        character.energy_points += 1
        character.dining_dollars-=3
        printLine("Yum! You are now ready to go back to work.")
    else:
        printLine('Chick-Fil-a has much better things to offer!')
        chick_fila()


def north_ave():
    printLine("Nave won't be your favorite but it does the job\n From the food you can get an icecream,chicken,tofu and salad.")
    printLine("Pick wisely, you need a sufficient amount of protein to succeed in your journey.")
    choice = input('')


    if choice == 'salad':
        character.energy_points += 1
        character.dining_dollars -= 2
    elif choice == 'ice cream':
        character.energy_points += 0.5
        character.dining_dollars -= 3
    elif choice == 'chicken' or choice == 'tofu':
        character.energy_points += 2
        character.dining_dollars -= 3
    else:
        printLine("You're at Nave, don't get too creative! Your options are limited.")
        north_ave()
    printLine("Yum! You are now ready to go back to work.")


def bagelBros():
    printLine("Everything Bagels is all we're offering today! Enjoy your meal!")
    character.energy_points += 1
    character.dining_dollars -= 2
    
def smoothieLand():
    printLine("Smoothie Land has two Clerks, Miss Happy and Mister Grumpy! Let's see who is serving you today!")
    num = random.randrange(1)
    if num == 0:
        printLine("Lucky Day! Miss Happy offered you a free smoothie")
    else:
        printLine("Shoot, Mister Grumpy is annoyed today and charges you twice as much for a smoothie!")
        character.dining_dollars -= 2
    character.energy_points += 0.5
    printLine("Yum! You are now ready to go back to work.")

    
def brittain():
    printLine("Welcome to Brittain! Looks similar to the Harry Potter dining Hall doesn't it?!\nWhat's special about brittain is that they offer a wide range\nof breakfast options at any time of the day!")
    printLine('You have two stations: the Smoothie Station and the Bagel Station\nWhere would you rather eat?')
    place = input('')
    if place == 'Bagel Station':
        bagelBros()
    elif place == 'Smoothie Station':
        smoothieLand()
    else:
        printLine('That place is closed! Sorry!\n')
        brittain()
    printLine("Yum! You are now ready to go back to work.")

        
def willage():
    printLine('Welcome to Willage! Today is Make your Own Waffle Day!\nYou can Head to the station and make your Waffle!')
    character.energy_points += 1
    character.dining_dollars -= 2
    printLine("Yum! You are now ready to go back to work.")



map1 = Map()
character = Character()

map1.telephone()
