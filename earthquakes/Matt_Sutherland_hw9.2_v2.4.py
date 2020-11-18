#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:14:40 2020

@author: msutherland
"""

import urllib.request  # instead of urllib2 like in Python 2.7
import json

#Input validation
quake_min = 1.0

#Request user input    
quake_mag =float(input("What magnitude earthquake are you looking for? "))

def findQuakes(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
#    while quake_mag > quake_min:
    for i in theJSON["features"]:
            if i["properties"]["mag"] == quake_mag:
#                print("Found your quakes!\n")
                print("%2.2f" % i["properties"]["mag"], i["properties"]["place"])
    print("*Successful Real-Time Search Complete*")  
 
'''
    #Print how many times the someone felt and reported the quake
    print("\n\nEvents that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0):
                print("%2.1f" % i["properties"]["mag"], i["properties"]
                      ["place"], " reported " + str(feltReports) + " times")
''' 
   
'''
main function for API
'''   
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()) + " searching.......... ")
    if (webUrl.getcode() == 200):
        data = webUrl.read().decode("utf-8")
        # print out our customized results
        findQuakes(data)
    else:
        print("Received an error from server, cannot retrieve results " +
              str(webUrl.getcode()))

if __name__ == "__main__":
    main()
