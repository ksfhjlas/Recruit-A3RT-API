#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pya3rt

def main(argv):
  apikey = "t3yTIONK5tfoySZIqukmblGZ7BXZgYO3"
  client = pya3rt.TextSuggestClient(apikey)


  for i, v in enumerate(argv):
    print("argv[{0}]: {1}".format(i, v))
