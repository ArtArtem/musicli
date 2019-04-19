import random
import time
global cards, score, scorebot
while 2 == 2:
    for i in range(10):
        print('###' * 10)
    cards = [2,3,4,5,6,7,8,9,10,11,3,4,5]
    cards *= 4
    score = 0
    scorebot = 0
    play = 0


    def take():
        global cards, score, scorebot
        number = random.choice(cards)
        score += number
        print('Вам выпало', number)


    def takebot():
        global cards, score, scorebot
        time.sleep(2)
        number = random.choice(cards)
        scorebot += number
        print('Боту выпало', number)
        print('Результат бота:', scorebot)


    print('Будете играть? y/n')
    if input() == 'y':
        play = 1
        while score <= 21 and play == 1:
            print('Ваш результат:', score)
            print('Будете брать? y/n')
            if input() == 'y':
                take()
            else:
                play = 0
    if score > 21:
        print('Вы проиграли, ваш результат', score)
        play = 0
    else:
        print('Ваш результат', score ,'. Очередь бота')
        play = 1
    if play == 1:
        while scorebot < score:
            takebot()

        if scorebot > 21:
            print('Вы выиграли')
        elif score == scorebot:
            print('Ничья!')
        else:
            print('Вы проиграли!')
