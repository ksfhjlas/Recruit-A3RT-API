#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json

def main(argv):
  apikey = "t3yTIONK5tfoySZIqukmblGZ7BXZgYO3"
  in_moji = u"馬"
  a = "馬"
  style = 0
  separation = 2
  params = urllib.urlencode({'apikey': apikey,
                             'previous_description': a,
                             'style': style,
                             'separation': separation,
                             })
  f = urllib.urlopen("https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict?%s" % params)
  j = f.read()
  con = json.loads(j)

  b=[]
  for i in con["suggestion"]:
    b.append(in_moji + i)

  for i in b:
    print i

  for i, v in enumerate(argv):
    print("argv[{0}]: {1}".format(i, v))
