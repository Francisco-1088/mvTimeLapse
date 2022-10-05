import meraki
import os
import requests
import time
import shutil
import datetime
from dateutil import tz

dashboard = meraki.DashboardAPI(api_key='API_KEY')
zone = tz.gettz('America/Bogota')
# Set starting date and time
date = datetime.datetime(2022,2,8,11,4,31, tzinfo=zone)
# Set timelapse interval in seconds
lapse_int = 120
# Set length of timelapse in seconds
lapse_length = 3600

for i in range(0, lapse_length, lapse_int):
    print(date)
    snap = dashboard.camera.generateDeviceCameraSnapshot(serial='CAMERA_SERIAL', timestamp=date.isoformat())
    time.sleep(10)
    local_file = open(f'./lapse/{date.isoformat().replace(":","-")}.jpg', 'wb')
    resp = requests.get(snap['url'], stream=True)
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    local_file.close()
    date += datetime.timedelta(seconds=lapse_int)

img_string = date.isoformat().split('T')[0]

os.system(f'convert -delay 10 -loop 0 ./lapse/{img_string}*.jpg timelapse.gif')
