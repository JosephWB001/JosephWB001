prompt1 = "How many sheep do you have?\n"
answer1 = input(prompt1)

if answer1 == '0' :
    sheep = -1
elif answer1 == '1' :
    sheep = 1
elif answer1 == '2' :
    sheep = 1
elif answer1 == '3' :
    sheep = 1
elif answer1 == '4' :
    sheep = 2
elif answer1 == '5' :
    sheep = 2
elif answer1 == '6' :
    sheep = 3
elif answer1 == '7' :
    sheep = 3
elif answer1 >= '8' :
    sheep = 4
elif answer1 >= '10' : # I got an error when I entered 10 into the prompt, but after adding this line of code everything was fine
    sheep = 4

prompt2 = "How many boar do you have?\n"
answer2 = input(prompt2)
if answer2 == '0' :
    boar = -1
elif answer2 == '1' :
    boar = 1
elif answer2 == '2' :
    boar = 1
elif answer2 == '3' :
    boar = 2
elif answer2 == '4' :
    boar = 2
elif answer2 == '5' :
    boar = 3
elif answer2 == '6' :
    boar = 3
elif answer2 == '7' :
    boar = 4
elif answer2 >= '10' :
    boar = 4

prompt3 = "How many cattle do you have?\n"
answer3 = input(prompt3)
if answer3 == '0' :
    cattle = -1
elif answer3 == '1' :
    cattle = 1
elif answer3 == '2' :
    cattle = 2
elif answer3 == '3' :
    cattle = 2
elif answer3 == '4' :
    cattle = 3
elif answer3 == '5' :
    cattle = 3
elif answer3 == '6' :
    cattle = 4
elif answer3 >= '10' :
    cattle = 4
score = int(sheep + boar + cattle)
print(f'The final score is {score} unless,\n') # Had some trouble getting the score in the curly brackets to work

prompt4 = "Do you have any bonus cards? Please answer Y or N\n"
answer4 = input(prompt4)
if answer4 == 'Y':
    prompt5 = "How many points are they worth?\n"
    bonus = int(input(prompt5))
    final = (score + bonus)
    print(f'Your real final score is {final}\n')
else:
    print(f'I am sorry, better luck next time! Your final score is {score}\n') # This was the only way I could get the bonus cards to work, I hope that's alright
