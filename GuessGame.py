import  random
secter_num = random.randint(1,6)
guess_limit = 4
guess_count = 0

# for feedback ergjamshid@gmail.com
user = ''
lc = ''
while user != '0':
    user = int(input('Guess: '))
    guess_count += 1
    if secter_num == user:
        print("You win!!! Yhaa- Whooo Congratulation, HOW LUCKY You are !!!!")
        print('''
                enter
                0 - to close
                1 - to continue''')
        lc = int(input('your option: '))
        if lc == 1:
            guess_count = 0
        break
    elif guess_count==3:
        print('''YOU LOSE choose option below
        enter
        0 - to close
        1 - to continue''')
        lc = int(input('your option: '))
        if lc==1:
            guess_count = 0
    else:
        print(" Wrong  Try again  ")


