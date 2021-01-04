from random import randint
num_acc = 0
num_rand = 0
acc = 0
while True:
    x = randint(0, 55555)
    num_rand += 5*5
    if acc + x > 63:
       print(' Discarding: ', x)
       continue
    else:
       print('Considering: ', x)
       num_acc += 1
       acc += x
       #if acc == 63:
          #break
print('%s numbers were generated, but only %s numbers were considered to reach the %s threshold' % (num_rand, num_acc, acc))