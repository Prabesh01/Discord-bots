#I was able to make this bot only because of thi blog: https://www.sicara.ai/blog/object-detection-template-matching
#Thansk to the writter. I don't know opencv and numpy well so only way to make this was to modify other's code.
#Any other codes I found on internet weren't givng me expected output.

################################################################################################################
# The template image (ab.png) used in this code to identify गजब छ बा! from the newspaper image can be downloaded from here: https://i.imgur.com/1T7O4SJ.png
################################################################################################################

import requests
import re
import wget
import os
import cv2
import numpy as np
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import sys

if os.path.exists('temp.jpg'):
    os.remove('temp.jpg')
if os.path.exists('output.jpg'):
    os.remove('temp.jpg')

url='https://epaper.ekantipur.com/kantipur/'
myhook='webhook_url'
r=requests.post(url)

match=re.findall('/files/epaper/kantipur/pdf/(?:(?!").)*', r.text)
if('thumbs' in str(match[1])):
    static=re.sub('thumbs', 'large', str(match[1]))
else:
    static=str(match[1])
link='https://epaper.ekantipur.com'+str(static)
wget.download(link,out='temp.jpg')
#urllib.request.urlretrieve(link, "temp.jpg")

DEFAULT_TEMPLATE_MATCHING_THRESHOLD = 0.5


class Template:
    def __init__(self, image_path, label, color, matching_threshold=DEFAULT_TEMPLATE_MATCHING_THRESHOLD):
        self.image_path = image_path
        self.label = label
        self.color = color
        self.template = cv2.imread(image_path)
        self.template_height, self.template_width = self.template.shape[:2]
        self.matching_threshold = matching_threshold

image = cv2.imread("temp.jpg")


template = Template(image_path="ab.png", label="1", color=(0, 0, 255))

detections = []
#for template in templates:
template_matching = cv2.matchTemplate(
    template.template, image, cv2.TM_CCOEFF_NORMED
)

match_locations = np.where(template_matching >= template.matching_threshold)

for (x, y) in zip(match_locations[1], match_locations[0]):
    match = {
        "TOP_LEFT_X": x,
        "TOP_LEFT_Y": y,
        "BOTTOM_RIGHT_X": x + template.template_width,
        "BOTTOM_RIGHT_Y": y + template.template_height,
        "MATCH_VALUE": template_matching[y, x],
        "LABEL": template.label,
        "COLOR": template.color
    }
    
    detections.append(match)
        
if detections:
    print('\ndetected')
    image_with_detections = image.copy()
    crop_img = image_with_detections[detections[0]["TOP_LEFT_Y"]:detections[0]["BOTTOM_RIGHT_Y"]+450,detections[0]["TOP_LEFT_X"]:detections[0]["BOTTOM_RIGHT_X"], ]
    cv2.imwrite("output.jpg", crop_img)
    webhook = DiscordWebhook(username='Routiney', avatar_url='https://cdn.discordapp.com/app-icons/786534057437691914/8dd876fd77d51452a5e3b3df4bc0ce18.png?size=256', content='Disclaimer: This bot everyday goes to ekantipur\'s site and fetches its first page. Then, it looks for गजब छ बा! and if available, it crops the required part. This all is done automatically using an AI library, so sometimes it may not work out well and wrong part of the newspaper might get posted.\n<https://epaper.ekantipur.com/kantipur/'+str(datetime.today().strftime('%Y-%m-%d'))+'>', url=myhook)
    with open("output.jpg", "rb") as f:
        webhook.add_file(file=f.read(), filename='abin.jpg')
    webhook.execute()
    os.remove('temp.jpg')
    os.remove('output.jpg')
else:
    print('\nnot detected')
    os.remove('temp.jpg')
