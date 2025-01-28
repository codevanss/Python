questions = ("How many elements are in the periodic table ? : ",
             "Which Animal lays ther largest eggs ? : ",
             "What is the most abundant gas in the Earth's Atmosphere ? : ",
             "How many bones are present in human body ? : ",
             "Which Planet in the solar system is the Hottest ? : ")

options = (("A: 116" , "B: 117" , "C: 118" , "D: 119"),
           ("A: Whale" , "B: Crocodile" , "C: Elephant" , "D: Ostrich"),
           ("A: Nitrogen" , "B: Oxygen" , "C: Carbon_Dioxide" , "D: Hydrogen"),
           ("A: 206" , "B: 207" , "C: 208" , "D: 209"),
           ("A: Mercury" , "B: Venus" , "C: Earth" , "D: Mars"))
answers = ("C" , "D" , "A" , "A" , "B")
guesses =[]
score = 0
questions_num = 0 

for question in questions:
    print("-------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score +=1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{answers[questions_num]} is the correct answer")
    questions_num +=  1
    
print("----------")
print("---Result---")
print("----------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("Guess: ", end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score =int(score/ len(questions)*100)
print(f"Your Score is: {score}%")