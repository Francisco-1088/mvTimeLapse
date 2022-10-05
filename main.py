import meraki
import os
import requests
import time
import shutil
import datetime
import config
from dateutil import tz

dashboard = meraki.DashboardAPI(api_key=config.API_KEY)
zone = tz.gettz(config.time_zone)
# Set starting date and time
date = datetime.datetime(config.start_year,config.start_month,config.start_day,config.start_hour,config.start_minute,config.start_second, tzinfo=zone)
# Set timelapse interval in seconds
lapse_int = config.lapse_interval
# Set length of timelapse in seconds
lapse_length = config.lapse_length

for i in range(0, lapse_length, lapse_int):
    print(date)
    snap = dashboard.camera.generateDeviceCameraSnapshot(serial=config.CAMERA_SERIAL, timestamp=date.isoformat())
    time.sleep(10)
    local_file = open(f'./lapse/{date.isoformat().replace(":","-")}.jpg', 'wb')
    resp = requests.get(snap['url'], stream=True)
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    local_file.close()
    date += datetime.timedelta(seconds=lapse_int)

img_string = date.isoformat().split('T')[0]

os.system(f'convert -delay 10 -loop 0 ./lapse/{img_string}*.jpg {config.lapse_file_name}')
