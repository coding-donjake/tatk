import sys
import time
import random

while True:
    x = random.randint(1, 5)
    
    if (x == 5):
        raise Exception('test exception due to x = 5')
    
    print(f'random number: {x}', flush=True)
    
    if x == 1:
        break
    
    time.sleep(1)

sys.exit(0)
