#!/usr/bin/env python
# coding=utf-8

import json
import sys


with open(sys.argv[1], "r") as f:
    data = json.load(f)

for item in data:
    print item['title']
    print item['price']
    if item.get('power'):
        print "Výkon:", item['power'], "kW"
    if item.get('year'):
        print "Ročník:", item['year']
    if item.get('mileage'):
        print "Najeto:", item['mileage']
    print
    if item.get('description', ""):
        print item['description'].strip()
    print
    print item['permalink']
    print '-' * 60
