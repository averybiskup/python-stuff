import requests
import time
import shutil
import datetime
import os

# Getting response with requests lib
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + os.environ['nasa_key'])
content = str(response.content)

# Getting the correct URL
imgURL = content.split('"url":')[1][1:-5]

# Preparing filename
date = str(datetime.datetime.now().date())
filename = date + ".jpg"

r = requests.get(imgURL, stream=True)

print("Getting photo from: " + imgURL)

# Checking for status
if r.status_code == 200:

    # Opening as f
    with open("images/" + filename, 'wb') as f:
        print("Creating file: " + filename)

        # Decoding
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

else:
    print("Wasn't able to get image.")
