#!/usr/bin/env python3
#import requests and os modules
import requests
import os

#intialise variables for file location and the url where the files are to be uploaded
file_location = os.path.expanduser("~") + "/supplier-data/images/"
url = "http://<ip>/upload/"

#iterate through directory and upload jpeg files only to url using requests
for image in os.listdir(file_location):
    if image.endswith(".jpeg"):
        with open(image, "rb") as opened:
            r = requests.post(url, files={"file": opened})