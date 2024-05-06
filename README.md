*Note:* This only works for Windows machines

# Setup
- Clone this repo
- Get your own [NASA API key](https://api.nasa.gov/) and paste it into a .env file
- Set this script to run every day using your preferred method (or see below)

# Running the script
Set up the script to run daily on Windows Task Scheduler
1. Press `Windows + S` and type "Task Scheduler," then open the application.

2. In the right-hand panel, click on "Create Basic Task."

3. Give your task a name and description, then click "Next."

4. Choose the "Daily" option and click "Next."

5. Set the start date and your desired time, then click "Next."

6. Choose the "Start a program" option and click "Next."

7. Browse to the location of your Python executable (`python.exe`).

8. In the "Add arguments" field, type the name of your script (e.g., `apod.py`).

9. In the "Start in" field, put the directory where your Python script is located.

10. Click "Next," review your settings, and click "Finish."
