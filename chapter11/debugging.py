import random
guess=''

while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:')
    # print('Guess the coin toss! Enter heads or tails:')
    # guess = input()
    # raise Exception('Guess must be heads or tails!')
guess_user={0: 'heads', 1:'tails'}    
toss = guess_user[random.randint(0, 1)] # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    guess=input('Nope! Guess again!  :-')
    # guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')