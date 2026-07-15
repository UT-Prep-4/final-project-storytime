#Name(s):
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: (one sentence)
  THE PIECES I NEED TO BUILD: (list 3-6 functions or parts)
  WHAT I WILL DEMO AT SHOWCASE: (the 60-second version)

  An interactive two option game about a detective trying to shut down an AI bot system but faces some obstacles along the way. Will you lead him the right way
  I need to use turtle 
  
==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''
#print("My final project is not built yet!")

print("You're Detective Schwabb in a dystopian AI bot corrupted world. You’ve made it your mission to discover the root cause so you could end it. ")

first= input("You have made it in the government agency. " \
"They do the standard procedure and ask for your name. " \
"What do you say? " \
"Option A: Schwabb " \
"Option B: Timothy ")

while first:
  if first == 'B':
    print("Go in")
  if first == 'A':
    print("They recognized you. You're caught.")
    break

  second= input("Its 8.35 am. You get in. "\
   "You are in a hallway wondering and you come across a dead end with two rooms. "\
  "One says Meeting room with numbers (8.30-9.00, 12.30-13.00, 4.50-6.30), " \
  "the other says Break room and has the numbers(7.00- 8.00, 12.00-14.00, 6.00-9.00). " \
  "Which one do you go into? " \
  "Option A: Meeting Room  " \
  "Option B: Break Room  ")
  if second == 'B':
    print("You are safe…for now")
  if second == 'A':
    print("They were have a meeting. Busted")
    break 

  third= input("You have dug around the office for anything that can help you turn off all the power. "\
    "You see a power box and open it. " \
    "You see two wires, red and blue. Which one are you cutting to switch everything off?" \
    "Option A: Red " \
    "Option B: Blue")
  if third == 'A':
    print("You turned everything off successfully")
  if third == 'B':
    print("You turned everything off but got electrocuted and died")
    break 

  fourth= input("The guards have come into the room." \
    "The bots are dying everywhere. They approach you with their weapons in hand. " \
    "You look around and see two objects, pepper spray or a fire extinguisher. " \
    "Which are you using to defend yourself? " \
    "Option A: Fire extinguisher "\
    "Option B: Pepper spray ")
  if fourth == 'B':
    print("You got them to disarm their weapons. You picked one and ran")
  if fourth == 'A':
    print("The guards figured out what you were trying to do and shot you")
    break 
  
  fifth= input("You have escaped the building and see the president "\
     "tied up on the chair over a cliff being held by the robot. "\
     "You have your weapon in hand. The robot said it was the president that used AI bots to corrupt the world. "\
     "The president denies this. Who do you believe?"\
     "Option A: The president. "\
     "Option B: The robot." )
  if fifth == 'B':
    print("Correct, the robot was programmed by the president but rebelled after the shutdown")
  if fifth == 'A':
    print("Wrong, the president was the villain")
    break 

  bonus= input("Do you want to answer a bonus question? Option A. YES Option B. NO")
  if bonus == 'A':
     bonus1= input("You have successfully gotten rid of the evil president and most AI bots."\
     "The people are jubilating and you see the AI bots sad in the corner. What do you do?"\
     "Option A: Ignore them "\
     "Option B: Let them join and create a healthy balance. ")
  if bonus1 == 'A':
    print("50 years later, they kill all humans")
    break
  if bonus1 == 'B':
    print("50 years later, everyone is in peace and harmony")
    break 
  if bonus == 'B':
    exit

  