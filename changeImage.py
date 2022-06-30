#!/usr/bin/env python3
#import os and Python Image Library Modules
import os
from PIL import Image

#initialise location variables

old_file_location = os.path.expanduser("~") + "/supplier-data/images/"
new_file_location = "/supplier-data/images/"

#iterate through directory, resizing and changing format to JPEG
for image in os.listdir(old_file_location):
        if "." not in image[0]:
                img = Image.open(old_file_location + image)
                img.resize((600, 400)).convert("RGB").save(new_file_location + image.split('.')[0] + ".jpeg", "JPEG")
                img.close()