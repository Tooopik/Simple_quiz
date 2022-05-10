from question import question
from random import randint

questionList = []
for q in question.keys():
    questionList.append(q)

numbersOfQuestions = 10
if len(questionList) < numbersOfQuestions:
    numbersOfQuestions = len(questionList)

print('Welcome in quiz game about ....', '\n')

while True:
    score = 0
    idx = 0
    while idx < numbersOfQuestions:
        idx += 1
        print(f'Question {idx}: ')
        choseQuestion = randint(0, len(questionList) - 1)
        questionText = questionList.pop(choseQuestion)
        print(f'{questionText}')
        for answer in question[questionText]:
            if answer != 0:
                print(f'{answer.upper()} : {question[questionText][answer]}')
        print('Choose the correct answer:')
        userChoice = input('>>> ')
        if userChoice.upper() == question[questionText][0].upper():
            print('GOOD!', '\n')
            score += 1
        else:
            print(
                f'{userChoice.upper()} is wrong, correct answer: {question[questionText][0].upper()}', '\n')

    print(f'Your score: {score}\n')  # Finish section
    print('Do you want play again? (y/N)')
    userChoice = input('>>> ')
    if userChoice == 'N':
        break
    else:
        score = 0
