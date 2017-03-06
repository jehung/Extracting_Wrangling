#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def numDigits(n): 
    return len(filter(lambda m:m.isdigit(), str(n)))

def fix_area(area):
    if area.startswith('{'):
        area_list = area.split("|")
        area1 = area_list[0][1:]
        area2 = area_list[1][:-1]
        
        #print(area2)
        
        if len(area1) > len(area2):
            finalarea = float(area1)
        else:
            finalarea = float(area2)
    elif (area == 'NULL') or (area == ''):
        finalarea = 'NULL'
    else:
        finalarea = float(area)
    
    return finalarea
        



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r", encoding='cp437', errors='replace') as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = next(reader)

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
                
            data.append(line)

    return data


def test():
    data = process_file(CITIES)
    print(data[8]["areaLand"])
    print("Printing three example results:")
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    
    
    

if __name__ == "__main__":
    test()