# mvTimeLapse
Fetch snapshots from your MV Cameras and build a timelapse from them

![alt text](lapse/sample.gif)

This has been tested on Python 3.9 on Mac OS 12.1

How to use:
1. Clone the repo
2. Edit the config.py file
  * Add your API_Key under `API_KEY`
  * Add the Camera you're looking to work with under `CAMERA_SERIAL`
  * Add your timezone under `time_zone`
  * Set the start date by filling each of the items (year, month, day, hour, minute and second)
  * Set the interval at which you want to fetch snapshots in seconds under `lapse_int`
  * Set the total time window you're looking at in seconds under `lapse_length`
  * Set the desired output filename under `lapse_file_name`
3. Run "pip install -r requirements.txt"
4. Run "python main.py"

NOTE: The steps above work well for Mac OS, but on Windows you will have to comment out the last line of the script. Then go to the folder where your time lapse images where stored (`/lapse`), select all of them, do a right-click and then click on Create Movie.

References:
* [Meraki Snapshot API](https://developer.cisco.com/meraki/mv-sense/#!rest-api/snapshot)
