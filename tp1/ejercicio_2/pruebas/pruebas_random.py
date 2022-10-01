# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:07:18 2022

@author: Julian Traversaro
"""

import random

random.seed(a=179)
print(random.random())
for i in range(3):
    random.seed(a=179)
    print(random.randint(0,1000))
    