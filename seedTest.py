# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 16:21:56 2021

@author: danis
"""
#=============================================================================
import random
import datetime

import main

ct = datetime.datetime.now()
a = []
random.seed('c')
print(ct)


def defSeed(seed):
    random.seed(seed)
    a = []
    for i in range(100):
        if i <= 9:
            a.append(random.randint(10, 20))
        elif 9 < i <= 20:
            a.append(random.randint(21, 50))
        elif 20 < i <= 30:
            a.append(random.randint(51, 70))
        elif 30 < i <= 80:
            a.append(random.randint(71, 120))
        elif 80 < i <= 90:
            a.append(random.randint(121, 150))
        if i > 90:
            a.append(random.randint(151, 170))
    random.shuffle(a)
    #print(random.choice(a))
    #print(random.choice(a))
    #print(random.choice(a))
    #print(a)
    #print(len(a))
    return a


def extractorsum(even, operator):
    if even is False and operator is False:
        return True
    else:
        return even and operator

# even = True
# operator = False
# print(extractorsum(even, operator))
out = main.setOutputName('/home/danis/Escritorio/tonto.png','/home/danis/Escritorio')
print(out)


# a = defSeed('c')
# b = defSeed('c')
# if a == b:
#     print('Son iguales')
# =============================================================================
# =============================================================================
# random.seed('c')
# b=[]
# for i in range(20):
#     b.append(random.randint(60,130))
# print(b)
# if(a==b):
#     print("iguales")
# else:
#     print("no iguales")
# =============================================================================