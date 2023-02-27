# from requests import get
import json
from urllib.parse import urlparse
from requests import get
from pathlib import Path
import time

# https://stackoverflow.com/questions/26766840/comma-separator-between-json-objects-with-json-dump
data = {}
json_location = 'ASK-paint/ASK-paint-user-only.json'
media_location = './media/ask/'
with open(json_location, 'r') as f:
    for i,line in enumerate(f):
        # print(line)
        data[i] = json.loads(line)

# print(next(iter(data)))
print(data[0]['photos'], len(data))

def photo_downloader(urls, download_location):
    for photo_url in urls['photos']:
        url_obj = urlparse(photo_url)   

        file_name = url_obj.path.replace("/media/", "")
        path = str(Path(download_location, file_name))
        if not Path(path).is_file():
            with open(path, "wb") as file:
                file.write(get(photo_url).content)
for i in range(len(data)):
    try:
        photo_downloader(data[i], media_location)
        print("No.%d ok. remain %d" % (i, len(data)-i))
        time.sleep(0.2)

    except Exception as e:
        print("No.%d has a error" % (i))
        continue

# photo_downloader(data[0], "./media/")