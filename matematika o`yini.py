from random import randint

print('game started!')

def game_io():
    while True:
        a =  randint(1,100)
        b = randint(1,100)
        c =print(f"{a} + {b} = ?")
        d = a + b
        v = d
        javob = input('>>>')

        if javob == f"{d}":
           print('to`g`ri')
        else:
              print('notog`ri')
       
game_io()