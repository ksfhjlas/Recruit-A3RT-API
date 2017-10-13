#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pya3rt
import random
import time

apikey = "t3yTIONK5tfoySZIqukmblGZ7BXZgYO3"
client = pya3rt.TextSuggestClient(apikey)

a="私"
b=[]
co=10

while co>0:
    c=client.text_suggest(a)
    t1=time.time()
    print c
    for i in c["suggestion"]:
        print i
        b.append(i)
    a=random.shuffle(b)
    b=[]
    co-=1
    while True:
        t2=time.time()
        if t2-t1>60:
            break
