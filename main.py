import time
print()
print(" "*15+"Know Your Personality")
print()
print("Let's discover who you really are with some fun data magic!")
time.sleep(0.5)
print("Scanning colors, foods, and animal energies...")
time.sleep(1)
print("Calculating your personality type using complex non-scientific logic...")
time.sleep(1.5)

print("_"*80)
print()

name=input("Enter your name : ")
age=input("Enter your age : ")
city=input("Enter the city you live in: ").title()
favourite_food=input("Your favourite food is: ").lower()
favourite_color=input("Enter your favourite color: ").upper()
spirit_animal=input("Enter the animal you feel sprit: ").lower()
love_doing=input("Enter the thing you love doing: ").lower()
personality_code=name[:2].upper()+age[-1]+spirit_animal[0].upper()+favourite_color[0].lower()
print()

print(f"You'r from {city},a place of dreams!")
print(f"You love {favourite_food}, and enjoying doing {love_doing}")
print(f"You vibe with color {favourite_color}, and your spirit animal is the {spirit_animal}")
print(f"You already lived {int(age)*12} months already")

if (int(age)<18):
    #print("You belong to 'Young Explorer' tribe")
    title='young explorer'
elif (int(age)>=18 and int(age)<=30):
    #print("You belong to 'Adventurer' tribe ")
    title='adventurer'
else:
    #print("You belong to 'Wise Owl' tribe")
    title='wise owl'
title=title.title()
print(f"You belong to {title} tribe")
print(f"Your Secret Personality Code is: {personality_code} ")

print()
str_len=len(love_doing)
if (str_len<=8):
    print("Time to explore more hobbies? You’ve got hidden sparks waiting!")
else:
    print("You seem deeply passionate — that hobby says a lot about your vibe!")

print()

print("You are officially certified as: FUNKY AND FABULOUS! ")
print()


