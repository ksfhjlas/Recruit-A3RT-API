#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json

apikey = "t3yTIONK5tfoySZIqukmblGZ7BXZgYO3"
in_moji=u"馬"
a="馬"
style=0
separation=2
params = urllib.urlencode({'apikey': apikey,
                           'previous_description': a,
                           'style': style,
                           'separation': separation,
                           })
print "https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict?%s" % params
f = urllib.urlopen("https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict?%s" % params)
j=f.read()
con=json.loads(j)
#dsaf
for i in con["suggestion"]:
    print in_moji+i