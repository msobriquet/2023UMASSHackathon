from random import randrange

data = [] 
for i in range(30): #will be multiplied by 2 so 60 secs
    seed = (randrange(0, 200))/100 #random float between 0-2
    data.append(seed + (i * 1.5))

print(data)    

