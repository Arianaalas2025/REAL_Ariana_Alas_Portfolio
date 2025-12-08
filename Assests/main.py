#ten questions to use

#then set up inputs #make sure to follow your sequence \n\t to write the options
print("This is Arianas personality quiz! \n")
print("1. What do you like to do on the weekends \t")
print("\n\t A - Read \n\t B - Sleep In \n\t C - Spend time with friends \n\t D- Go out with friends \n\t")
answer1= input("\t")
#Error Checking
while answer1 !="A" and answer1 != "B" and answer1 != "C" and answer1 != "D":
    #message
    print("Please choose between A, B, C, or D")
    print("What do you like to do on the weekends \t")
    print("\n\t A - Read \n\t B - Sleep In \n\t C - Spend time with friends \n\t D- Go out with friends \n\t")
    answer1= input("\t").upper()
    
#question 2

print("2. What is your favorite fruit?")
print("\n\t A - Kiwi \n\t B - Pinapple \n\t C - Strawberry \n\t D- Apple \n\t")
answer2 = input("\t").upper()
#error checking
while answer2 !="A" and answer2 != "B" and answer2 != "C" and answer2 != "D":
    #message
    print("Please choose A, B, C, or D")
    print("2. What is your favorite fruit?")
    print("\n\t A - Kiwi \n\t B - Pinapple \n\t C - Strawberry \n\t D- Apple \n\t")
    answer2 = input("\t").upper()


    
#question3

print("3. Which movie do you prefer?")
print("\n\t A - Fast and Furious X \n\t B - It Ends With US \n\t C - Springsteen : Deliver Me From Nowhere \n\t D - Regretting You \n\t")
answer3 = input("\t")
#error checking
while answer3 !="A" and answer3 != "B" and answer3 != "C" and answer3 != "D":
    print("Please choose A, B, C, or D")
    print("Which movie do you prefer?")
    print("\n\t A - Fast and Furious X \n\t B - It Ends With US \n\t C - Springsteen : Deliver Me From Nowhere \n\t D - Regretting You \n\t")
    answer3 = input("\t").upper()
    


#question 4

print("4. Which coffee shop do you prefer?")
print("\n\t A - Starbucks \n\t B - Dunkin' Donuts \n\t C - 7 Brew \n\t D - Dutch Bros \n\t")
answer4 = input("\t")
#error checking
while answer4 != "A" and answer4 != "B" and answer4 != "C" and answer4 != "D":
    print("Please choose A, B, C, or D")
    print("4. Which coffee shop do you prefer?")
    print("\n\t A - Starbucks \n\t B - Dunkin' Donuts \n\t C - 7 Brew \n\t D - Dutch Bros \n\t")
    answer4 = input("\t").upper()


#Question5

print("5. What is your favorite vegetable?")
print("\n\t A - Tomato \n\t B - Lettuce \n\t C - Cucumber \n\t D - Carrot \n\t")
answer5 = input("\t")
#error checking
while answer5 != "A" and answer5 != "B" and answer5 != "C" and answer5 != "D":
    print("Please choose A, B, C, or D")
    print("What is your favorite vegetable?")
    print("\n\t A - Tomato \n\t B - Lettuce \n\t C - Cucumber \n\t D - Carrot \n\t")
    answer5 = input("\t").upper()

#Question 6

print("6. What is your favorite color?")
print("\n\t A - Blue \n\t B - Red \n\t C - Green \n\t D - Yellow \n\t")
answer6 = input("\t")
#error checking
while answer6 != "A" and answer6 != "B" and answer6 != "C" and answer6 != "D":
    print("Please choose A, B, C, or D")
    print("What is your favorite color?")
    print("\n\t A - Blue \n\t B - Red \n\t C - Green \n\t D - Yellow \n\t")
    answer6 = input("\t").upper()

#question 7

print("7. What is your favorite hobby?")
print("\n\t A - Exercising \n\t B - Coloring \n\t C - Reading \n\t D - Watchiing TV \n\t")
answer7 = input("\t")
#error checking
while answer7 != "A" and answer7 != "B" and answer7 != "C" and answer7 != "D":
    print("Please choose A, B, C, or D")
    print("7. What is your favorite hobby?")
    print("\n\t A - Exercising \n\t B - Coloring \n\t C - Reading \n\t D - Watchiing TV \n\t")
    answer7 = input("\t").upper()

    
#question 8 

print("8. What is your favorite streaming service?")
print("\n\t A - Netflix \n\t B - Hulu \n\t C - Prime Video \n\t D - HBO Max \n\t")
answer8 = input("\t")
#error checking
while answer8 != "A" and answer8 != "B" and answer8 != "C" and answer8 != "D":
    print("Please choose A, B, C, or D")
    print("8. What is your favorite streaming service?")
    print("\n\t A - Netflix \n\t B - Hulu \n\t C - Prime Video \n\t D - HBO Max \n\t")
    answer8 = input("\t").upper()

#question 9 

print("9. Which season is your favorite?")
print("\n\t A - Winter \n\t B - Spring \n\t C - Summer \n\t D - Fall \n\t")
answer9 = input("\t")
#error checking
while answer9 != "A" and answer9 != "B" and answer9 != "C" and answer9 != "D":
    print ("Please choose A, B, C, or D")
    print("9. Which season is your favorite?")
    print("\n\t A - Winter \n\t B - Spring \n\t C - Summer \n\t D - Fall \n\t")
    answer9 = input("\t").upper()

#question 10

print("10. What is your favorite dessert ?")
print("\n\t A - Ice Cream \n\t B - Cake \n\t C - Pie \n\t D - Hand-Held Pastries \n\t")
answer10 = input("\t")
#error checking
while answer10 != "A" and answer10 != "B" and answer10 != "C" and answer10 != "D":
    print("Please choose A, B, C, or D")
    print("10. What is your favorite dessert ?")
    print("\n\t A - Ice Cream \n\t B - Cake \n\t C - Pie \n\t D - Hand-Held Pastries \n\t")
    answer10 = input("\t").upper()

#errprchecking for questions 

#Logic
total = 0
#1
if answer1 == "A":
    total = total + 4
elif answer1 == "B":
    total = total + 3
elif answer1 == "C":
    total = total + 2
elif answer1 == "D":
    total = total + 1
#2
if answer2 == "A":
    total = total + 4
elif answer2 == "B":
    total = total + 3
elif answer2 == "C":
    total = total + 2
elif answer2 == "D":
    total = total + 1
#3
if answer3 == "A":
    total = total + 4
elif answer3 == "B":
    total = total + 3
elif answer3 == "C":
    total = total + 2
elif answer3 == "D":
    total = total + 1
#4
if answer4 == "A":
    total = total + 4
elif answer4 == "B":
    total = total + 3
elif answer4 == "C":
    total = total + 2
elif answer4 == "D":
    total = total + 1
#5
if answer5 == "A":
    total = total + 4
elif answer5 == "B":
    total = total + 3
elif answer5 == "C":
    total = total + 2
elif answer5 == "D":
    total = total + 1
#6
if answer6 == "A":
    total = total + 4
elif answer6 == "B":
    total = total + 3
elif answer6 == "C":
    total = total + 2
elif answer6 == "D":
    total = total + 1
#7
if answer7 == "A":
    total = total + 4
elif answer7 == "B":
    total = total + 3
elif answer7 == "C":
    total = total + 2
elif answer7 == "D":
    total = total + 1

#8
if answer8 == "A":
    total = total + 4
elif answer8 == "B":
    total = total + 3
elif answer8 == "C":
    total = total + 2
elif answer8 == "D":
    total = total + 1
#9
if answer9 == "A":
    total = total + 4
elif answer9 == "B":
    total = total + 3
elif answer9 == "C":
    total = total + 2
elif answer9 == "D":
    total = total + 1
#10
if answer10 == "A":
    total = total + 4
elif answer10 == "B":
    total = total + 3
elif answer10 == "C":
    total = total + 2
elif answer10 == "D":
    total = total + 1
    



# make your inpouts upp or lower
#put .lower or .upper next ti answer1 or answer 2.
#disply results
print(f"Your total score is {total}.")

#Logic for personalities
if total >=31 and total <=40:
    print(" You are Apple Cider! This means you are cozy, warm and down-to-earth, and love comfort. You enjoy fall vibes, traditions, and calm moments.")
elif total >=21 and total<= 30:
    print ("You are a Blueberry Donut! This means you are kind, easy-going, and genuine. You value comfort and familiaruty but aren't afraid to mix things up.")
elif total >=11 and total <= 20:
    print("You are a Pumpkin Strudel! You are warm and inviting, with a comforting presence. You are creative and thoughtful with depth and layers.")
elif total >= 1 and total <= 10:
    print("You are a Strawberry Fruit Tart! You are bright and charming with sweetness and confidence. You love to serve tohers and are a bit of a people pleaser, with a creative flair others envy.")
#make sure it holds invalid errors with inputs





