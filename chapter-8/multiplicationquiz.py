import random
import threading
import time

ques = 10
score = 0


print("Welcome!, you will have 8 seconds to answer each question")

time.sleep(3)

for quesnum in range(ques):
    max = 3
    chance= 0
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    right = a * b
    while chance < max:
        chance += 1
        timer =threading.Timer(8,print,[" UHH OH !!  Your time is up"]) 
        timer.start() 
        user= input('#%s: %s * %s = ' % (quesnum+1, a, b))
        timer.cancel()
        if int(user) == right:
            print('Your answer is correct')
            break
        else:
            if chance == max:
                print('Out of tries. Please wait for the next question.')
                time.sleep(1)
            else: 
                print('Your answer is wrong . Try again.!')
                continue