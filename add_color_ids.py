#!/usr/bin/python

import json

newdata={}
with open('english.json') as json_file:
    data = json.load(json_file)
    for key, value in data.iteritems():
        if key.startswith('GUI_PALETTECOLOR_'):
            number = key.split('_', 2)
            number = number[2]
            newdata[key]='%s %s'%(value, number)
        else:
            newdata[key]=value

with open('englishnumbers.json','w') as outfile:
    json.dump(newdata,outfile, indent=4, sort_keys=True)
