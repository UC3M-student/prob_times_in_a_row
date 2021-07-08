from numpy import random
##### prob. three times in a row
time = 0
n = 0
u = 0
while time <= 10001:
    x = random.randint(36)
    n = n + 1
    if x == 5:
        y = random.randint(36)
        if y ==5:
            z = random.randint(36)
            if z ==5:
                time = time + 1
                a = 1/n
                print("Prob. same number 3 times in a row")
                u = u + (1/n)
                n = 0
                print("Numero de veces ejecutado el problema:", time)
result = u/10001
print(result)
