# mvTimeLapse
Fetch snapshots from your MV Cameras and build a timelapse from them

![alt text](lapse/sample.gif)

This has been tested on Python 3.9 on Mac OS 12.1

How to use:
1. Clone the repo
2. Edit the main.py file
  -Line 9: Replace "API_KEY" with your API key
  -Line 10: Set your timezone
  -Line 12: Set the start date for fetching snapshots
  -Line 14: Set the interval at which you want to fetch snapshots in seconds
  -Line 16: Set the total time window you're looking at in seconds
  -Line 31: Change "timelapse.gif" to whatever name you want in your timelapse file
3. Run "pip install -r requirements.txt"
4. Run "python main.py"
