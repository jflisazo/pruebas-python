import random
import time

random.seed(time.time())

acertijo = int(random.randint(0,101))
num = -1
   
while acertijo != num:
    print('Ingrese un numero entre 0 y 100')
    num = int(input())
    
    if num < acertijo:
        print('Muy bajo!!!')
    elif num > acertijo:
        print('Muy alto!!!')
    else:
        print('Acertaste!!! Eres un genio!!!')

