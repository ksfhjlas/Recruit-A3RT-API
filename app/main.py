#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pya3rt
import random

def main(argv):
  apikey = "t3yTIONK5tfoySZIqukmblGZ7BXZgYO3"
  client = pya3rt.TextSuggestClient(apikey)

  a="我"
  b=[]
  while True:
    c=client.text_suggest(a)
    for i in c["suggestion"]:
      print i
      b.append(i)
    a=random.shuffle(b)
    b=[]



  for i, v in enumerate(argv):
    print("argv[{0}]: {1}".format(i, v))
